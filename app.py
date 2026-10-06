from flask import Flask

from controllers.health import health_bp
from controllers.notes import notes_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(health_bp)
    app.register_blueprint(notes_bp)
    return app


if __name__ == "__main__":
    create_app().run(port=5000)
