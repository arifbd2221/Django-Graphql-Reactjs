import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

from graphql_jwt.decorators import login_required



class UserType(DjangoObjectType):
    """
    The UserType class generally converts python database Model to Graphql Object Type.
    """
    class Meta:
        model = get_user_model()


class QueryUser(graphene.ObjectType):
    """
    This UserType class allows you to fecth user specific informations. As of now the user is the default django user.
    """
    # Graphql query parameters
    user = graphene.Field(UserType, id=graphene.Int(required=True))
    me = graphene.Field(UserType)

    def resolve_user(self, info, id):
        """
        This function returns a user taking a parameter called (id). This method is free of authentication.
        """
        return get_user_model().objects.get(id=id)

    @login_required
    def resolve_me(self, info):
        """
        This function returns a current user who is logged in. This method requires user authentication.
        """
        user = info.context.user
        return user

class CreateUser(graphene.Mutation):
    """
    This CreateUser class allows you to create a new user by providing (username,email,password) informations.
    """
    # Graphql query parameter
    user = graphene.Field(UserType)

    class Arguments:
        """
        This Arguments class takes inputs to create a user. Inputs are (username,email,password).
        """
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    
    def mutate(self, info, **kwargs):
        """
        This mutate method generally creates a user according to the provided informations.
        """
        username = kwargs.get('username')
        email = kwargs.get('email')
        password = kwargs.get('password')
        user = get_user_model()(username=username, email=email)
        user.set_password(password)

        user.save()

        return CreateUser(user=user)



class Mutation(graphene.ObjectType):
    """
    This Mutate class allows you to write your query for the user creation. Query starts with {create_user}    
    """
    create_user = CreateUser.Field()