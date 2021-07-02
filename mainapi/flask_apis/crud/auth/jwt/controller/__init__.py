from flask import Blueprint, request, make_response
from flask.json import loads
from simple_rest_client.exceptions import ErrorWithResponse

from ..service import CrudAuthJwtService


crud_auth_jwt_blueprint = Blueprint("crud_auth_jwt", __name__)


@crud_auth_jwt_blueprint.route("/crud/auth/jwt/<action>", methods=["POST"])
def index(action):
    body = loads(request.data)
    try:
        if action == 'create':
            response = CrudAuthJwtService.create(
                body=body
            )
        elif action == 'refresh':
            response = CrudAuthJwtService.refresh(
                body=body
            )
        else:
            response = CrudAuthJwtService.verify(
                body=body
            )
    except ErrorWithResponse as e:
        response = e.response
    resp = make_response(response.body, response.status_code)
    return resp
