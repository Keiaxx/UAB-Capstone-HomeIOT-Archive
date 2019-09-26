# Contributor(s): Adrian Gose, Senay Patel
# If you worked on this file, add your name above so we can keep track of contributions

# This file is meant to be called via CLI interface
# and is designed to aid in creating database tables and
# mock data. Do not import this generator into any modules.

# Misc Imports
import os
from datetime import datetime, timedelta
import random
import calendar

# Import SQL Models
from models.location import Location
from models.device import Device
from models.eventlog import EventLog
from models.usage import Usage


# Import DAO Helpers
# If you don't know, DAO = Data Access Object
import dao.location as ldao
import dao.device as ddao
import dao.events as edao
import dao.usage as udao
from dao.calculate import *

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
        # garage = ldao.add_location('Garage')
        # kitchen = ldao.add_location('Kitchen')

        # # Add lights
        # # TODO: Specify correct wattages and names/locations
        # light = ddao.add_light(kitchen, "kitchen_light", 60)

        # print(kitchen.devices)

        # # Add HVAC System
        # newhvac = ddao.add_hvac(garage, "Main HVAC", 3500)

        # # Add generic electric device
        # fridge = ddao.add_electric_device(kitchen, "fridge", 150)

        # hvacs = ddao.get_hvac_systems()

        # for hvac in hvacs:
        #     ddao.set_hvac_params(hvac, 30, 20, 10, 10)

        # print(ddao.get_devices())

        # edao.add_event(fridge, "ON", datetime.now())
        # edao.add_event(fridge, "OFF", datetime.now())

        # udao.add_usage(fridge, datetime.now(), "electric", 20)

        # fromdate = datetime.now() - timedelta(hours=1)
        # todate = datetime.now() + timedelta(hours=1)

        # print(f'Getting usages {fromdate} > {todate}')
        # print(udao.get_usages(fromdate, todate))

        # print("Data generated!")
        # print("You may now start the REST API Server!")

        
        kitchen= ldao.add_location('Kitchen')
        kitchen_light = ddao.add_light(kitchen, "kitchen_light", 60)
        microwave = ddao.add_electric_device(kitchen, "microwave", 1100)
        refrigerator = ddao.add_electric_device(kitchen, "refrigerator", 150)
        stove = ddao.add_electric_device(kitchen, "stove", 3000)
        oven = ddao.add_electric_device(kitchen, "oven", 4000)
        dishwasher = ddao.add_electric_device(kitchen,"dishwasher", 1800)
       

        """

        kitchenlight usage comuptation

        """ 
        def kitchen_light_usage(given_date: datetime):
            dates = given_date
            days = calendar.day_name[dates.weekday()]
            if days == "Monday" or days == "Tuesday" or days == "Wednesday" or days == "Thursday" or days == "Friday":
                d = random.randint(5, 7)
                start_time = given_date + timedelta(hours = d)
                on_minutes = random.randint(30, 60)
                end_time = start_time + timedelta(minutes = on_minutes) 
                edao.add_event(kitchen_light, "ON", start_time)
                edao.add_event(kitchen_light, "OFF", end_time)
                n = random.randint(18, 22)
                start_time2 = given_date + timedelta(hours = n)
                on_minutes2 = random.randint(60, 180)
                end_time2 = start_time2 + timedelta(minutes = on_minutes2) 
                edao.add_event(kitchen_light, "ON", start_time2)
                edao.add_event(kitchen_light, "OFF", end_time2) 
                usage_minutes = on_minutes + on_minutes2 
                usage = general_eq(60, timedelta(minutes =usage_minutes))
                udao.add_usage(kitchen_light, dates, "electric", usage)
            else:
                r = random.randint(4, 5)
                usage_time = 0
                for x in range(r):
                    s = random.randint(7, 22)
                    start_time = given_date + timedelta(hours = s)
                    on_minutes = random.randint(15 , 180)
                    end_time = start_time + timedelta(minutes =on_minutes)
                    edao.add_event(kitchen_light, "ON", start_time)
                    edao.add_event(kitchen_light, "OFF", end_time)
                    usage_time =+ on_minutes
                usage = general_eq(60, timedelta(minutes =usage_time))
                udao.add_usage(kitchen_light, dates, "electric", usage)


        """

        Refrigerator usage comuptation

        """  
        def refrigerator_usage(given_date:  datetime):
            dates = given_date
            edao.add_event(refrigerator, "ON", dates)
            usage = general_eq(150 , timedelta(hours = 24))
            udao.add_usage(refrigerator, dates, "electric", usage)


        """

        Dishwasher usage comuptation

        """  
        def dishwasher_usage(given_date: datetime):
            dates = given_date
            days = calendar.day_name[dates.weekday()]
            if days == "Monday" or days == "Wednesday" or days == "Thursday" or days == "Friday":
                r = random.randint(18, 22)
                start_time = given_date + timedelta(hours = r)
                end_time = start_time + timedelta(minutes = 45)
                edao.add_event(dishwasher, "ON", start_time)
                edao.add_event(dishwasher, "OFF", end_time)
                usage = general_eq(1800 ,timedelta(minutes = 45))
                udao.add_usage(dishwasher, dates, "electric", usage)



        """

        Stove usage comuptation

        """        
        def Stove_usage(given_date: datetime):
            dates = given_date
            days = calendar.day_name[dates.weekday()]
            if days == "Monday" or days == "Tuesday" or days == "Wednesday" or days == "Thursday" or days == "Friday":
                r = random.randint(18, 22)
                start_time = given_date + timedelta(hours = r)
                end_time = start_time + timedelta(minutes = 15)
                edao.add_event(stove, "ON", start_time)
                edao.add_event(stove, "OFF", end_time )
                usage = general_eq(3500 ,timedelta(minutes = 15))
                udao.add_usage(stove, dates, "electric", usage)
            else: 
                r = random.randint(7, 22)
                start_time = given_date + timedelta(hours = r)
                end_time = start_time + timedelta(minutes = 15)
                edao.add_event(stove, "ON", start_time)
                edao.add_event(stove, "OFF", end_time)
                usage = general_eq(3500 ,timedelta(minutes = 30))
                udao.add_usage(stove, dates, "electric", usage)

        """

        Oven usage comuptation

        """  
        def oven_usage(given_date: datetime):
            dates = given_date
            days = calendar.day_name[dates.weekday()]
            if days == "Monday" or days == "Tuesday" or days == "Wednesday" or days == "Thursday" or days == "Friday":
                r = random.randint(18, 22)
                start_time = given_date + timedelta(hours = r)
                end_time = start_time + timedelta(minutes = 45)
                edao.add_event(oven, "ON", start_time)
                edao.add_event(oven, "OFF", end_time )
                usage = general_eq(4000 ,timedelta(minutes = 45))
                udao.add_usage(oven, dates, "electric", usage)
            else: 
                r = random.randint(18, 22)
                start_time = given_date + timedelta(hours = r)
                end_time = start_time + timedelta(minutes = 60)
                edao.add_event(stove, "ON", start_time)
                edao.add_event(stove, "OFF", end_time)
                usage = general_eq(4000 ,timedelta(minutes = 60))
                udao.add_usage(oven, dates, "electric", usage)

        
        """

        Microwave usage comuptation

        """          
        def microwave_usage(given_date: datetime):
            dates = given_date
            days = calendar.day_name[dates.weekday()]
            if days == "Monday" or days == "Tuesday" or days == "Wednesday" or days == "Thursday" or days == "Friday":
                r = random.randint(18, 22)
                start_time = given_date + timedelta(hours = r)
                end_time = start_time + timedelta(minutes = 20)
                edao.add_event(microwave, "ON", start_time)
                edao.add_event(microwave, "OFF", end_time )
                usage = general_eq(1100,timedelta(minutes = 20))
                udao.add_usage(microwave, dates, "electric", usage)
            else: 
                r = random.randint(18, 22)
                start_time = given_date + timedelta(hours = r)
                end_time = start_time + timedelta(minutes = 30)
                edao.add_event(microwave, "ON", start_time)
                edao.add_event(microwave, "OFF", end_time)
                usage =  general_eq(1100,timedelta(minutes = 30))
                udao.add_usage(microwave, dates, "electric", usage)

        
        """

        Overall kicthen usage comuptation

        """     
        def generate_kitchen_usage(start_date: datetime, end_date: datetime):                
            days_date = end_date-start_date
            first_date = start_date
            for x in range(days_date.days):
                dishwasher_usage(first_date)
                Stove_usage(first_date)
                oven_usage(first_date)
                microwave_usage(first_date)
                refrigerator_usage(first_date)
                kitchen_light_usage(first_date)
                first_date += timedelta(days=1)

        """
        Test Case
        """
        generate_kitchen_usage(datetime(19, 9, 18), datetime(19,9, 25))  



        # TODO: Garage historical data generation.
        garage = ldao.add_location('Garage')   




        #TODO: Living room historical data generation
        living_room = ldao.add_location('Living room')




        #TODO: Bedroom1 historical data generation
        Bedroom1 = ldao.add_location('Bedroom1')



        #TODO: Bedroom1 historical data generation
        Bedroom2 = ldao.add_location('Bedroom2')