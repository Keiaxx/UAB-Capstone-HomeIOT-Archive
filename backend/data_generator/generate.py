# Contributor(s): Adrian Gose
# If you worked on this file, add your name above so we can keep track of contributions

# This file is meant to be called via CLI interface
# and is designed to aid in creating database tables and
# mock data. Do not import this generator into any modules.

# Misc Imports
import os

# Import SQL Models
from models.location import Location

# Import DAO Helpers
# If you don't know, DAO = Data Access Object
import dao.location as ldao

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
    if os.path.exists(os.path.join(basedir, "../homeiot.db")):
        os.remove(os.path.join(basedir, "../homeiot.db"))

    # Run this file directly to create the database tables.
    print("Initializing Database")

    # Create application context and perform database initialization queries within the context
    with app.app_context():
        db.create_all()
        print("Database initialized, generating data!")

        # Create locations/rooms
        # TODO: Add locations based on project specifications document
        print(ldao.add_location('Garage'))
        print(ldao.add_location('Bedroom 1'))
        print(ldao.add_location('Bedroom 2'))
        print(ldao.add_location('Kitchen'))

        print("Data generated!")
        print("You may now start the REST API Server!")

