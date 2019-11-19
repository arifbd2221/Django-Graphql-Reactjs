import graphene
from graphene_django import DjangoObjectType

from .models import Track, Like
from users.schema import UserType

from django.db.models import Q

from graphql_jwt.decorators import login_required


class TrackType(DjangoObjectType):
    class Meta:
        model = Track


class LikeType(DjangoObjectType):
    class Meta:
        model = Like


class Query(graphene.ObjectType):
    tracks = graphene.List(TrackType, search=graphene.String())
    likes = graphene.List(LikeType)

    def resolve_tracks(self, info, search=None):
        if search:

            filter = (
                Q(title__icontains=search) |
                Q(description__icontains=search) |
                Q(url__icontains=search) |
                Q(posted_by__username__icontains=search)
            )

            return Track.objects.filter()
        return Track.objects.all()

    def resolve_likes(self, info):
        return Like.objects.all()

class CreateTrack(graphene.Mutation):
    track = graphene.Field(TrackType)

    class Arguments:
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()
    
    @login_required
    def mutate(self, info, **kwagrs):

        user = info.context.user
        """ user = info.context.user

        if user.is_anonymous:
            raise Exception("Log in to add track") """

        track = Track(title=kwagrs.get('title'), description=kwagrs.get('description'), url=kwagrs.get('url'), posted_by=user)
        track.save()
        return CreateTrack(track=track)



class UpdateTrack(graphene.Mutation):
    track = graphene.Field(CreateTrack)

    class Arguments:
        track_id = graphene.Int()
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        track = Track.objects.get(id=kwargs.get('track_id'))

        """ if track.posted_by != user:
            raise Exception("Not permitted to update this track") """

        track.title = kwargs.get('title')
        track.description = kwargs.get('description')
        track.url = kwargs.get('url')

        track.save()

        return UpdateTrack(track=track)


class DeleteTrack(graphene.Mutation):
    track_id = graphene.Int()

    class Arguments:
        track_id = graphene.Int(required=True)
    
    @login_required
    def mutate(self, info, **kwagrs):
        user = info.context.user
        track_id = kwagrs.get('track_id')

        track = Track.objects.get(id=track_id)

        """ if track.posted_by != user:
            raise Exception("You are not peritted to delete this track") """

        track.delete()

        return DeleteTrack(track_id=track_id)


class CreateLikeTrack(graphene.Mutation):
    user = graphene.Field(UserType)
    track = graphene.Field(TrackType)

    class Arguments:
        track_id = graphene.Int()

    
    def mutate(self, info, **kwagrs):
        user = info.context.user

        if user.is_anonymous:
            raise Exception("Please Login first")

        track_id = kwagrs.get("track_id")

        track = Track.objects.get(id=track_id)

        Like.objects.create(
            user=user,
            track=track
        )

        return CreateLikeTrack(user=user, track=track)


class Mutation(graphene.ObjectType):
    create_track = CreateTrack.Field()
    update_track = UpdateTrack.Field()
    delete_track = DeleteTrack.Field()
    like_track = CreateLikeTrack.Field()