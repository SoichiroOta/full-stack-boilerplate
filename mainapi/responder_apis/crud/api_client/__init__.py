import os

from simple_rest_client.api import API

from .auth import CrudAuthResource


DEFAULT_HEADERS = {
    'Content-Type': 'application/json'
}


class CrudApi:

    def __init__(self):
        self._api = API(
            api_root_url=os.getenv('CRUDAPI_URL'),  # base api url
            params={},  # default params
            headers=DEFAULT_HEADERS,  # default headers
            timeout=2,  # default timeout in seconds
            append_slash=False,  # append slash to final url
            json_encode_body=True,  # encode body as json
        )
        self._api.add_resource(
            resource_name='auth',
            resource_class=CrudAuthResource
        )

    @property
    def auth(self):
        return self._api.auth
