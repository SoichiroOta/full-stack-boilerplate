from functools import wraps

from .service import CrudAuthService


def authenticate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        response = CrudAuthService.verify(
            headers=kwargs.get('headers', dict())
        )
        if response.status_code != 200:
            return response

        return f(*args, **kwargs)

    return wrapper
