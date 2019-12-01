# Contributor(s): Adrian Gose, Senay Patel
# If you worked on this file, add your name above so we can keep track of contributions

# This file is meant to be called via CLI interface
# and is designed to aid in creating database tables and
# mock data. Do not import this generator into any modules.

# Misc Imports
import os
from datetime import datetime, timedelta
from datetime import date as dt
import random
import calendar

# Import SQL Models
from models.location import Location
from models.device import Device
from models.eventlog import EventLog
from models.usage import Usage
from data_generator.weather_data import *

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

# PostgreSQL config
import yaml
pgconfig = None
with open("./pgconfig.yml", 'r') as stream: 
    try:
        pgconfig = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        exit(1)

app = create_app(pgconfig)
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
    print("Connecting to Database")

    # Create application context and perform database initialization queries within the context
    with app.app_context():
        print("DB Connected. Generating tables...")
        db.create_all()
        print("Tables generated, generating data!")


        
        kitchen= ldao.add_location('Kitchen')
        kitchen_light = ddao.add_light(kitchen, 0, 0, "kitchen_light", 60)
        microwave = ddao.add_electric_device(kitchen, 0, 0, "microwave", 1100)
        refrigerator = ddao.add_electric_device(kitchen, 920, 415, "refrigerator", 150)
        stove = ddao.add_electric_device(kitchen, 0, 0, "stove", 3000)
        oven = ddao.add_electric_device(kitchen, 935, 335, "oven", 4000)
        dishwasher = ddao.add_electric_device(kitchen, 0, 0, "dishwasher", 1800)
        kitchen_door = ddao.add_door(kitchen, 870, 20, "kitchen_door")
        kitchen_window = ddao.add_window(kitchen, 0, 0, "kitchen_window")

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
                n = random.randint(18, 20)
                start_time2 = given_date + timedelta(hours = n)
                on_minutes2 = random.randint(60, 180)
                end_time2 = start_time2 + timedelta(minutes = on_minutes2) 
                edao.add_event(kitchen_light, "ON", start_time2)
                edao.add_event(kitchen_light, "OFF", end_time2) 
                usage_minutes = on_minutes + on_minutes2 
                usage = general_eq(60, timedelta(minutes =usage_minutes))
                udao.add_usage(kitchen_light, dates, "electric", usage/1000)
            else:
                r = random.randint(4, 5)
                usage_time = 0
                for x in range(r):
                    s = random.randint(7, 20)
                    start_time = given_date + timedelta(hours = s)
                    on_minutes = random.randint(15 , 180)
                    end_time = start_time + timedelta(minutes =on_minutes)
                    edao.add_event(kitchen_light, "ON", start_time)
                    edao.add_event(kitchen_light, "OFF", end_time)
                    usage_time += on_minutes
                usage = general_eq(60, timedelta(minutes =usage_time))
                udao.add_usage(kitchen_light, dates, "electric", usage/1000)


        """

        Refrigerator usage comuptation

        """  
        def refrigerator_usage(given_date:  datetime):
            dates = given_date
            edao.add_event(refrigerator, "ON", dates)
            usage = general_eq(150 , timedelta(hours = 24))
            udao.add_usage(refrigerator, dates, "electric", usage /1000)


        """

        Dishwasher usage comuptation

        """  
        def dishwasher_usage(given_date: datetime):
            dates = given_date
            days = calendar.day_name[dates.weekday()]
            if days == "Monday" or days == "Wednesday" or days == "Thursday" or days == "Friday":
                r = random.randint(18, 20)
                start_time = given_date + timedelta(hours = r)
                end_time = start_time + timedelta(minutes = 45)
                edao.add_event(dishwasher, "ON", start_time)
                edao.add_event(dishwasher, "OFF", end_time)
                usage = general_eq(1800 ,timedelta(minutes = 45))
                water_heater_usage(start_time, 6)
                udao.add_usage(dishwasher, dates, "electric", usage/1000)
                udao.add_usage(dishwasher, dates, "water", water_usage_calculation(6))



        """

        Stove usage comuptation

        """        
        def Stove_usage(given_date: datetime):
            dates = given_date
            days = calendar.day_name[dates.weekday()]
            if days == "Monday" or days == "Tuesday" or days == "Wednesday" or days == "Thursday" or days == "Friday":
                r = random.randint(18, 20)
                start_time = given_date + timedelta(hours = r)
                end_time = start_time + timedelta(minutes = 15)
                edao.add_event(stove, "ON", start_time)
                edao.add_event(stove, "OFF", end_time )
                usage = general_eq(3500 ,timedelta(minutes = 15))
                udao.add_usage(stove, dates, "electric", usage/1000)
            else: 
                r = random.randint(7, 22)
                start_time = given_date + timedelta(hours = r)
                end_time = start_time + timedelta(minutes = 15)
                edao.add_event(stove, "ON", start_time)
                edao.add_event(stove, "OFF", end_time)
                usage = general_eq(3500 ,timedelta(minutes = 30))
                udao.add_usage(stove, dates, "electric", usage/1000)

        """

        Oven usage comuptation

        """  
        def oven_usage(given_date: datetime):
            dates = given_date
            days = calendar.day_name[dates.weekday()]
            if days == "Monday" or days == "Tuesday" or days == "Wednesday" or days == "Thursday" or days == "Friday":
                r = random.randint(18, 21)
                start_time = given_date + timedelta(hours = r)
                end_time = start_time + timedelta(minutes = 45)
                edao.add_event(oven, "ON", start_time)
                edao.add_event(oven, "OFF", end_time )
                usage = general_eq(4000 ,timedelta(minutes = 45))
                udao.add_usage(oven, dates, "electric", usage/1000)
            else: 
                r = random.randint(18, 21)
                start_time = given_date + timedelta(hours = r)
                end_time = start_time + timedelta(minutes = 60)
                edao.add_event(stove, "ON", start_time)
                edao.add_event(stove, "OFF", end_time)
                usage = general_eq(4000 ,timedelta(minutes = 60))
                udao.add_usage(oven, dates, "electric", usage/1000)

        
        """

        Microwave usage comuptation

        """          
        def microwave_usage(given_date: datetime):
            dates = given_date
            days = calendar.day_name[dates.weekday()]
            if days == "Monday" or days == "Tuesday" or days == "Wednesday" or days == "Thursday" or days == "Friday":
                r = random.randint(18, 21)
                start_time = given_date + timedelta(hours = r)
                end_time = start_time + timedelta(minutes = 20)
                edao.add_event(microwave, "ON", start_time)
                edao.add_event(microwave, "OFF", end_time )
                usage = general_eq(1100,timedelta(minutes = 20))
                udao.add_usage(microwave, dates, "electric", usage/1000)
            else: 
                r = random.randint(9, 21)
                start_time = given_date + timedelta(hours = r)
                end_time = start_time + timedelta(minutes = 30)
                edao.add_event(microwave, "ON", start_time)
                edao.add_event(microwave, "OFF", end_time)
                usage =  general_eq(1100,timedelta(minutes = 30))
                udao.add_usage(microwave, dates, "electric", usage/1000)

        
        """

        Overall kicthen usage comuptation

        """     
        def generate_kitchen_usage(start_date: datetime, end_date: datetime):       
            print("Generating kitchen usage")         
            days_date = end_date-start_date
            first_date = start_date
            for x in range(days_date.days):
                print(" Kitchen > ",first_date)
                dishwasher_usage(first_date)
                Stove_usage(first_date)
                oven_usage(first_date)
                microwave_usage(first_date)
                refrigerator_usage(first_date)
                kitchen_light_usage(first_date)
                first_date += timedelta(days=1)

       


        # TODO: Garage historical data generation.
        garage = ldao.add_location('Garage')   
        main_hvac = ddao.add_hvac(garage, 0, 0, "main_hvac", 3500 )
        garage_door = ddao.add_door(garage, 568, 80,"garage_door")
        birmingham = City_location("Birmingham", "Alabama", "61ddd4b2d1917d2d18707c527467ad92")
        water_heater = ddao.add_electric_device(garage, 700, 180, "water_heater", 4500)


        def water_heater_usage(given_date: datetime, water: float):
            start_time = given_date
            HEATER_MIN_PER_GAL = timedelta(minutes=4)
            process_time = water * HEATER_MIN_PER_GAL
            end_time = start_time + process_time
            edao.add_event(water_heater, "ON", start_time)
            edao.add_event(water_heater, "OFF", end_time)
            usage = compute_water_heater_usage(water)
            udao.add_usage(water_heater, given_date, "electric", usage/1000)




        """
        MAIN HVAC USAGE COMPUTATION
        """
        def main_hvac_usage(given_date: datetime):
            s = random.randint(70, 75)       ## RANDOMLY CHOOSES THE SET HVAC TEMP 
            h = s + random.randint(0,3)      ## RANDOMLY CHOOSES THE TEMP   
            l = s - random.randint(0,3)
            temp = birmingham.one_day_temp(given_date)
            int_temp = random.randint(s-2,s+2) 
            times = 0
            usage =0
            for x in range(24):
                out_temp = temp[x+1]
                for m in range(60):
                    dates = given_date + timedelta(hours = x) + timedelta(minutes = m)
                    betweenfirst = dates - timedelta(minutes = 1)

                    betweenlast = dates
                    # door_count = EventLog.query.filter(EventLog.date.between(dates - timedelta(minutes = 1), dates), EventLog.state == 'OPENDOOR').count()
                    # window_count = EventLog.query.filter(EventLog.date.between(dates - timedelta(minutes = 1), dates ), EventLog.state == 'OPENWINDOW').count()
                    door_count = db.engine.execute(f"SELECT COUNT(*) FROM EventLog WHERE state = 'OPENDOOR' AND date BETWEEN '{betweenfirst.strftime('%Y-%m-%d %H:%M:%S')}' AND '{betweenlast.strftime('%Y-%m-%d %H:%M:%S')}'").first()[0]
                    window_count = db.engine.execute(f"SELECT COUNT(*) FROM EventLog WHERE state = 'OPENWINDOW' AND date BETWEEN '{betweenfirst.strftime('%Y-%m-%d %H:%M:%S')}' AND '{betweenlast.strftime('%Y-%m-%d %H:%M:%S')}'").first()[0]
                    int_temp = get_new_interior_temperature(int_temp, out_temp, 0, 0)
                    if int_temp == h or int_temp >= h or int_temp == l or int_temp <= l:
                        times = abs(s - h)
                    if times != 0:
                        usage += general_eq(3500,timedelta(minutes = 1))
                        edao.add_hvac_event(main_hvac,"ON", int_temp, dates)
                        edao.add_hvac_event(main_hvac,"OFF", int_temp, dates+timedelta(minutes =1))
                        int_temp = get_new_HVAC_temperature(int_temp, s)
                        times -=1
                if usage != 0:
                    udao.add_usage(main_hvac, dates, "electric", usage/1000)
                usage = 0
                
                    
        #TODO: Living room historical data generation
        living_room = ldao.add_location('Living room')
        livingroom_tv = ddao.add_electric_device(living_room, 0, 0, "living_room_tv", 636)
        livingroom_light = ddao.add_light(living_room, 0, 0, "living_room_light", 60)
        main_door = ddao.add_door(living_room, 15, 710, "main_door")
        livingroom_window = ddao.add_window(living_room, 0, 0, "livingroom_window")

        """

        Livingroom TV usage computation

        """
        def livingroom_tv_usage(given_date: datetime):
            dates = given_date
            days = calendar.day_name[dates.weekday()]
            if days == "Monday" or days == "Tuesday" or days == "Wednesday" or days == "Thursday" or days == "Friday":
                r = random.randint(16, 18)
                start_time = given_date + timedelta(hours = r)
                end_time = start_time + timedelta(hours = 4)
                edao.add_event(livingroom_tv, "ON", start_time)
                edao.add_event(livingroom_tv, "OFF", end_time )
                usage = general_eq(636,timedelta(minutes = 240))
                udao.add_usage(livingroom_tv, dates, "electric", usage/1000)
            else: 
                r = random.randint(9, 16)
                start_time = given_date + timedelta(hours = r)
                end_time = start_time + timedelta(hours = 8)
                edao.add_event(livingroom_tv, "ON", start_time)
                edao.add_event(livingroom_tv, "OFF", end_time)
                usage =  general_eq(636,timedelta(minutes = 480))
                udao.add_usage(livingroom_tv, dates, "electric", usage /1000)
        


        """

        Usag of Doors computation

        """
        def door_usage(given_date: datetime):
            dates = given_date
            days = calendar.day_name[dates.weekday()]
            if days == "Monday" or days == "Tuesday" or days == "Wednesday" or days == "Thursday" or days == "Friday":
                for d in range(16):
                    if d <= 3:
                        r = random.randint(28, 30)
                        start_time = given_date + timedelta(hours = 7) + timedelta(minutes = r)
                        end_time = start_time + timedelta(seconds = 30)
                        door_selection = random.randint(1,2)
                        if door_selection ==1:
                           edao.add_event(main_door, "OPENDOOR", start_time)
                           edao.add_event(main_door, "CLOSEDOOR", end_time)
                        elif door_selection ==2:
                            edao.add_event(garage_door, "OPENDOOR", start_time)
                            edao.add_event(garage_door, "CLOSEDOOR", end_time)
                            
                    elif d == 4 and d == 5:
                        r = random.randint(0,5)
                        start_time = given_date + timedelta(hours = 16) + timedelta(minutes = r)
                        end_time = start_time + timedelta(seconds = 30)
                        door_selection = random.randint(1,2)
                    
                        if door_selection ==1:
                           edao.add_event(main_door, "OPENDOOR", start_time)
                           edao.add_event(main_door, "CLOSEDOOR", end_time)
                        elif door_selection ==2:
                            edao.add_event(garage_door, "OPENDOOR", start_time)
                            edao.add_event(garage_door, "CLOSEDOOR", end_time)
                        
                    elif d == 6 and d == 7:
                        r = random.randint(30, 35)
                        start_time = given_date + timedelta(hours = 17) + timedelta(minutes = r)
                        end_time = start_time + timedelta(seconds = 30)
                        door_selection = random.randint(1,2)
                        if door_selection ==1:
                           edao.add_event(main_door, "OPENDOOR", start_time)
                           edao.add_event(main_door, "CLOSEDOOR", end_time)
                        elif door_selection ==2:
                            edao.add_event(garage_door, "OPENDOOR", start_time)
                            edao.add_event(garage_door, "CLOSEDOOR", end_time)
                    else:
                        hh = random.randint(6, 22)
                        mm = random.randint(0,59)
                        door_selection= random.randint(1,3)
                        start_time = given_date + timedelta(hours = hh ) + timedelta(minutes = mm)
                        end_time = start_time + timedelta(seconds = 30)
                        if door_selection == 1:
                            edao.add_event(main_door, "OPENDOOR", start_time)
                            edao.add_event(main_door, "CLOSEDOOR", end_time)
                           
                        elif door_selection == 2:
                            edao.add_event(garage_door, "OPENDOOR", start_time)
                            edao.add_event(garage_door, "CLOSEDOOR", end_time)   
                        elif door_selection == 3:
                            edao.add_event(kitchen_door, "OPENDOOR", start_time)
                            edao.add_event(kitchen_door, "CLOSEDOOR", end_time)
            else:
                for x in range(32):
                    hh = random.randint(0, 22)
                    mm = random.randint(0,59)
                    door_selection= random.randint(1,3)
                    start_time = given_date + timedelta(hours = hh ) + timedelta(minutes = mm)
                    end_time = start_time + timedelta(seconds = 30)
                    
                    if door_selection == 1:
                        edao.add_event(main_door, "OPENDOOR", start_time)
                        edao.add_event(main_door, "CLOSEDOOR", end_time)
                           
                    elif door_selection == 2:
                        edao.add_event(garage_door, "OPENDOOR", start_time)
                        edao.add_event(garage_door, "CLOSEDOOR", end_time)   
                    elif door_selection == 3:
                        edao.add_event(kitchen_door, "OPENDOOR", start_time)
                        edao.add_event(kitchen_door, "CLOSEDOOR", end_time)
        """
        Window Usage computation
        """
        def window_usage(given_date: datetime):
            dates = given_date
            days = calendar.day_name[dates.weekday()]
            if days == "Monday" or days == "Tuesday" or days == "Wednesday" or days == "Thursday" or days == "Friday":
                for d in range(random.randint(0, 10)):
                    if d <= 1:
                        r = random.randint(28, 30)
                        start_time = given_date + timedelta(hours = 7) + timedelta(minutes = r)
                        open_time = random.randint(4, 20)
                        end_time = start_time + timedelta(minutes = open_time)
                        window_selection = random.randint(1,3)
                        if window_selection ==1:
                           edao.add_event(livingroom_window, "OPENWINDOW", start_time)
                           edao.add_event(livingroom_window, "CLOSEWINDOW", end_time)
                        elif window_selection ==2:
                            edao.add_event(kitchen_window, "OPENWINDOW", start_time)
                            edao.add_event(kitchen_window, "CLOSEWINDOW", end_time)
                        elif window_selection == 3:
                            edao.add_event(bedroom1_window, "OPENWINDOW", start_time)
                            edao.add_event(bedroom1_window, "CLOSEWINDOW", end_time)
                        elif window_selection == 4:
                            edao.add_event(bedroom2_window, "OPENWINDOW", start_time)
                            edao.add_event(bedroom2_window, "CLOSEWINDOW", end_time)
    
                    else:
                        hh = random.randint(6, 22)
                        mm = random.randint(0,59)
                        door_selection= random.randint(1,2)
                        start_time = given_date + timedelta(hours = hh ) + timedelta(minutes = mm)
                        open_time = random.randint(4, 30)
                        end_time = start_time + timedelta(minutes = open_time)
                        window_selection = random.randint(1,4)
                        if window_selection ==1:
                           edao.add_event(livingroom_window, "OPENWINDOW", start_time)
                           edao.add_event(livingroom_window, "CLOSEWINDOW", end_time)
                        elif window_selection ==2:
                            edao.add_event(kitchen_window, "OPENWINDOW", start_time)
                            edao.add_event(kitchen_window, "CLOSEWINDOW", end_time)
                        elif window_selection == 3:
                            edao.add_event(bedroom1_window, "OPENWINDOW", start_time)
                            edao.add_event(bedroom1_window, "CLOSEWINDOW", end_time)
                        elif window_selection == 4:
                            edao.add_event(bedroom2_window, "OPENWINDOW", start_time)
                            edao.add_event(bedroom2_window, "CLOSEWINDOW", end_time)
            else:
                for x in range(32):
                    hh = random.randint(0, 22)
                    mm = random.randint(0,59)
                    door_selection= random.randint(1,2)
                    start_time = given_date + timedelta(hours = hh ) + timedelta(minutes = mm)
                    end_time = start_time + timedelta(seconds = 30)
                    window_selection = random.randint(1,4)
                    if window_selection ==1:
                        edao.add_event(livingroom_window, "OPENWINDOW", start_time)
                        edao.add_event(livingroom_window, "CLOSEWINDOW", end_time)
                    elif window_selection ==2:
                        edao.add_event(kitchen_window, "OPENWINDOW", start_time)
                        edao.add_event(kitchen_window, "CLOSEWINDOW", end_time)
                    elif window_selection == 3:
                        edao.add_event(bedroom1_window, "OPENWINDOW", start_time)
                        edao.add_event(bedroom1_window, "CLOSEWINDOW", end_time)
                    elif window_selection == 4:
                        edao.add_event(bedroom2_window, "OPENWINDOW", start_time)
                        edao.add_event(bedroom2_window, "CLOSEWINDOW", end_time)

        """

        Living Room light usage Computation 

        """
        def livingroom_light_usage(given_date: datetime):
            dates = given_date
            days = calendar.day_name[dates.weekday()]
            if days == "Monday" or days == "Tuesday" or days == "Wednesday" or days == "Thursday" or days == "Friday":
                d = random.randint(5, 6)
                start_time = given_date + timedelta(hours = d)
                on_minutes = random.randint(30, 60)
                end_time = start_time + timedelta(minutes = on_minutes) 
                edao.add_event(livingroom_light, "ON", start_time)
                edao.add_event(livingroom_light, "OFF", end_time)
                n = random.randint(18, 20)
                start_time2 = given_date + timedelta(hours = n)
                on_minutes2 = random.randint(60, 180)
                end_time2 = start_time2 + timedelta(minutes = on_minutes2) 
                edao.add_event(livingroom_light, "ON", start_time2)
                edao.add_event(livingroom_light, "OFF", end_time2) 
                usage_minutes = on_minutes + on_minutes2 
                usage = general_eq(60, timedelta(minutes =usage_minutes))
                udao.add_usage(livingroom_light, dates, "electric", usage/1000)
            else:
                r = random.randint(4, 5)
                usage_time = 0
                for x in range(r):
                    s = random.randint(7, 20)
                    start_time = given_date + timedelta(hours = s)
                    on_minutes = random.randint(15 , 180)
                    end_time = start_time + timedelta(minutes =on_minutes)
                    edao.add_event(livingroom_light, "ON", start_time)
                    edao.add_event(livingroom_light, "OFF", end_time)
                    usage_time += on_minutes
                usage = general_eq(60, timedelta(minutes =usage_time))
                udao.add_usage(livingroom_light, dates, "electric", usage/1000)


        """

        Adding up devices and Window to Bedroom1 

        """
        Bedroom1 = ldao.add_location('Bedroom1')
        bedroom1_light = ddao.add_light(Bedroom1, 0, 0, "Bedroom1_light", 60)
        bedroom1_tv = ddao.add_electric_device(Bedroom1, 0, 0, "bedroom1_tv", 100)
        bedroom1_window = ddao.add_window(Bedroom1, 0, 0, "bedroom1_window")



        """

        Bedroom1 light usage Computation

        """

        def bedroom1_light_usage(given_date: datetime):
            dates = given_date
            days = calendar.day_name[dates.weekday()]
            if days == "Monday" or days == "Tuesday" or days == "Wednesday" or days == "Thursday" or days == "Friday":
                d = random.randint(5, 7)
                start_time = given_date + timedelta(hours = d)
                on_minutes = random.randint(30, 60)
                end_time = start_time + timedelta(minutes = on_minutes) 
                edao.add_event(bedroom1_light, "ON", start_time)
                edao.add_event(bedroom1_light, "OFF", end_time)
                n = random.randint(18, 22)
                start_time2 = given_date + timedelta(hours = n)
                on_minutes2 = random.randint(60, 180)
                end_time2 = start_time2 + timedelta(minutes = on_minutes2) 
                edao.add_event(bedroom1_light, "ON", start_time2)
                edao.add_event(bedroom1_light, "OFF", end_time2) 
                usage_minutes = on_minutes + on_minutes2 
                usage = general_eq(60, timedelta(minutes =usage_minutes))
                udao.add_usage(bedroom1_light, dates, "electric", usage/1000)
            else:
                r = random.randint(4, 5)
                usage_time = 0
                for x in range(r):
                    s = random.randint(7, 22)
                    start_time = given_date + timedelta(hours = s)
                    on_minutes = random.randint(15 , 180)
                    end_time = start_time + timedelta(minutes =on_minutes)
                    edao.add_event(bedroom1_light, "ON", start_time)
                    edao.add_event(bedroom1_light, "OFF", end_time)
                    usage_time += on_minutes
                usage = general_eq(60, timedelta(minutes =usage_time))
                udao.add_usage(bedroom1_light, dates, "electric", usage/1000)


        """
        
        Bedroom1 Tv usage Computation

        """
        def bedroom1_tv_usage(given_date: datetime):
            dates = given_date
            days = calendar.day_name[dates.weekday()]
            if days == "Monday" or days == "Tuesday" or days == "Wednesday" or days == "Thursday" or days == "Friday":
                r = random.randint(20, 22)
                start_time = given_date + timedelta(hours = r)
                end_time = start_time + timedelta(hours = 2)
                edao.add_event(bedroom1_tv, "ON", start_time)
                edao.add_event(bedroom1_tv, "OFF", end_time )
                usage = general_eq(100,timedelta(minutes = 120))
                udao.add_usage(bedroom1_tv, dates, "electric", usage/1000)
            else: 
                r = random.randint(9, 22)
                start_time = given_date + timedelta(hours = r)
                end_time = start_time + timedelta(hours = 4)
                edao.add_event(bedroom1_tv, "ON", start_time)
                edao.add_event(bedroom1_tv, "OFF", end_time)
                usage = general_eq(100,timedelta(minutes = 240))
                udao.add_usage(bedroom1_tv, dates, "electric", usage/1000)

        """

        Adding devices and windows to Bedroom2 


        """
        Bedroom2 = ldao.add_location('Bedroom2')
        bedroom2_light = ddao.add_light(Bedroom2, 0, 0, "Bedroom2_light", 60)
        bedroom2_tv = ddao.add_electric_device(Bedroom2, 0, 0,"bedroom2_tv", 100)
        bedroom2_window = ddao.add_window(Bedroom2, 0, 0, "bedroom_window")


        """

        Bedroom2 light usage Computation

        """
        def bedroom2_light_usage(given_date: datetime):
            dates = given_date
            days = calendar.day_name[dates.weekday()]
            if days == "Monday" or days == "Tuesday" or days == "Wednesday" or days == "Thursday" or days == "Friday":
                d = random.randint(5, 6)
                start_time = given_date + timedelta(hours = d)
                on_minutes = random.randint(30, 60)
                end_time = start_time + timedelta(minutes = on_minutes) 
                edao.add_event(bedroom1_light, "ON", start_time)
                edao.add_event(bedroom1_light, "OFF", end_time)
                n = random.randint(18, 20)
                start_time2 = given_date + timedelta(hours = n)
                on_minutes2 = random.randint(60, 180)
                end_time2 = start_time2 + timedelta(minutes = on_minutes2) 
                edao.add_event(bedroom1_light, "ON", start_time2)
                edao.add_event(bedroom1_light, "OFF", end_time2) 
                usage_minutes = on_minutes + on_minutes2 
                usage = general_eq(60, timedelta(minutes =usage_minutes))
                udao.add_usage(bedroom1_light, dates, "electric", usage/1000)
            else:
                r = random.randint(4, 5)
                usage_time = 0
                for x in range(r):
                    s = random.randint(7, 20)
                    start_time = given_date + timedelta(hours = s)
                    on_minutes = random.randint(15 , 180)
                    end_time = start_time + timedelta(minutes = on_minutes)
                    edao.add_event(bedroom1_light, "ON", start_time)
                    edao.add_event(bedroom1_light, "OFF", end_time)
                    usage_time += on_minutes
                usage = general_eq(60, timedelta(minutes =usage_time))
                udao.add_usage(bedroom1_light, dates, "electric", usage/1000)

        """

        Bedroom2 Tv usage Computation

        """
        def bedroom2_tv_usage(given_date: datetime):
            dates = given_date
            days = calendar.day_name[dates.weekday()]
            if days == "Monday" or days == "Tuesday" or days == "Wednesday" or days == "Thursday" or days == "Friday":
                r = random.randint(16, 20)
                start_time = given_date + timedelta(hours = r)
                end_time = start_time + timedelta(hours = 2)
                edao.add_event(bedroom2_tv, "ON", start_time)
                edao.add_event(bedroom2_tv, "OFF", end_time )
                usage = general_eq(100,timedelta(minutes = 120))
                udao.add_usage(bedroom2_tv, dates, "electric", usage/1000)
            else: 
                r = random.randint(9, 20)
                start_time = given_date + timedelta(hours = r)
                end_time = start_time + timedelta(hours = 4)
                edao.add_event(bedroom2_tv, "ON", start_time)
                edao.add_event(bedroom2_tv, "OFF", end_time)
                usage = general_eq(100,timedelta(minutes = 240))
                udao.add_usage(bedroom2_tv, dates, "electric", usage/1000)

        """
        Adding bathroom1 and Adding devices to it

        """
        Bathroom1 = ldao.add_location('Bathroom1')
        bathroom1_exhaust_fan = ddao.add_electric_device(Bathroom1, 0, 0, 'bathroom1_exhaust_fan',30)
        bathroom1_light = ddao.add_light(Bathroom1, 0, 0, 'bathroom1_light',60)
        bathroom1_bath_water_meter = ddao.add_water_meter(Bathroom1,  0, 0, 'bathroom1_bath_water_meter')

        def bathroom1_light_usage(given_date: datetime, usage_start_time: int):
            dates = given_date
            days = calendar.day_name[dates.weekday()]
            if days == "Monday" or days == "Tuesday" or days == "Wednesday" or days == "Thursday" or days == "Friday":
                start_time = given_date + timedelta(hours = usage_start_time)
                on_minutes = random.randint(45, 60)
                end_time = start_time + timedelta(minutes = on_minutes) 
                edao.add_event(bathroom1_light, "ON", start_time)
                edao.add_event(bathroom1_light, "OFF", end_time)
                usage = general_eq(60, timedelta(minutes = on_minutes))
                udao.add_usage(bathroom1_light, dates, "electric", usage/1000)
            else:
                r = random.randint(1, 3)
                usage_time = 0
                for x in range(r):
                    s = random.randint(7, 20)
                    start_time = given_date + timedelta(hours = s)
                    on_minutes = random.randint(20 , 60)
                    end_time = start_time + timedelta(minutes = on_minutes)
                    edao.add_event(bathroom1_light, "ON", start_time)
                    edao.add_event(bathroom1_light, "OFF", end_time)
                    usage_time += on_minutes
                usage = general_eq(60, timedelta(minutes =on_minutes))
                udao.add_usage(bathroom1_light, dates, "electric", usage/1000)

        def bathroom1_exhaust_fan_usage(given_date: datetime, starting_time:int, on_minutes:int):
            dates = given_date
            start_time = starting_time
            end_time = start_time + timedelta(minutes = on_minutes)
            edao.add_event(bathroom1_exhaust_fan, "ON", start_time)
            edao.add_event(bathroom1_exhaust_fan, "OFF", end_time)
            usage = general_eq(60, timedelta(minutes = on_minutes))
            udao.add_usage(bathroom1_exhaust_fan, dates, "electric", usage/1000)

        def bathroom1_bath_water_meter_usage(given_date: datetime, usage_start_time: int, times: int):
            dates = given_date
            days = calendar.day_name[dates.weekday()]
            heater_water = 30 * 0.65
            if times == 2:
                start_time = given_date + timedelta(hours = usage_start_time)
                on_minutes = random.randint(20, 25)
                end_time = start_time + timedelta(minutes = on_minutes)
                bathroom1_exhaust_fan_usage(given_date, start_time, on_minutes)
                water_heater_usage(start_time, heater_water) 
                edao.add_event(bathroom1_bath_water_meter, "ON", start_time)
                edao.add_event(bathroom1_bath_water_meter, "OFF", end_time)
                usage = water_usage_calculation(30)
                udao.add_usage(bathroom1_bath_water_meter, dates, "water", usage)
                #Time2
                start_time2 = end_time +timedelta(minutes = 5)
                on_minutes2 = random.randint(20,25)
                end_time2 = start_time2 + timedelta(minutes = on_minutes2)
                edao.add_event(bathroom1_bath_water_meter, "ON", start_time2)
                edao.add_event(bathroom1_bath_water_meter, "OFF", end_time2)
                bathroom1_exhaust_fan_usage(given_date, start_time2, on_minutes2) 
                water_heater_usage(start_time2, heater_water)
                usage1 = water_usage_calculation(30)
                udao.add_usage(bathroom1_bath_water_meter, dates, "water", usage1)
            else:
                start_time = given_date + timedelta(hours = usage_start_time)
                on_minutes = random.randint(20, 25)
                end_time = start_time + timedelta(minutes = on_minutes)
                bathroom1_exhaust_fan_usage(given_date, start_time, on_minutes) 
                water_heater_usage(start_time, heater_water)
                edao.add_event(bathroom1_bath_water_meter, "ON", start_time)
                edao.add_event(bathroom1_bath_water_meter, "OFF", end_time)
                usage = water_usage_calculation(30)
                udao.add_usage(bathroom1_bath_water_meter, dates, "water", usage)
                #Time 2
                start_time2 = end_time +timedelta(minutes = 5)
                on_minutes2 = random.randint(20,25)
                end_time2 = start_time2 + timedelta(minutes = on_minutes2)
                edao.add_event(bathroom1_bath_water_meter, "ON", start_time2)
                edao.add_event(bathroom1_bath_water_meter, "OFF", end_time2)
                bathroom1_exhaust_fan_usage(given_date, start_time2, on_minutes2) 
                water_heater_usage(start_time2, heater_water)
                usage2 = water_usage_calculation(30)
                udao.add_usage(bathroom1_bath_water_meter, dates, "water", usage2)
                #Time 3
                start_time3 = end_time2 +timedelta(hours = 3)
                on_minutes3 = random.randint(20,25)
                end_time3 = start_time3 + timedelta(minutes = on_minutes3)
                edao.add_event(bathroom1_bath_water_meter, "ON", start_time3)
                edao.add_event(bathroom1_bath_water_meter, "OFF", end_time3)
                bathroom1_exhaust_fan_usage(given_date, start_time3, on_minutes3) 
                water_heater_usage(start_time3, heater_water)
                usage3 = water_usage_calculation(30)
                udao.add_usage(bathroom1_bath_water_meter, dates, "water", usage3)


        

         

        """
        Adding bathroom1 and Adding devices to it

        """
        Bathroom2 = ldao.add_location('Bathroom2')
        bathroom2_exhaust_fan = ddao.add_electric_device(Bathroom2, 0, 0, 'bathroom2_exhaust_fan',30)
        bathroom2_light = ddao.add_light(Bathroom2, 0, 0, 'bathroom2_light',60)
        bathroom2_shower_water_meter= ddao.add_water_meter(Bathroom2, 0, 0, 'bathroom2_shower_water_meter')
        
        def bathroom2_light_usage(given_date: datetime, usage_start_time: int):
            dates = given_date
            days = calendar.day_name[dates.weekday()]
            if days == "Monday" or days == "Tuesday" or days == "Wednesday" or days == "Thursday" or days == "Friday":
                start_time = given_date + timedelta(hours = usage_start_time)
                on_minutes = random.randint(45, 60)
                end_time = start_time + timedelta(minutes = on_minutes) 
                edao.add_event(bathroom2_light, "ON", start_time)
                edao.add_event(bathroom2_light, "OFF", end_time)
                usage = general_eq(60, timedelta(minutes = on_minutes))
                udao.add_usage(bathroom2_light, dates, "electric", usage/1000)
            else:
                r = random.randint(1, 3)
                usage_time = 0
                for x in range(r):
                    s = random.randint(7, 20)
                    start_time = given_date + timedelta(hours = s)
                    on_minutes = random.randint(20 , 60)
                    end_time = start_time + timedelta(minutes = on_minutes)
                    edao.add_event(bathroom2_light, "ON", start_time)
                    edao.add_event(bathroom2_light, "OFF", end_time)
                    usage_time += on_minutes
                usage = general_eq(60, timedelta(minutes =on_minutes))
                udao.add_usage(bathroom2_light, dates, "electric", usage/1000)

        def bathroom2_exhaust_fan_usage(given_date: datetime, starting_time:int, on_minutes:int):
            dates = given_date
            start_time = starting_time
            end_time = start_time + timedelta(minutes = on_minutes)
            edao.add_event(bathroom2_exhaust_fan, "ON", start_time)
            edao.add_event(bathroom2_exhaust_fan, "OFF", end_time)
            usage = general_eq(60, timedelta(minutes = on_minutes))
            udao.add_usage(bathroom2_exhaust_fan, dates, "electric", usage/1000)

        def bathroom2_shower_water_meter_usage(given_date: datetime, usage_start_time: int, times: int):
            dates = given_date
            days = calendar.day_name[dates.weekday()]
            heater_water = 25 * 0.65
            if times == 2:
                start_time = given_date + timedelta(hours = usage_start_time)
                on_minutes = random.randint(20, 25)
                end_time = start_time + timedelta(minutes = on_minutes)
                bathroom2_exhaust_fan_usage(given_date, start_time, on_minutes) 
                water_heater_usage(start_time, heater_water)
                edao.add_event(bathroom2_shower_water_meter, "ON", start_time)
                edao.add_event(bathroom2_shower_water_meter, "OFF", end_time)
                usage = water_usage_calculation(25)
                udao.add_usage(bathroom2_shower_water_meter, dates, "water", usage)
                #Time2
                start_time2 = end_time +timedelta(minutes = 5)
                on_minutes2 = random.randint(20,25)
                end_time2 = start_time2 + timedelta(minutes = on_minutes2)
                edao.add_event(bathroom2_shower_water_meter, "ON", start_time2)
                edao.add_event(bathroom2_shower_water_meter, "OFF", end_time2)
                bathroom2_exhaust_fan_usage(given_date, start_time2, on_minutes2)
                water_heater_usage(start_time2, heater_water) 
                usage1 = water_usage_calculation(25)
                udao.add_usage(bathroom2_shower_water_meter, dates, "water", usage1)
            else:
                start_time = given_date + timedelta(hours = usage_start_time)
                on_minutes = random.randint(20, 25)
                end_time = start_time + timedelta(minutes = on_minutes)
                bathroom2_exhaust_fan_usage(given_date, start_time, on_minutes)
                water_heater_usage(start_time, heater_water) 
                edao.add_event(bathroom2_shower_water_meter, "ON", start_time)
                edao.add_event(bathroom2_shower_water_meter, "OFF", end_time)
                usage = water_usage_calculation(25)
                udao.add_usage(bathroom2_shower_water_meter, dates, "water", usage)
                #Time 2
                start_time2 = end_time +timedelta(minutes = 5)
                on_minutes2 = random.randint(20,25)
                end_time2 = start_time2 + timedelta(minutes = on_minutes2)
                edao.add_event(bathroom2_shower_water_meter, "ON", start_time2)
                edao.add_event(bathroom2_shower_water_meter, "OFF", end_time2)
                bathroom2_exhaust_fan_usage(given_date, start_time2, on_minutes2)
                water_heater_usage(start_time2, heater_water) 
                usage2 = water_usage_calculation(25)
                udao.add_usage(bathroom2_shower_water_meter, dates, "water", usage2)
                #Time 3
                start_time3 = end_time2 +timedelta(hours = 3)
                on_minutes3 = random.randint(20,25)
                end_time3 = start_time3 + timedelta(minutes = on_minutes3)
                edao.add_event(bathroom2_shower_water_meter, "ON", start_time3)
                edao.add_event(bathroom2_shower_water_meter, "OFF", end_time3)
                bathroom2_exhaust_fan_usage(given_date, start_time3, on_minutes3) 
                water_heater_usage(start_time3, heater_water)
                usage3 = water_usage_calculation(25)
                udao.add_usage(bathroom2_shower_water_meter, dates, "water", usage3)


        """
        Adding Laundary area and Addding washer and dryer         
        """
        Laundary_area = ldao.add_location('Laundary_area')
        washer = ddao.add_electric_device(Laundary_area,  840, 140, 'washer',500)
        washer_water_meter = ddao.add_water_meter(Laundary_area, 0, 0, 'washer_water_meter')
        dryer = ddao.add_electric_device(Laundary_area,  840, 140, 'dryer', 3000)


        def washer_usage(given_date: datetime):
            print("Generating washer usage")
            dates = given_date
            days = calendar.day_name[dates.weekday()]
            if days == "Saturday" or days == "Sunday":
                r = random.randint(10, 19)
                start_time = given_date + timedelta(hours = r)
                end_time = start_time + timedelta(minutes = 30)
                edao.add_event(washer, "ON", start_time)
                edao.add_event(washer, "OFF", end_time)
                dryer_usage(end_time+ timedelta(minutes =10) )   ##calling dryer methode to start 
                usage = general_eq(500 ,timedelta(minutes = 30))
                water_heater_usage(start_time, 20 * 0.85)       ##calling heater methode to start 
                udao.add_usage(washer, dates, "electric", usage/1000)
                udao.add_usage(washer_water_meter, dates, "water", water_usage_calculation(20))
                start_time2 = given_date + end_time + timedelta(minutes )
                end_time2 = start_time2 + timedelta(minutes = 30)
                edao.add_event(washer, "ON", start_time2)
                edao.add_event(washer, "OFF", end_time2)
                dryer_usage(end_time2+ timedelta(minutes =10)) ##calling dryer methode to start
                water_heater_usage(start_time2, 20 * 0.85)     ##calling heater methode to start
                usage2 = general_eq(500 ,timedelta(minutes = 30))
                udao.add_usage(washer, dates, "electric", usage2/1000)
                udao.add_usage(washer_water_meter, dates, "water", water_usage_calculation(20))

        def dryer_usage(given_date: datetime):
            print("Generating dryer usage")
            dates = given_date
            days = calendar.day_name[dates.weekday()]
            start_time = given_date
            end_time = start_time + timedelta(minutes = 30)
            edao.add_event(dryer, "ON", start_time)
            edao.add_event(dryer, "OFF", end_time)
            usage = general_eq(3000 ,timedelta(minutes = 30))
            udao.add_usage(dryer, dates, "electric", usage)


            

        """

        Giving start date and end date of which
        user wants to compute data for Bedroom1.

        """
        def Bedroom1_usage(start_date: datetime, end_date: datetime):      
            print("Generating bedroom1 usage")          
            days_date = end_date-start_date
            first_date = start_date
            for x in range(days_date.days):
                if(first_date == dt.today()):
                    break
                bedroom1_tv_usage(first_date)
                bedroom1_light_usage(first_date)
                first_date += timedelta(days=1)


        """

        Giving start date and end date of which
        user wants to compute data for Bedroom2.

        """
        def Bedroom2_usage(start_date: datetime, end_date: datetime):       
            print("Generating bedroom2 usage")         
            days_date = end_date-start_date
            first_date = start_date
            for x in range(days_date.days + 1):
                if(first_date == dt.today()):
                    break
                bedroom2_tv_usage(first_date)
                bedroom2_light_usage(first_date)
                first_date += timedelta(days=1)



        """

        Giving start date and end date of which
        user wants to compute data for Livingroom.

        """
        def living_room_usage(start_date: datetime, end_date: datetime):     
            print("Generating living room usage")           
            days_date = end_date-start_date
            first_date = start_date
            for x in range(days_date.days + 1):
                if(first_date == dt.today()):
                    break
                livingroom_tv_usage(first_date)
                livingroom_light_usage(first_date)
                first_date += timedelta(days=1)
       
        """

        Giving start date and end date of which
        user wants to compute data for doors.

        """
        def door_action(start_date: datetime, end_date: datetime):
            print("Generating door actions")
            days_date = end_date-start_date
            first_date = start_date
            for x in range(days_date.days + 1):
                if(first_date == dt.today()):
                    break
                door_usage(first_date)
                first_date += timedelta(days=1)
        
        """

        Giving start date and end date of which
        user wants to compute data for windows.

        """
        def window_action(start_date: datetime, end_date: datetime ):
            print("Generating window actions" )
            days_date = end_date-start_date
            first_date = start_date
            for x in range(days_date.days + 1):
                if(first_date == dt.today()):
                    break
                window_usage(first_date)
                first_date += timedelta(days=1)

        """

        Giving start date and end date of which
        user wants to compute data for Garage.

        """
        def garage_usage(start_date: datetime, end_date: datetime ):
            print("Generating garage usage")
            days_date = end_date - start_date
            first_date = start_date
            for x in range(days_date.days + 1):
                print(" Garage > ",first_date)
                if(first_date == dt.today()):
                    break
                main_hvac_usage(first_date)
                first_date += timedelta(days=1) 


      
        """

        Giving start date and end date of which
        user wants to compute data for Bathroom1.

        """
        def Bathroom1_usage(start_date: datetime, end_date: datetime ):
            print("Generating bathroom1_usage")
            days_date = end_date - start_date
            first_date = start_date
        
            for x in range(days_date.days + 1):
                days = calendar.day_name[first_date.weekday()]
                if(first_date == dt.today()):
                    break
                
                if days == "Monday" or days == "Tuesday" or days == "Wednesday" or days == "Thursday" or days == "Friday":
                    usage_time = random.randint(5, 6)
                    bathroom1_light_usage(first_date, usage_time)
                    bathroom1_bath_water_meter_usage(first_date, usage_time, 2)
                else:
                    usage_time = random.randint(7, 19)
                    bathroom1_bath_water_meter_usage(first_date, usage_time, 3)
                    bathroom1_light_usage(first_date, usage_time)
                first_date += timedelta(days=1) 


        def Bathroom2_usage(start_date: datetime, end_date: datetime ):
            print("Generating bathroom2 usage")
            days_date = end_date - start_date
            first_date = start_date
        
            for x in range(days_date.days + 1):                
                days = calendar.day_name[first_date.weekday()]
                if(first_date == dt.today()):
                    break
                
                if days == "Monday" or days == "Tuesday" or days == "Wednesday" or days == "Thursday" or days == "Friday":
                    usage_time = random.randint(5, 6)
                    bathroom2_light_usage(first_date, usage_time)
                    bathroom2_shower_water_meter_usage(first_date, usage_time, 2)
                else:
                    usage_time = random.randint(7, 19)
                    bathroom2_shower_water_meter_usage(first_date, usage_time, 3)
                    bathroom2_light_usage(first_date, usage_time)
                first_date += timedelta(days=1) 


        """

        Giving start date and end date of which
        user wants to compute data for entire home.

        """
        def home_usage(start: datetime, end: datetime):
            generate_kitchen_usage(start, end) ## calls generate_kitchen_usage
            Bedroom1_usage(start, end)  ## calls Bedroom1_usage
            door_action(start,end)  ## calls door_usage
            window_action(start, end)  ## calls window_usage
            Bedroom2_usage(start, end)  ## calls Bedroom2_usage
            living_room_usage(start, end)  ## calls Livingroom_usage
            garage_usage(start, end)  ## calls garage_usage
            Bathroom1_usage(start, end)
            Bathroom2_usage(start, end)
        

        """
        Test Case is below we can change 
        it later to compute data for last 2 months. 
        """
        home_usage(datetime.today() - timedelta(days= 7), datetime.today() - timedelta(days=1))


       


