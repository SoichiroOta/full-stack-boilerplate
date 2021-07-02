from .....utils import handle_request_error_with_response
from ....api_client import CrudApi


class CrudAuthJwtService:
    @staticmethod
    @handle_request_error_with_response
    def create(body):
        crud_api = CrudApi()
        return crud_api.auth.jwt_create(
            body=body
        )

    @staticmethod
    @handle_request_error_with_response
    def refresh(body):
        crud_api = CrudApi()
        return crud_api.auth.jwt_refresh(
            body=body
        )

    @staticmethod
    @handle_request_error_with_response
    def verify(body):
        crud_api = CrudApi()
        return crud_api.auth.jwt_verify(
            body=body
        )
