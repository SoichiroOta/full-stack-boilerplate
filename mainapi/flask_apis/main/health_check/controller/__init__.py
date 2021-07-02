from flask import Blueprint, jsonify


main_health_check_blueprint = Blueprint("main_health_check", __name__)


@main_health_check_blueprint.route("/", methods=["GET"])
def index():
    return jsonify(
        status=True
    )
