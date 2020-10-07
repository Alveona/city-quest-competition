from flask import Flask
from flask_restful import Api
import mongoengine
from views.teams import TeamsHandler
from views.tasks import TasksHandler
from views.competitions import CompetitionsHandler
from views.auth import AuthHandler
from views.answers import AnswersHandler
from views.leaderboard import LeaderboardHandler
from flask_apps.jwt import jwt


def register_routes(api: Api) -> None:
    api.add_resource(TeamsHandler, "/teams")
    api.add_resource(TasksHandler, "/tasks")
    api.add_resource(CompetitionsHandler, "/competitions")
    api.add_resource(AuthHandler, "/auth")
    api.add_resource(AnswersHandler, "/answer")
    api.add_resource(LeaderboardHandler, "/leaderboard")


def create_app() -> Flask:
    _app = Flask(__name__)
    _app.config["JWT_SECRET_KEY"] = "supersecret"

    api = Api(_app)
    jwt.init_app(_app)

    mongoengine.connect(
        db="hightechcross",
        host="mongodb",
        port=27017,
        authentication_source="admin",
    )

    register_routes(api)

    return _app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)