from simple_rest_client.exceptions import ErrorWithResponse

from .service import SpacyService
from ...crud.auth.service import CrudAuthService


class SpacyResource:
    async def on_post(self, req, resp, *, action):
        body = await req.media()
        if action == 'entities_by_type':
            response = await SpacyService.entities_by_type(
                body=body,
                headers=req.headers
            )
        else:
            response = await SpacyService.entities(
                body=body,
                headers=req.headers
            )
        resp.media = response.body
        resp.status_code = response.status_code
