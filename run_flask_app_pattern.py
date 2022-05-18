# from flask import current_app as app
from flask import Flask
from flask_app_pattern.flask_app_pattern import HelloBlueprint


def create_app():
    app = Flask(__name__)

    hello_blueprint = HelloBlueprint()
    hello_blueprint.add_url_rule()

    app.register_blueprint(hello_blueprint.get_blueprint())

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
