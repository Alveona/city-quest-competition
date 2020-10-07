from flask_restful import Resource, reqparse
from business_logic.tasks import initiate_new_task, get_tasks
from flask_jwt_extended import jwt_required, get_jwt_identity
from serializers.tasks import task_serializer
import json
from utils.utils import team_by_token_identity


class TasksHandler(Resource):
    parser_post = reqparse.RequestParser()
    parser_post.add_argument("title", type=str, required=True)
    parser_post.add_argument("description", type=str, required=True)
    parser_post.add_argument("lat", type=float, required=True)
    parser_post.add_argument("lon", type=float, required=True)
    parser_post.add_argument("correct_answer", type=str, required=True)
    parser_post.add_argument("hints", type=str, action="append")

    def post(self):
        data = self.parser_post.parse_args()
        task = initiate_new_task(
            title=data["title"],
            coords=(data["lat"], data["lon"]),
            description=data["description"],
            correct_answer=data["correct_answer"],
            hints=data["hints"],
        )
        return json.loads(task.to_json())

    @jwt_required
    def get(self):
        team = team_by_token_identity(get_jwt_identity())
        tasks = get_tasks(team)
        return [task_serializer(task) for task in tasks]
