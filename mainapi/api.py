import responder
from flask import Flask

from responder_apis.main.health_check.controller import MainHealthCheckResource
from responder_apis.crud.auth.jwt.controller import CrudAuthJwtResource
from responder_apis.microservices.spacy.controller import SpacyResource
from flask_apis.main.health_check.controller import main_health_check_blueprint
from flask_apis.crud.auth.jwt.controller import crud_auth_jwt_blueprint
from flask_apis.microservices.spacy.controller import spacy_blueprint


api = responder.API(
    cors=True,
    allowed_hosts=["*"],
    cors_params={
        "allow_origins": "*",
        "allow_methods": "*",
        "allow_headers": "*"
    }
)
flask = Flask(__name__)

api.add_route(
    '/api/responder/',
    MainHealthCheckResource
)
api.add_route(
    '/api/responder/crud/auth/jwt/{action}',
    CrudAuthJwtResource
)
api.add_route(
    '/api/responder/spacy/{action}',
    SpacyResource
)
flask.register_blueprint(main_health_check_blueprint)
flask.register_blueprint(crud_auth_jwt_blueprint)
flask.register_blueprint(spacy_blueprint)

api.mount('/api/flask', flask)


if __name__ == '__main__':
    api.run()
