import tkinter

# 画面作成
version = tkinter.Tcl().eval('info patchlevel')
window = tkinter.Tk()
window.geometry("500x600")
window.title("画像表示：" )

# キャンバス作成
canvas = tkinter.Canvas(window, bg="#deb887", height=200, width=200)
canvas2 = tkinter.Canvas(window, bg="#000000", height=200, width=200)
label_1 = tkinter.Label(window,text='name1')
label_1_value = tkinter.Label(window, text="yen")
label_2 = tkinter.Label(window,text='name2')
label_2_value = tkinter.Label(window, text="yen")

canvas3 = tkinter.Canvas(window, bg="#deb887", height=200, width=200)
canvas4 = tkinter.Canvas(window, bg="#000000", height=200, width=200)
label_3 = tkinter.Label(window,text='name1')
label_3_value = tkinter.Label(window, text="yen")
label_4 = tkinter.Label(window,text='name2')
label_4_value = tkinter.Label(window, text="yen")
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
img = tkinter.PhotoImage(file="apple.png", width=200, height=200)
img2= tkinter.PhotoImage(file="orange.png", width=200, height=200)
img3= tkinter.PhotoImage(file="banana.png", width=200, height=200)
img4= tkinter.PhotoImage(file="melon.png", width=200, height=200)
# キャンバスにイメージを表示
canvas.create_image(2, 2, image=img, anchor=tkinter.NW)
canvas2.create_image(2,2, image=img2, anchor=tkinter.NW)
canvas3.create_image(2, 2, image=img3, anchor=tkinter.NW)
canvas4.create_image(2,2, image=img4, anchor=tkinter.NW)

Static1 = tkinter.Label(text=u'test', foreground='#ff0000', background='#ffaacc')
Static1.place(x=0, y=550)

window.mainloop()