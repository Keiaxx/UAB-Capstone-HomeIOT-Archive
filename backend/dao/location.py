# Contributor(s): Adrian Gose
# If you worked on this file, add your name above so we can keep track of contributions

from models.location import Location
from extensions.database import db


def add_location(name):
    newloc = Location(name)
    db.session.add(newloc)
    db.session.commit()
    return newloc


def get_locations():
    return Location.query.all()