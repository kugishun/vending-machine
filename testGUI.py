#!/usr/bin/python3
# -*- coding: utf8 -*-
import tkinter as tk

def pushed(b):
    b["text"] = "押されたよ"
    print("test")
    root.after(1,count,0)

def count(input):
    label.config(text=input)
    input = input+1
    root.after(1,count,input)

#rootウィンドウを作成
root = tk.Tk()
#rootウィンドウのタイトルを変える
root.title("Tkinterテスト")
#rootウィンドウの大きさを320x240に
root.geometry("320x240")

#Label部品を作る
label = tk.Label(root, text="Tkinterのテストです")
#表示する
label.grid()

#ボタンを作る
button = tk.Button(root, text="ボタン", command= lambda : pushed(button))
#表示
button.grid()

#メインループ
root.mainloop()