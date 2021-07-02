from flask import Blueprint, request, make_response
from flask.json import loads
from simple_rest_client.exceptions import ErrorWithResponse

from .service import SpacyService


spacy_blueprint = Blueprint("spacy", __name__)


@spacy_blueprint.route("/spacy/<action>", methods=["POST"])
def index(action):
    body = loads(request.data)
    try:
        if action == 'entities_by_type':
            response = SpacyService.entities_by_type(
                body=body,
                headers=request.headers
            )
        else:
            response = SpacyService.entities(
                body=body,
                headers=request.headers
            )
    except ErrorWithResponse as e:
        response = e.response
    resp = make_response(response.body, response.status_code)
    return resp
