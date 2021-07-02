from simple_rest_client.resource import Resource


class CrudAuthResource(Resource):

    actions = {
        'jwt_create': {'method': 'POST', 'url': 'auth/jwt/create'},
        'jwt_refresh': {'method': 'POST', 'url': 'auth/jwt/refresh'},
        'jwt_verify': {'method': 'POST', 'url': 'auth/jwt/verify'},
    }
