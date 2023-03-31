# Custom Tkinter Modern GUI
# pyinstaller -w --icon=icon.ico --exclude numpy --hiddenimport win32timezone --hidden-import plyer.platforms.win.notification main.py

import time
from tkinter import *
import  customtkinter as ctk
from PIL import ImageTk, Image
from tkinter import font

# Main Window 세팅
ctk.set_appearance_mode('dark')
window = ctk.CTk()
window.iconbitmap('instagram.ico')
window.title('Tkinter Modern GUI')
window.geometry('1000x600+500+500')
window.resizable(False,False)

def close_window():
    from plyer import notification

    notification.notify(
        title="title",
        message="Message",
        app_name="app_name",
        # app_icon="./icon.ico",
        timeout=15,
    )
    window.destroy()

def fileOpen():

    from tkinter import filedialog
    import os
    import tkinter
    root = tkinter.Tk()
    root.wm_withdraw() #this completely hides the root window
    filename = filedialog.askopenfilename(title="원하는 파일을 선택하세요",filetypes=(("txt file","*.txt;*.csv"),("all files","*.*")))
    root.destroy()

    listbox.insert(END,f'파일경로 : {filename}')

def test_tread():
    import threading
    t1 = threading.Thread(target=test)
    t1.start()

def test():
    for i in range(100):
        listbox.insert(END,f"테스트 {i}번째")
        listbox.itemconfig(END, {'fg':'blue'})
        listbox.see(END)
        time.sleep(0.3)

# 이미지 있는 버튼
img1 = ImageTk.PhotoImage(Image.open('home.png').resize((25,25)))
btn = ctk.CTkButton(window, text="button", command=test_tread, compound='left', image=img1,width=150,height=50,font=('default',15,'bold'),corner_radius=10)
btn.place(x=100,y=100)

img1 = ImageTk.PhotoImage(Image.open('home.png').resize((25,25)))
btn = ctk.CTkButton(window, text="File Open", command=fileOpen, compound='left', image=img1,width=150,height=50,font=('default',15,'bold'),corner_radius=10)
btn.place(x=300,y=100)

img1 = ImageTk.PhotoImage(Image.open('home.png').resize((25,25)))
btn = ctk.CTkButton(window, text="Close Window", command=close_window, compound='left', image=img1,width=150,height=50,font=('default',15,'bold'),corner_radius=10)
btn.place(x=500,y=100)

# 슬라이더 버튼
sliderFrame = ctk.CTkFrame(window, fg_color='transparent')
sliderFrame.place(x=400,y=20)
slider = ctk.CTkSlider(sliderFrame)
slider.pack(padx=20,pady=20)

# 스크롤바 logging 창
bg_color = 'gray15'
ctkFrame = ctk.CTkFrame(window,width=800,height=150, corner_radius=10,fg_color= bg_color)
ctkFrame.place(x=100,y=170)
listbox = Listbox(ctkFrame,width=100,height=23,selectmode="extended")
fontStyle = font.Font(weight = 'bold', size=12)
listbox.configure(bg=bg_color,font=fontStyle,foreground='white',borderwidth=0, highlightbackground=bg_color)
listbox.pack(side='left',fill='y', padx=10, pady=10)
scrollbar = ctk.CTkScrollbar(ctkFrame)
scrollbar.configure(command=listbox.yview)
scrollbar.pack(side='right', fill='y')
listbox.config(yscrollcommand = scrollbar.set)

#Input Box
entry = ctk.CTkEntry(window,placeholder_text='placeholder')
entry.place(x=100 , y=50)

#스위치형 버튼
switch = ctk.CTkSwitch(window,text='Switch Button', progress_color='pink')
switch.place(x=100, y=10)

# window start
window.mainloop()