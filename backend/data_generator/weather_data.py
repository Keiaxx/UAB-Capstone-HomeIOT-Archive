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


"""
Make an instance of this
with two atributes city_name
and state_name.
place = Location(city_name,state_name)
"""
class Location():
    def __init__(self, city_name:  str, state_name: str, key: str):
        self.city_name =city_name
        self.state_name = state_name
        self.key = key
        
    """
    CAll this function to get
    latitude of a place
    """
    def latitude(self) -> float:
        place = self.city_name + " " + self.state_name
        geolocator = Nominatim(user_agent="darksky1")
        locate = geolocator.geocode(place)     
        return locate.latitude

    
    """
    CAll this function to get
    longitude of the place
    """
    def longitude(self) -> float:
        place = self.city_name + " " + self.state_name
        geolocator = Nominatim(user_agent="darksky1")
        locate = geolocator.geocode(place)     
        return locate.longitude

    
    """
    The data of a date will be generated hourly
    in dictionary where hours(1-24) are used as
    keys and temperature is value.
    """
    def one_day_temp(self, date):
        lat=  self.latitude()
        long = self.longitude()
        PLACE = self.key, lat, long
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

    
    """
    The data will be generated of a
    particular hour of a particular date.
    """
    def one_hour_temp(self, date, hour) -> float:
        lat =  self.latitude()
        long = self.longitude()
        PLACE = self.key, lat, long
        yy = date.year
        mm = date.month
        dd = date.day
        hh = hour
        t = dt(yy,mm, dd, hh).isoformat()
        place = forecast(*PLACE, time=t)
        return place.hourly[hour].temperature

    """
    This will provide current tempreature 
    of the a specific place.
    """
    def current_temp(self):
        lat =  self.latitude()
        long = self.longitude()
        PLACE = self.key, lat, long
        now = dt.now()
        t = dt(now.year,now.month, now.day, now.hour).isoformat()
        place = forecast(*PLACE, time=t)
        return place['currently']['temperature']

    """
    This methode is used to
    change the location.
    """
    def change_city(self,city_name, state_name):
        self.city_name =city_name2w
        self.state_name =state_name

    
