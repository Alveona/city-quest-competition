from flask_restful import Resource, reqparse
from business_logic.auth import auth


class AuthHandler(Resource):
    parser_post = reqparse.RequestParser()
    parser_post.add_argument("login", type=str, required=True)
    parser_post.add_argument("password", type=str, required=True)

    def post(self):
        data = self.parser_post.parse_args()
        auth_response = auth(login=data["login"], password=data["password"])
        if not auth_response:
            return {"message": "Wrong creds"}, 403
        return {
            "access_token": auth_response[0],
            "refresh_token": auth_response[1],
        }, 200
