# Contributor(s): Adrian Gose
# If you worked on this file, add your name above so we can keep track of contributions

from models.location import Location
from extensions.database import db, commit


def add_location(name):
    newloc = Location(name)
    commit(newloc)
    return newloc


def get_locations():
    return Location.query.all()