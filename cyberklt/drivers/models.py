# -*- coding: utf-8 -*-
import numpy as np
from django.db import models
import drivers.MPL3115A2 as mpl

class Temperature(models.Model):
    temp = models.FloatField(default=-999.9) #Celcius
    altitude = models.FloatField(default=np.nan) #meters
    timestamp = models.DateTimeField(auto_now=True) 
    instrument = models.CharField(max_length=100,default="MPL3115A2")

    @classmethod
    def getTemp(cls):
        """
        Supose to measure temperature from the sensor
        """
        data = mpl.readData()
        temp = cls(temp=data['Temperature'])
        return temp

    @classmethod
    def create(cls):
        """
        Supose to measure temperature from the sensor
        """
        data = mpl.readData()
        temp = cls(temp=data['Temperature'],altitude=data['Altitude'])
        temp.save()
        return temp

    def __str__(self):
        time_ = self.timestamp.strftime(" |%H:%M %d-%M-%Y|")
        cad = "<Temperature reading: %s , %s>"%(self.temp,time_)
        return cad

class Pressure(models.Model):
    pressure = models.FloatField(default=-999.9) #KPa
    timestamp = models.DateTimeField(auto_now=True) 
    instrument = models.CharField(max_length=100,default="MPL3115A2")

    @classmethod
    def getPressure(cls):
        """
        Supose to measure temperature from the sensor
        """
        data = mpl.readData(mode=2)
        temp = cls(temp=data['Pressure'])
        return temp

    @classmethod
    def create(cls):
        """
        Supose to measure temperature from the sensor
        """
        data = mpl.readData(mode=2)
        temp = cls(pressure=data['Pressure'])
        temp.save()
        return temp

    def __str__(self):
        time_ = self.timestamp.strftime(" |%H:%M %d-%M-%Y|")
        cad = "<Pressure reading: %s , %s>"%(self.pressure,time_)
        return cad


