import graphene
from graphene_django import DjangoObjectType
from .models import Track, Like
from users.schema import UserType
from django.db.models import Q
from graphql_jwt.decorators import login_required


class TrackType(DjangoObjectType):
    """
    The TrackType class generally converts python database Model[Track] to Graphql Object Type.
    """
    class Meta:
        model = Track


class LikeType(DjangoObjectType):
    """
    The LikeType class generally converts python database Model[Like] to Graphql Object Type.
    """
    class Meta:
        model = Like


class Query(graphene.ObjectType):
    """
    This Query class allows you to fetch/search data related to Track model.
    """
    # Graphql query parameters
    tracks = graphene.List(TrackType, search=graphene.String())
    likes = graphene.List(LikeType)

    def resolve_tracks(self, info, search=None):
        """
        This method has one (search) parameter which default is None. Ignoring the (search) parameter you get all the (Track) tracks list. If the parameter 
        is provided the you get only the list of tracks according to the search parameter.
        """
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
        """
        This method returns all the likes as list those belongs to the Track model.
        """
        return Like.objects.all()

class CreateTrack(graphene.Mutation):
    """
    This CreateTrack class allows to create a track on preference.
    """
    # Graphql query parameter
    track = graphene.Field(TrackType)

    class Arguments:
        """
        This Arguments class takes 3 inputs for the track object creation. Inputs are (title,description,url).
        """
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()
    
    @login_required
    def mutate(self, info, **kwagrs):
        """
        This method generally creates a Track object according to the given parameters
        """
        user = info.context.user
        track = Track(title=kwagrs.get('title'), description=kwagrs.get('description'), url=kwagrs.get('url'), posted_by=user)
        track.save()

        return CreateTrack(track=track)



class UpdateTrack(graphene.Mutation):
    """
    This UpdateTrack class allows you to make changes to the tracks user created.
    """
    # Graphql query parameter
    track = graphene.Field(TrackType)

    class Arguments:
        """
        This Arguments class takes 4 inputs for the track object updation. Inputs are (trackId,title,description,url).
        """
        track_id = graphene.Int()
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()

    @login_required
    def mutate(self, info, **kwargs):
        """
        This method allows you to insert a track object according to the given parameters into the database. It requires user authentication.
        """
        user = info.context.user
        track = Track.objects.get(id=kwargs.get('track_id'))
        track.title = kwargs.get('title')
        track.description = kwargs.get('description')
        track.url = kwargs.get('url')

        track.save()

        return UpdateTrack(track=track)


class DeleteTrack(graphene.Mutation):
    """
    This DeleteTrack class allows you to delete a track from the database.
    """
    # Graphql query parameter
    track_id = graphene.Int()

    class Arguments:
        """
        This Arguments class takes 1 input(track_id) for the track deletion process. 
        """
        track_id = graphene.Int(required=True)
    
    @login_required
    def mutate(self, info, **kwagrs):
        """
        This method takes care of the deletion process. It delete a track record from the database. It requires user authentication.
        """
        user = info.context.user
        track_id = kwagrs.get('track_id')
        track = Track.objects.get(id=track_id)

        track.delete()

        return DeleteTrack(track_id=track_id)


class CreateLikeTrack(graphene.Mutation):
    """
    This CreateLikeTrack allows you to add a track to the user preference.
    """
    # Graphql query parameters
    user = graphene.Field(UserType)
    track = graphene.Field(TrackType)

    class Arguments:
        """
        This Arguments class take 1 input (track_id)
        """
        track_id = graphene.Int()

    @login_required
    def mutate(self, info, **kwagrs):
        """
        This method adds a track to the user like list. It requires user authention.
        """
        user = info.context.user
        track_id = kwagrs.get("track_id")
        track = Track.objects.get(id=track_id)

        Like.objects.create(
            user=user,
            track=track
        )

        return CreateLikeTrack(user=user, track=track)


class Mutation(graphene.ObjectType):
    """
    This Mutation class allows you to write your query for the Track CRUD operations. Query starts with {create_track,update_track,delete_track,like_track}
    """
    create_track = CreateTrack.Field()
    update_track = UpdateTrack.Field()
    delete_track = DeleteTrack.Field()
    like_track = CreateLikeTrack.Field()