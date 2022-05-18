from flask import Blueprint, make_response, jsonify, Response
from flask.views import MethodView


class HelloEndpoint(MethodView):
    def get(self) -> Response:
        return make_response(jsonify({'message': "Hello World!"}), 200)


class HelloBlueprint:
    def __init__(self):
        self._view = Blueprint('hello_view', __name__)

    def add_url_rule(self):
        self._view.add_url_rule(
            '/api/hello',
            view_func=HelloEndpoint.as_view('hello_endpoint')
        )

    def get_blueprint(self) -> Blueprint:
        return self._view
