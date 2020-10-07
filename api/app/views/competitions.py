from flask_restful import Resource
from business_logic.competitions import initiate_new_competition
from utils.exceptions import NotEnoughTasksException
import json


class CompetitionsHandler(Resource):
    def post(self):
        try:
            competition = initiate_new_competition()
        except NotEnoughTasksException as e:
            return {"error": str(e)}, 400
        return json.loads(competition.to_json())
