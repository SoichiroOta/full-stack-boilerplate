import logging
from functools import wraps

from simple_rest_client.exceptions import ErrorWithResponse


logger = logging.getLogger(__name__)


def handle_request_error_with_response(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            response = f(*args, **kwargs)
        except ErrorWithResponse as exc:
            logger.exception(exc)
            response = exc.response
        except Exception as exc:
            logger.exception(exc)
            raise exc
        return response

    return wrapper


def handle_async_request_error_with_response(f):
    async def wrapper(*args, **kwargs):
        try:
            response = await f(*args, **kwargs)
        except ErrorWithResponse as exc:
            logger.exception(exc)
            response = exc.response
        except Exception as exc:
            logger.exception(exc)
            raise exc
        return response

    return wrapper
