from models.tasks import Task, Attempt
from models.teams import Team
from models.competitions import Competition
from utils.exceptions import CompetitionIsOver, CompetitionHasntStarted
import typing as tp
import datetime as dt


def answer_on_task(team: Team, coords: tp.Tuple[float, float], answer: str) -> Attempt:
    competition = Competition.objects.filter().first()
    if not competition:
        raise CompetitionHasntStarted("Competition hasn't started yet :c")
    if dt.datetime.utcnow() > competition.date_end:
        raise CompetitionIsOver("Competition time is over!")
    task = Task.objects.filter(coords__near=coords).first()
    attempt = Attempt(task=task, team=team, answer=answer)
    if answer == task.correct_answer:
        attempt.is_correct = True
        team.tasks_done += 1
    else:
        team.working_time += dt.timedelta(minutes=30)
    team.save()
    attempt.save()
    return attempt