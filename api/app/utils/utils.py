import datetime as dt
from models.teams import Team, TeamUser


def calculate_competition_end_date() -> dt.datetime:
    return dt.datetime.utcnow() + dt.timedelta(hours=5)


def team_by_token_identity(identity: str) -> Team:
    """Gets team by provided user_id
    Usually uses with get_jwt_identity()"""

    try:
        user = TeamUser.objects.filter(id=identity).first()
        if user:
            team = Team.objects.filter(user=user).first()
            if team:
                return team
            else:
                return None
        else:
            return None
    except:
        return None
