from models.teams import TeamUser, Team
import bcrypt


def initiate_new_team_user(login: str, password: str) -> TeamUser:
    """Creates new user for fresh team."""

    hashpw = bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())
    user = TeamUser(login=login, hashpw=hashpw)
    user.save()
    return user


def initiate_new_team(title: str, user: TeamUser) -> Team:
    """Creates new team by its title and auth user."""
    team = Team(title=title, user=user)
    team.save()
    return team
