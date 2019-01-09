import RPi.GPIO as GPIO ## Import GPIO Library
import time ## Import 'time' library.  Allows us to use 'sleep'

## Define function named Blink()
def Blink(numTimes, speed):
    GPIO.setmode(GPIO.BCM) ## Use BOARD pin numbering
    n_pin = 4
    GPIO.setup(n_pin, GPIO.OUT) ## Setup GPIO pin 4 to OUT
    for i in range(0,numTimes): ## Run loop numTimes
        print "Iteration " + str(i+1) ##Print current loop
        GPIO.output(n_pin, True) ## Turn on GPIO pin 7
        time.sleep(speed) ## Wait
        GPIO.output(n_pin, False) ## Switch off GPIO pin 7
        time.sleep(speed) ## Wait
    print "Done" ## When loop is complete, print "Done"
    GPIO.cleanup()



def main():
    ## Prompt user for input
    iterations = raw_input("Enter the total number of times to blink: ")
    speed = raw_input("Enter the length of each blink in seconds: ")

    ## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters
    Blink(int(iterations),float(speed))
    
    

if __name__ == "__main__":
    main()
