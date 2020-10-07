from models.competitions import Competition
from models.teams import Team
from models.tasks import Attempt, Task
from utils.exceptions import NotEnoughTasksException
import datetime as dt
import typing as tp
import random


def initiate_new_competition() -> Competition:
    competitions = Competition.objects.filter()
    for competition in competitions:
        competition.delete()  # only one in time
    for attempt in Attempt.objects.filter():
        attempt.delete()

    tasks = Task.objects.filter()
    teams = Team.objects.filter()

    if len(teams) * 6 > len(tasks):
        raise NotEnoughTasksException(
            "You have too little amount of tasks, should be at least (teams * 6)"
        )
    for task in tasks:
        task.team_assigned = random.choice(teams)
        task.save()

    competition = Competition()
    competition.save()
    now = dt.datetime.utcnow()
    for team in teams:
        team.working_time = now
        team.save()
    return competition


def get_competitions() -> tp.List[Competition]:
    return Competition.objects.filter()