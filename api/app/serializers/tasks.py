from models.tasks import Task
from business_logic.tasks import get_task_status
import json


def task_serializer(task: Task, admin=False) -> dict:
    data = {
        "id": str(task.id),
        "title": task.title,
        "description": task.description,
        "coords": task.coords,
        "status": get_task_status(
            task
        ),  # i hate static calculations, let's do it on air
    }
    if admin:
        data["team_assigned"] = (
            json.loads(task.team_assigned.to_json()) if task.team_assigned else None
        )
    return json.loads(json.dumps(data))