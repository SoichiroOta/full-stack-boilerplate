from simple_rest_client.exceptions import ErrorWithResponse

from ..service import CrudAuthJwtService


class CrudAuthJwtResource:
    async def on_post(self, req, resp, *, action):
        body = await req.media()
        try:
            if action == 'create':
                response = await CrudAuthJwtService.create(
                    body=body
                )
            elif action == 'refresh':
                response = await CrudAuthJwtService.refresh(
                    body=body
                )
            else:
                response = await CrudAuthJwtService.verify(
                    body=body
                )
        except ErrorWithResponse as e:
            response = e.response
        resp.media = response.body
        resp.status_code = response.status_code
