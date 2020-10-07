from flask_restful import Resource, reqparse
from business_logic.teams import initiate_new_team, initiate_new_team_user
import json

class TeamsHandler(Resource):
    parser_post = reqparse.RequestParser()
    parser_post.add_argument("login", type=str, required = True)
    parser_post.add_argument("password", type=str, required = True)
    parser_post.add_argument("title", type=str, required = True)

    def post(self):
        data = self.parser_post.parse_args()
        user = initiate_new_team_user(login = data["login"], password=data["password"])
        team = initiate_new_team(title = data["title"], user = user)
        return json.loads(team.to_json())



