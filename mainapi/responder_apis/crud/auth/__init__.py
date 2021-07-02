from .service import CrudAuthService


def authenticate_async(f):
    async def wrapper(*args, **kwargs):
        response = await CrudAuthService.verify(
            headers=kwargs.get('headers', dict())
        )
        if response.status_code != 200:
            return response

        return await f(*args, **kwargs)

    return wrapper
