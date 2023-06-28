# -*- coding: utf8 -*-
import tkinter as tk
import RPi.GPIO as GPIO
import time

#macro
button50 = 24
button100 = 23

#settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(button100,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button50,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def button():
    label = tk.Label(root, text="Tkinterのテストです1")
    root.update()
    sum = 0
    while True:
        btn100 = GPIO.input(button100)
        btn50 = GPIO.input(button50)

        if sum >= 150:
            print("you input"+ str(sum) +"yen")
            break
        if btn100 == True:
            print("pushed 100yen")
            sum += 100

            label.config(text="you input"+str(sum)+"yen")
            label.update()
            time.sleep(1)
            continue
        if btn50 == True:
            print("pushed 50yen")
            sum += 50

            label.config(text="you input"+str(sum)+"yen")
            label.update()
            time.sleep(1)
            continue
    time.sleep(1)
    GPIO.cleanup()
    return sum

print("push button")

root = tk.Tk()
root.geometry("320x240")
#Label部品を作る
label = tk.Label(root, text="Tkinterのテストです")
#表示する
label.grid()
button()

root.mainloop()
