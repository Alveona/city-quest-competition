import mongoengine as me
import mongoengine_goodjson as gj
import datetime as dt


class Task(gj.Document):
    title = me.StringField(max_length=255)
    coords = me.GeoPointField(exclude_to_json=True)
    description = me.StringField(max_length=300)
    correct_answer = me.StringField(exclude_to_json=True)
    team_assigned = me.ReferenceField("Team", default=None, exclude_to_json=True)
    hints = me.ListField(me.StringField(max_length=255), exclude_to_json=True)
    hints_issued = me.IntField(default=0)


class Attempt(gj.Document):
    attempt_time = me.DateTimeField(default=dt.datetime.utcnow)
    team = me.ReferenceField("Team", exclude_to_json=True)
    task = me.ReferenceField("Task")
    answer = me.StringField()
    is_correct = me.BooleanField(default=False)