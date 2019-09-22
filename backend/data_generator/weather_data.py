#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 15:36:40 2019

@author: senaypatel
"""

from darksky import forecast
from datetime import datetime as dt
from datetime import timedelta
from datetime import date
from geopy.geocoders import Nominatim
import certifi
import ssl


class Location():
    def __init__(self, city_name:  str, state_name: str):
        self.city_name =city_name
        self.state_name = state_name
        
    def latitude(self) -> float:
        place = self.city_name + " " + self.state_name
        geolocator = Nominatim(user_agent="darksky1")
        locate = geolocator.geocode(place)     
        return locate.latitude
    
    def longitude(self) -> float:
        place = self.city_name + " " + self.state_name
        geolocator = Nominatim(user_agent="darksky1")
        locate = geolocator.geocode(place)     
        return locate.longitude

    def one_day_temp(self, date):
        lat=  self.latitude()
        long = self.longitude()
        key = "714247b8f24a0afa9474e19df782ceeb"
        PLACE = key, lat, long
        yy = date.year
        mm = date.month
        dd = date.day
        hh = date.hour
        t = dt(yy,mm, dd, hh).isoformat()
        place = forecast(*PLACE, time=t)
        a = [hour.temperature for hour in place.hourly[:2]]
        data ={}
        b =1
        for x in range(len(a)):
            data[b] = a[x]
            b += 1
        return data
    
    def one_hour_temp(self, date, hour) -> float:
        lat =  self.latitude()
        long = self.longitude()
        key = "714247b8f24a0afa9474e19df782ceeb"
        PLACE = key, lat, long
        yy = date.year
        mm = date.month
        dd = date.day
        hh = hour
        t = dt(yy,mm, dd, hh).isoformat()
        place = forecast(*PLACE, time=t)
        return place.hourly[hour].temperature
    
    def change_city(self,city_name, state_name):
        self.city_name =city_name2w
        self.state_name =state_name

    

    
"""Test CASES are given below
   just to give an idea how
   the code goes """


#start_date =dt(2019, 9, 17)
#end_date = dt(2019, 9, 17)

##start_date =dt(2019, 9, 22)
##end_date = dt(2019, 9, 22)
##
####temperatures("birmingham", "alabama", start_date, end_date)
##
###print(data,date(2019, 9, 18))
##place= Location("Chelsea", "Alabama")
##print(place.latitude(), place.longitude(), place.one_day_temp(start_date))


##place.change_city("Birmingham", "Alabama")
##print(place.latitude(), place.longitude(), place.one_day_temp(start_date))
##tempreature = place.one_day_temp(start_date)
##print(tempreature[1])
##tempreature = place.one_hour_temp(dt(2019, 9, 22), 13)
##print(tempreature)
