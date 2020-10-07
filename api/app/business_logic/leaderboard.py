from models.teams import Team
from models.tasks import Task
from serializers.tasks import task_serializer
from models.competitions import Competition
import typing as tp


def generate_leaderboard() -> tp.List[dict]:
    teams = Team.objects.filter().order_by("-tasks_done", "+working_time")
    competition = Competition.objects.filter().first()
    leaderboard = []
    for place, team in enumerate(teams):
        team_tasks = Task.objects.filter(team_assigned=team)
        leaderboard_string = {
            "current_place": place + 1,
            "title": team.title,
            "tasks_info": [task_serializer(task) for task in team_tasks],
            "tasks_done": team.tasks_done,
            "fine_time": ((team.working_time - competition.date_start).seconds) // 60,
        }
        leaderboard.append(leaderboard_string)
    return leaderboard
