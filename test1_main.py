# -*- coding: utf8 -*-
import tkinter as tk
import RPi.GPIO as GPIO
import time

import json
import pigpio
import test0_IR as IR
import test0_senser as senser

# detabase
import dbshow
import dbchange

#button
button50 = 24
button100 = 23

# led
led = 3

# IR
IR_RX_PIN = 25
GLITCH = 100
PRE_MS = 200
POST_MS = 15
FREQ = 38.0
SHORT = 10
TOLERANCE = 15

POST_US = POST_MS * 1000
PRE_US = PRE_MS * 1000
TOLER_MIN = (100 - TOLERANCE) / 100.0
TOLER_MAX = (100 + TOLERANCE) / 100.0

last_tick = 0
in_code = False
code = []
fetching_code = False

#settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(button100,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button50,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(led,GPIO.OUT,initial=GPIO.LOW)




def button():
    #label.config(text="tkのテストです1")
    window.update()
    sum = 0
    while True:
        btn100 = GPIO.input(button100)
        btn50 = GPIO.input(button50)

        if sum >= 150:
            print(str(sum) +"円投入しました")
            break
        if btn100 == True:
            print("pushed 100yen")
            sum += 100

            label.config(text=str(sum)+"円投入しました")
            label.update()
            time.sleep(1)
            continue
        if btn50 == True:
            print("pushed 50yen")
            sum += 50

            label.config(text=str(sum)+"円投入しました")
            label.update()
            time.sleep(1)
            continue
    time.sleep(1)
    GPIO.cleanup()
    return sum


def normalise(c):
        entries = len(c)
        p = [0] * entries  # Set all entries not processed.
        for i in range(entries):
            if not p[i]:  # Not processed?
                v = c[i]
                tot = v
                similar = 1.0

                # Find all pulses with similar lengths to the start pulse.
                for j in range(i + 2, entries, 2):
                    if not p[j]:  # Unprocessed.
                        if (c[j] * TOLER_MIN) < v < (c[j] * TOLER_MAX):  # Similar.
                            tot = tot + c[j]
                            similar += 1.0

                # Calculate the average pulse length.
                newv = round(tot / similar, 2)
                c[i] = newv

                # Set all similar pulses to the average value.
                for j in range(i + 2, entries, 2):
                    if not p[j]:  # Unprocessed.
                        if (c[j] * TOLER_MIN) < v < (c[j] * TOLER_MAX):  # Similar.
                            c[j] = newv
                            p[j] = 1

def compare(p1, p2):
        if len(p1) != len(p2):
            return False

        for i in range(len(p1)):
            v = p1[i] / p2[i]
            if (v < TOLER_MIN) or (v > TOLER_MAX):
                return False

        for i in range(len(p1)):
            p1[i] = int(round((p1[i] + p2[i]) / 2.0))

        return True

def end_of_code():
        global code, fetching_code
        if len(code) > SHORT:
            normalise(code)
            fetching_code = False
        else:
            code = []
            print("Short code, probably a repeat, try again")

def cbf(gpio, level, tick):
        global last_tick, in_code, code, fetching_code

        if level != pigpio.TIMEOUT:
            edge = pigpio.tickDiff(last_tick, tick)
            last_tick = tick

            if fetching_code:
                if (edge > PRE_US) and (not in_code):  # Start of a code.
                    in_code = True
                    pi.set_watchdog(IR_RX_PIN, POST_MS)  # Start watchdog.

                elif (edge > POST_US) and in_code:  # End of a code.
                    in_code = False
                    pi.set_watchdog(IR_RX_PIN, 0)  # Cancel watchdog.
                    end_of_code()

                elif in_code:
                    code.append(edge)
        else:
            pi.set_watchdog(IR_RX_PIN, 0)  # Cancel watchdog.
            if in_code:
                in_code = False
                end_of_code()

pi = pigpio.pi()  # Connect to Pi.

if not pi.connected:
    exit(0)
# i=0
# while(1):
#     if(int(i)==1):
#         break
#     else:
#         i = input("input 1")
check =0
while(check == 0):
    check = senser.detct()

print("push button")

version = tk.Tcl().eval('info patchlevel')
window = tk.Tk()
window.geometry("500x600")
window.title("画像表示：" )

a = dbshow.show()

# キャンバス作成
canvas = tk.Canvas(window, bg="#deb887", height=200, width=200)
canvas2 = tk.Canvas(window, bg="#000000", height=200, width=200)
label_1 = tk.Label(window,text=a[0][1])
label_1_value = tk.Label(window, text=str(a[0][3])+"円")
label_2 = tk.Label(window,text=a[1][1])
label_2_value = tk.Label(window, text=str(a[1][3])+"円")

canvas3 = tk.Canvas(window, bg="#deb887", height=200, width=200)
canvas4 = tk.Canvas(window, bg="#000000", height=200, width=200)
label_3 = tk.Label(window,text=a[2][1])
label_3_value = tk.Label(window, text=str(a[2][3])+"円")
label_4 = tk.Label(window,text=a[3][1])
label_4_value = tk.Label(window, text=str(a[3][3])+"円")
# キャンバス表示
canvas.place(x=0, y=0)
canvas2.place(x=300,y=0)
label_1.place(x=70, y=210)
label_1_value.place(x=70, y=230)
label_2.place(x=370, y=210)
label_2_value.place(x=370, y=230)
canvas3.place(x=0, y=300)
canvas4.place(x=300,y=300)
label_3.place(x=70, y=510)
label_3_value.place(x=70, y=530)
label_4.place(x=370, y=510)
label_4_value.place(x=370, y=530)


# イメージ作成
img = tk.PhotoImage(file="apple.png", width=200, height=200)
img2= tk.PhotoImage(file="orange.png", width=200, height=200)
img3= tk.PhotoImage(file="banana.png", width=200, height=200)
img4= tk.PhotoImage(file="melon.png", width=200, height=200)
# キャンバスにイメージを表示
canvas.create_image(2, 2, image=img, anchor=tk.NW)
canvas2.create_image(2,2, image=img2, anchor=tk.NW)
canvas3.create_image(2, 2, image=img3, anchor=tk.NW)
canvas4.create_image(2,2, image=img4, anchor=tk.NW)


#Label部品を作る
label = tk.Label(window, text="お金を投入してください")
#表示する
label.place(x=0,y=550)
money = button()
print("finish button")

# IR maint------------------------------------------------------------------
with open('car_mp3') as f:
        key_config = json.load(f)

        pi.set_mode(IR_RX_PIN, pigpio.INPUT)  # IR RX connected to this IR_RX_PIN.

        pi.set_glitch_filter(IR_RX_PIN, GLITCH)  # Ignore glitches.

        cb = pi.callback(IR_RX_PIN, pigpio.EITHER_EDGE, cbf)

        try:
            while True:
                code = []
                fetching_code = True
                while fetching_code:
                    # print("stack")
                    time.sleep(0.1)
                time.sleep(0.5)
                key_name = "-"
                for key, val in key_config.items():
                    if compare(val, code[:]):
                        key_name = key
                if key_name == "b0":
                    # ALL -> ON
                    print("0")
                    num = 0
                    break
                elif key_name == "b1":
                    # GREEN -> ON, OTHER -> OFF
                    print("1")
                    num = 1
                    break
                elif key_name == "b2":
                    # YELLOW -> ON, OTHER -> OFF
                    print("2")
                    num = 2
                    break
                elif key_name == "b3":
                    # RED -> ON, OTHER -> OFF
                    print("3")
                    num = 3
                    break
                else:
                    # ALL -> OFF
                    # print("other")
                    continue

        except KeyboardInterrupt:
            pass
        finally:
            pi.stop()
# -------------------------------------------------------------------

result = dbchange.change(num,money)

if(result == False):
    label.config(text="投入金額が足りません")
    label.update()
else:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led,GPIO.OUT,initial=GPIO.LOW)
    GPIO.output(led,1)
    time.sleep(3)


# num = IR.test0_IR()
# print(num)
window.mainloop()
