from flask_restful import Resource, reqparse
from business_logic.answers import answer_on_task
from flask_jwt_extended import get_jwt_identity, jwt_required
from utils.utils import team_by_token_identity
from utils.exceptions import CompetitionIsOver, CompetitionHasntStarted
import json


class AnswersHandler(Resource):
    parser_post = reqparse.RequestParser()
    parser_post.add_argument("answer", type=str, required=True)
    parser_post.add_argument("current_lat", type=float, required=True)
    parser_post.add_argument("current_lon", type=float, required=True)

    @jwt_required
    def post(self):
        data = self.parser_post.parse_args()
        team = team_by_token_identity(get_jwt_identity())
        try:
            attempt = answer_on_task(
                team=team,
                coords=(data["current_lat"], data["current_lon"]),
                answer=data["answer"],
            )
        except CompetitionIsOver as e:
            return {"error": str(e)}, 400
        except CompetitionHasntStarted as e:
            return {"error": str(e)}, 400
        return json.loads(attempt.to_json())
