from typing import List

from models.usage import Usage
from models.device import Device
from extensions.database import commit


def add_usage(device: Device, date, type: str, data: int) -> Usage:
    """

    :param device:
    :param date:
    :param type:
    :param data:
    :return:
    """
    assert data > 0

    usageData = Usage(device, date, type, data)
    
    commit(usageData)
    return usageData


def get_usages(startdate, enddate) -> List[Usage]:
    """

    :param startdate:
    :param enddate:
    :return:
    """
    return Usage.query.filter(Usage.date.between(startdate, enddate)).all()
