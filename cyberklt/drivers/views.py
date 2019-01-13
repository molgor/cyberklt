# -*- coding: utf-8 -*-
from django.shortcuts import render
from drivers.models import Temperature
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('CyberKLT la forma más chingona de cuidar tu jardín')

def readTemperature(request):
    t = Temperature.create()
    return HttpResponse('La temperatura es: %s C.'%round(t.temp,2))
