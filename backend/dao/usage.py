from models.usage import Usage
from models.device import Device
from extensions.database import commit


def add_usage(device: Device, date, type: str, data: int):
    assert data > 0

    usageData = Usage(device, date, type, data)
    commit(usageData)
    return usageData


def get_usages(startdate, enddate):
    return Usage.query.filter(Usage.date.between(startdate, enddate)).all()
