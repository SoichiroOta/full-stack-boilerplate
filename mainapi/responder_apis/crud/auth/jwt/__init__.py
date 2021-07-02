from ...api_client import CrudApi


class CrudAuthJwtService:
    @staticmethod
    async def create(body):
        crud_api = CrudApi()
        return await crud_api.auth.jwt_create(
            body=body
        )

    @staticmethod
    async def refresh(body):
        crud_api = CrudApi()
        return await crud_api.auth.jwt_refresh(
            body=body
        )

    @staticmethod
    async def verify(body):
        crud_api = CrudApi()
        return await crud_api.auth.jwt_verify(
            body=body
        )
