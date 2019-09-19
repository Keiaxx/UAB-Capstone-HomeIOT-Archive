# Contributor(s): Adrian Gose
# If you worked on this file, add your name above so we can keep track of contributions

from models.device import Device
from models.eventlog import EventLog
from extensions.database import commit


def add_event(device: Device, state: str, date):
    event = EventLog(device, state, date)
    commit(event)
    return event


def get_events():
    return EventLog.query.all()