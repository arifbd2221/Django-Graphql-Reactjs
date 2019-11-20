import graphene
import tracks.schema
import users.schema
import graphql_jwt

class Query(users.schema.QueryUser,tracks.schema.Query, graphene.ObjectType):
    """
    This Query class allows you fetch informations related to Track objects from the database.
    """
    pass

class Mutation(users.schema.Mutation ,tracks.schema.Mutation, graphene.ObjectType):
    """
    This Mutation class allows you to create user,track objects. Also it facilates you update,delete the objects as needed. It also takes care of
    the user authentication process. It logins a user and returns a unique JsonWebToken for further authentications.
    """
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

# registering Quey and Muation to the graphql schema.
schema = graphene.Schema(query=Query, mutation=Mutation)