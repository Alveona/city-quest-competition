import mongoengine as me
import mongoengine_goodjson as gj


class TeamUser(gj.Document):
    login = me.StringField(max_length=255)
    hashpw = me.StringField(max_length=255)


class Team(gj.Document):
    title = me.StringField(max_length=255)
    user = me.ReferenceField(
        "TeamUser", reverse_delete_rule=me.CASCADE, exclude_to_json=True
    )
    tasks_done = me.IntField(default=0)
    working_time = me.DateTimeField(default=None)