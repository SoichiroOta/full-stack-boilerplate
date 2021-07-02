from ...utils import handle_request_error_with_response
from ...crud.auth import authenticate
from .api_client import SpacyApi


class SpacyService:
    @staticmethod
    @authenticate
    @handle_request_error_with_response
    def entities(body, headers):
        api = SpacyApi()
        return api.entities.create(
            body=body
        )

    @staticmethod
    @authenticate
    @handle_request_error_with_response
    def entities_by_type(body, headers):
        crud_api = SpacyApi()
        return crud_api.entities_by_type.create(
            body=body
        )
