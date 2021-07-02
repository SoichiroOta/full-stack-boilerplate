from simple_rest_client.exceptions import ErrorWithResponse

from .api_client import SpacyApi
from ...utils import handle_async_request_error_with_response
from ...crud.auth import authenticate_async


class SpacyService:
    @staticmethod
    @authenticate_async
    @handle_async_request_error_with_response
    async def entities(body, headers):
        api = SpacyApi()
        return await api.entities.create(
            body=body
        )

    @staticmethod
    @authenticate_async
    @handle_async_request_error_with_response
    async def entities_by_type(body, headers):
        crud_api = SpacyApi()
        return await crud_api.entities_by_type.create(
            body=body
        )
