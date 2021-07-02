import os

from simple_rest_client.api import API
from simple_rest_client.resource import AsyncResource


DEFAULT_HEADERS = {
    'Content-Type': 'application/json'
}


class SpacyApi:

    def __init__(self):
        api = API(
            api_root_url=os.getenv('SPACYAPI_URL'),  # base api url
            params={},  # default params
            headers=DEFAULT_HEADERS,  # default headers
            timeout=2,  # default timeout in seconds
            append_slash=False,  # append slash to final url
            json_encode_body=True,  # encode body as json
        )
        api.add_resource(
            resource_name='entities',
            resource_class=AsyncResource
        )
        api.add_resource(
            resource_name='entities_by_type',
            resource_class=AsyncResource
        )
        self._api = api

    @property
    def entities(self):
        return self._api.entities

    @property
    def entities_by_type(self):
        return self._api.entities_by_type
