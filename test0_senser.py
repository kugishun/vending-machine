import RPi.GPIO as GPIO
import time

M_pin = 18 #select the pin for motionsensor

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(M_pin,GPIO.IN)

def detct():
    for i in range(101):
        if GPIO.input(M_pin):
            print("ON")
            time.sleep(2)
            return 1
        else:
            print ("OFF")
            time.sleep(2)
    time.sleep(5)
    GPIO.cleanup()

if __name__ == "__main__":
    detct()