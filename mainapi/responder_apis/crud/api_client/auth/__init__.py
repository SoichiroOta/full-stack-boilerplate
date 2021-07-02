from simple_rest_client.resource import AsyncResource


class CrudAuthResource(AsyncResource):

    actions = {
        'jwt_create': {'method': 'POST', 'url': 'auth/jwt/create'},
        'jwt_refresh': {'method': 'POST', 'url': 'auth/jwt/refresh'},
        'jwt_verify': {'method': 'POST', 'url': 'auth/jwt/verify'},
    }
