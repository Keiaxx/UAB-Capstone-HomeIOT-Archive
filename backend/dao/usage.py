from typing import List


from models.usage import Usage
from models.device import Device
from extensions.database import commit

from sqlalchemy import func


def add_usage(device: Device, date, type: str, data: int) -> Usage:
    """

    :param device: deviceId
    :param date: DATETIME
    :param type: water/electric
    :param data: gallons/kWh
    :return:
    """
    assert data > 0

    usageData = Usage(device, date, type, data)
    
    commit(usageData)
    return usageData


def get_usages(startdate: str, enddate: str, type: str, ascending: bool) -> List[Usage]:
    """
    :param startdate: Start date in ISO format
    :param enddate: End date in ISO format
    :param type: water/electric
    :param ascending: sorting type
    :return:
    """
    if startdate and enddate:
        return Usage.query \
            .filter(Usage.date.between(startdate, enddate)) \
            .filter(Usage.type == type) \
            .order_by(Usage.date.asc()) \
            .all()
    else:
        return Usage.query \
            .filter(Usage.type == type) \
            .order_by(Usage.date.asc()) \
            .all()

def get_device_total_usage(deviceid: int, startdate: str, enddate: str) -> int:
    if startdate and enddate:
        return Usage.query.with_entities(func.sum(Usage.data) \
            .label("usage_total")) \
            .filter(Usage.date.between(startdate, enddate)) \
            .filter(Usage.deviceId == deviceid) \
            .first()[0]
    else:
        return Usage.query.with_entities(func.sum(Usage.data) \
            .label("usage_total")) \
            .filter(Usage.deviceId == deviceid) \
            .first()[0]



