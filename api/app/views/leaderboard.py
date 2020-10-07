from flask_restful import Resource
from business_logic.leaderboard import generate_leaderboard


class LeaderboardHandler(Resource):
    def get(self):
        leaderboard = generate_leaderboard()
        return leaderboard
