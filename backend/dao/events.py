# Contributor(s): Adrian Gose
# If you worked on this file, add your name above so we can keep track of contributions

from typing import List

from models.device import Device
from models.eventlog import EventLog
from extensions.database import commit


def add_event(device: Device, state: str, date) -> EventLog:
    """

    :param device:
    :param state:
    :param date:
    :return:
    """
    event = EventLog(device, state, date, 0)
    commit(event)
    return event

def add_int_temperature_log(device: Device, temperature: int, date) -> EventLog:
    """

    :param device:
    :param state:
    :param date:
    :return:
    """
    event = EventLog(device, "INTTEMP", date, temperature)
    commit(event)
    return event

def add_out_temperature_log(device: Device, temperature: int, date) -> EventLog:
    """

    :param device:
    :param state:
    :param date:
    :return:
    """
    event = EventLog(device, "EXTTEMP", date, temperature)
    commit(event)
    return event

def add_hvac_event(device: Device, state: str, temperature: int, date) -> EventLog:
    """

    :param device:
    :param state:
    :param date:
    :return:
    """
    event = EventLog(device, state, date, temperature)
    commit(event)
    return event

def get_events() -> List[EventLog]:
    """

    :return:
    """
    return EventLog.query.all()