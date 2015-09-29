import RPi.GPIO as GPIO
import time


#PIN_NUMBER = 4 
GPIO.setmode(GPIO.BCM)

def getBinaryValues(PIN_NUMBER):
	data = []
	# Setup out signal to intialize DHT1l
	GPIO.setup(PIN_NUMBER,GPIO.OUT)
	# Send the signal 1 or True or High
	GPIO.output(PIN_NUMBER,GPIO.HIGH)
	# Hold it!
	time.sleep(0.025)
	# End signal
	GPIO.output(PIN_NUMBER,GPIO.LOW)
	# Wait a bit
	time.sleep(0.02)	
	# Receive Data
	GPIO.setup(PIN_NUMBER, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
	# Data format: 8bit integral RH data + 8bit decimal RH data + 8bit integral T data + 8bit decimal T data + 8bit check sum
	for i in range(0,500):
    		data.append(GPIO.input(PIN_NUMBER))
	return data

# GPIO.cleanup()

def getDecVal(PIN_NUMBER):
	stream_bin = getBinaryValues(PIN_NUMBER)
	values = {"RH-int":stream_bin[0:8],"RH-dec":stream_bin[8:16],"Temp-int":stream_bin[16:24],"Temp-dec":stream_bin[24:32],"ChckSum":stream_bin[32:40]}
	return values



def getStream(PINNUMBER):
    data = []
    GPIO.setup(PIN_NUMBER,GPIO.OUT)
    GPIO.output(PIN_NUMBER,GPIO.HIGH)
    time.sleep(0.025)
    GPIO.output(PIN_NUMBER,GPIO.LOW)
    time.sleep(0.02)
    GPIO.setup(PIN_NUMBER, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    for i in range(40):
        bit = GPIO.input(PIN_NUMBER)
        data.append(bit)
        if bit == 1:
            time.sleep(0.07)
        else:
            time.sleep(0.05)
    return data

