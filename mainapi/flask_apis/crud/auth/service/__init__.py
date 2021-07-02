import re

from simple_rest_client.exceptions import ErrorWithResponse, NotFoundError

from ..jwt.service import CrudAuthJwtService


class CrudAuthService:
    @staticmethod
    def verify(headers):
        authorization = headers.get(
            'Authorization', ''
        )
        token = re.sub('^Bearer ', '', authorization)
        try:
            response = CrudAuthJwtService.verify(
                body=dict(token=token)
            )
        except NotFoundError as e:
            raise e
        except ErrorWithResponse as e:
            response = e.response
        except Exception as e:
            raise e
        return response
