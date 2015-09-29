from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def prueba(request):
	return HttpResponse("Hola muchachos! Esto es el CyberKLT")

def lucecita(request):
	prendido = request.GET["switch"]
	if prendido == 'on':
		cadena = " Esta prendida"
	else:
		cadena = "Esta apagada"
	return HttpResponse(cadena)
