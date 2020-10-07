from utils.utils import calculate_competition_end_date
import mongoengine as me
import mongoengine_goodjson as gj
import datetime as dt


class Competition(gj.Document):
    date_start = me.DateTimeField(default=dt.datetime.utcnow)
    date_end = me.DateTimeField(default=calculate_competition_end_date)
