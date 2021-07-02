from .....utils import handle_async_request_error_with_response
from ....api_client import CrudApi


class CrudAuthJwtService:
    @staticmethod
    @handle_async_request_error_with_response
    async def create(body):
        crud_api = CrudApi()
        return await crud_api.auth.jwt_create(
            body=body
        )

    @staticmethod
    @handle_async_request_error_with_response
    async def refresh(body):
        crud_api = CrudApi()
        return await crud_api.auth.jwt_refresh(
            body=body
        )

    @staticmethod
    @handle_async_request_error_with_response
    async def verify(body):
        crud_api = CrudApi()
        return await crud_api.auth.jwt_verify(
            body=body
        )
