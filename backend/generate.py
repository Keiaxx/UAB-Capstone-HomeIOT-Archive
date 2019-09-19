# Contributor(s): Adrian Gose
# If you worked on this file, add your name above so we can keep track of contributions

# This file is meant to be called via CLI interface
# and is designed to aid in creating database tables and
# mock data. Do not import this generator into any modules.

# Misc Imports
import os
from datetime import datetime, timedelta

# Import SQL Models
from models.location import Location

# Import DAO Helpers
# If you don't know, DAO = Data Access Object
import dao.location as ldao
import dao.device as ddao
import dao.events as edao
import dao.usage as udao

# Import DB instance
from app import create_app
from extensions.database import db

app = create_app()
db.init_app(app)

if __name__ == "__main__":
    # Delete SQLITE DB
    # SQLITE ONLY FOR DEBUG/DEV PURPOSES. PRODUCTION MUST USE
    # UAB POSTGRES
    # TODO: Connect PostgreSQL
    basedir = os.path.abspath(os.path.dirname(__file__))
    if os.path.exists(os.path.join(basedir, "homeiot.db")):
        os.remove(os.path.join(basedir, "homeiot.db"))

    # Run this file directly to create the database tables.
    print("Initializing Database")

    # Create application context and perform database initialization queries within the context
    with app.app_context():
        db.create_all()
        print("Database initialized, generating data!")

        # Create locations/rooms
        # TODO: Add locations based on project specifications document
        garage = ldao.add_location('Garage')
        kitchen = ldao.add_location('Kitchen')

        # Add lights
        # TODO: Specify correct wattages and names/locations
        light = ddao.add_light(kitchen, "kitchen_light", 60)

        print(kitchen.devices)

        # Add HVAC System
        newhvac = ddao.add_hvac(garage, "Main HVAC", 3500)

        # Add generic electric device
        fridge = ddao.add_electric_device(kitchen, "fridge", 150)

        hvacs = ddao.get_hvac_systems()

        for hvac in hvacs:
            ddao.set_hvac_params(hvac, 30, 20, 10, 10)

        print(ddao.get_devices())

        edao.add_event(fridge, "ON", datetime.now())
        edao.add_event(fridge, "OFF", datetime.now())

        udao.add_usage(fridge, datetime.now(), "electric", 20)

        fromdate = datetime.now() - timedelta(hours=1)
        todate = datetime.now() + timedelta(hours=1)

        print(f'Getting usages {fromdate} > {todate}')
        print(udao.get_usages(fromdate, todate))

        print("Data generated!")
        print("You may now start the REST API Server!")

