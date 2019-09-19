# Contributor(s): Adrian Gose
# If you worked on this file, add your name above so we can keep track of contributions

from models.device import *
from models.location import *
from extensions.database import commit


###############
# Lights
###############
def add_light(name: str, wattage: int, location: Location):
    newlight = Light(name, wattage, location)
    commit(newlight)
    return newlight


def get_lights():
    return Light.query.all()


###############
# Doors
###############
def add_door(location: Location, name: str):
    newlight = Door(location, name)
    commit(newlight)
    return newlight


def get_doors():
    return Door.query.all()


###############
# Windows
###############
def add_window(location: Location, name: str):
    newlight = Window(location, name)
    commit(newlight)
    return newlight


def get_windows():
    return Window.query.all()


###############
# Water
###############
def add_water_meter(location: Location, name: str):
    newlight = Water(location, name)
    commit(newlight)
    return newlight


def get_water_meters():
    return Water.query.all()


###############
# Generic Electric Device
###############
def add_electric_device(location: Location, name: str, wattage: int):
    newelec = Electric(location, name, wattage)
    commit(newelec)
    return newelec


def get_electric_devices():
    return Electric.query.all()


###############
# HVAC
###############
def add_hvac(location: Location, name: str, wattage: int):
    newhvac = HVAC(location, name, wattage)
    commit(newhvac)
    return newhvac


def set_hvac_params(hvacsystem: HVAC, high_f: int, low_f: int, int_f: int, ext_f: int):
    # Ensure high temp is not less than low temp
    assert high_f > low_f

    hvacsystem.int_f = int_f
    hvacsystem.ext_f = ext_f
    hvacsystem.high_f = high_f
    hvacsystem.low_f = low_f

    commit(hvacsystem)


def get_hvac_systems():
    return HVAC.query.all()


###############
# Generic Device Queries
###############
def get_devices():
    return Device.query.all()


def get_device_by_name(name: str):
    return Device.query.filter(Light.name.ilike(name)).first()


def get_device_by_id(did: int):
    return Device.query.filter(Device.deviceId == did).first()

