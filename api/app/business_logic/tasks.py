from models.tasks import Task, Attempt
from models.teams import Team
import typing as tp
import utils.constants as constants


def initiate_new_task(
    title: str,
    coords: tp.Tuple[float, float],
    description: str,
    correct_answer: str,
    hints: tp.List[str],
) -> Task:
    """Creates new task."""

    task = Task(
        title=title,
        coords=coords,
        description=description,
        correct_answer=correct_answer,
        hints=hints,
    )

    task.save()
    return task


def get_tasks(team: Team) -> tp.List[Task]:
    """Get only team's tasks."""
    return Task.objects.filter(team_assigned=team)


def get_task_status(task: Task) -> str:
    attempts = Attempt.objects.filter(task=task)
    if not attempts:
        return constants.NOT_STARTED_STATUS
    correct_attempt = Attempt.objects.filter(task=task, is_correct=True)
    if correct_attempt:
        return constants.DONE_STATUS
    return constants.IN_PROGRESS_STATUS