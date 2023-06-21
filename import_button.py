#coding:utf-8
import RPi.GPIO as GPIO
import time

#macro
button50 = 24
button100 = 23

#settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(button100,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button50,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
def input_button():
    print("push button")
    sum = 0
    while True:
        btn100 = GPIO.input(button100)
        btn50 = GPIO.input(button50)

        if btn100 == True:
            print("pushed 100yen")
            sum = 100
            #time.sleep(1)
            break
        if btn50 == True:
            print("pushed 50yen")
            sum += 50
            #time.sleep(1)
            break
        time.sleep(1)

    GPIO.cleanup()
    return sum
