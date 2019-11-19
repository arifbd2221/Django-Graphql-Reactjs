import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

from graphql_jwt.decorators import login_required



class UserType(DjangoObjectType):
    """
    
    """
    class Meta:
        model = get_user_model()


class QueryUser(graphene.ObjectType):
    user = graphene.Field(UserType, id=graphene.Int(required=True))
    me = graphene.Field(UserType)

    def resolve_user(self, info, id):
        return get_user_model().objects.get(id=id)

    @login_required
    def resolve_me(self, info):
        user = info.context.user
        return user

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    
    def mutate(self, info, **kwargs):
        username = kwargs.get('username')
        email = kwargs.get('email')
        password = kwargs.get('password')

        user = get_user_model()(username=username, email=email)

        user.set_password(password)

        user.save()

        return CreateUser(user=user)



class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()