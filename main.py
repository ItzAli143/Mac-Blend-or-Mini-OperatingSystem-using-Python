# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox
import tkinter as tk
from tkinter import filedialog
import platform
import psutil

# brightness
import screen_brightness_control as pct
# audio
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
# weather
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
# clock
from time import strftime
# calender
from tkcalendar import *
# open google
import pyautogui
import subprocess
import webbrowser as wb
import random
##########################################
root = Tk()
root.title('Mac-Blend Tool')
root.geometry("1400x800+300+110")
root.resizable(False,False)
root.configure(bg="#292e2e")     # dark grayish green color

# icon
image_icon=PhotoImage(file="image/icon.png")
root.iconphoto(False,image_icon)

Body=Frame(root,width=1350,height=900,bg="#d6d6d6")  # d6d6d6(light gray)
Body.pack(pady=20,padx=20)
#--------------------------------------------------
LHS=Frame(Body,width=500,height=740,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)  # #f4f5f5(off-white) #adacb1(light-grayish-blue)
LHS.place(x=10,y=10)

# logo
photo=PhotoImage(file="image/laptop.png")
myimage=Label(LHS,image=photo,background=("#f4f5f5"))   # #f4f5f5(off-white)
myimage.place(x=90,y=50)

my_system= platform.uname()

l1=Label(LHS, text="Hajvery Tech Knowledge",bg="#f4f5f5",font=("Acumin Variable Concept",20,'bold'),justify="center")
l1.place(x=50,y=250)
l2=Label(LHS, text=f"Version:{my_system.version}",bg="#f4f5f5",font=("Acumin Variable Concept",10,'bold'),justify="center")
l2.place(x=50,y=400)
l3=Label(LHS, text=f"System:{my_system.system}",bg="#f4f5f5",font=("Acumin Variable Concept",15,'bold'),justify="center")
l3.place(x=50,y=450)
l4=Label(LHS, text=f"Machine:{my_system.machine}",bg="#f4f5f5",font=("Acumin Variable Concept",15,'bold'),justify="center")
l4.place(x=50,y=500)
l5=Label(LHS, text=f"Total RAM Installed:  {round(psutil.virtual_memory().total//1000000000)} GB",bg="#f4f5f5",font=("Acumin Variable Concept",15,'bold'),justify="center")
l5.place(x=50,y=550)
l6=Label(LHS, text=f"Pro:{my_system.processor}",bg="#f4f5f5",font=("Acumin Variable Concept",10,"bold"),justify="center")
l6.place(x=50,y=600)
#--------------------------------------------------
RHS=Frame(Body,width=815,height=350,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)  # #f4f5f5(off-white) #adacb1(light-grayish-blue)
RHS.place(x=520,y=10)

system=Label(RHS, text='System',font=("Acumin Variable Concept",15,'bold'),bg="#f4f5f5")    # #f4f5f5(off-white)
system.place(x=10,y=10)
# ########################## Battery ################################
def convertTime(seconds):
    minutes,seconds=divmod(seconds,60)
    hours,minutes=divmod(minutes,60)
    return "%d:%02d:%02d"% (hours,minutes,seconds)
def none():
    global battery_png
    global battery_label
    battery=psutil.sensors_battery()
    percent=battery.percent
    time=convertTime(battery.secsleft)
    lbl.config(text=f"{percent}%")
    lbl_plug.config(text=f"Plug in:{str(battery.power_plugged)}")
    lbl_time.config(text=f"{time} remaining")

    battary_label=Label(RHS,background='#f4f5f5')
    battary_label.place(x=40,y=70)

    lbl.after(1000,none)

    if battery.power_plugged==True:
        battery_png=PhotoImage(file="image/charging.png")
        battary_label.config(image=battery_png)
    else:
        battery_png=PhotoImage(file='image/battery.png')
        battary_label.config(image=battery_png)

lbl=Label(RHS,font=("Acumin Variable Concept",60,'bold'),bg='#f4f5f5')    # #f4f5f5(off-white)
lbl.place(x=400,y=70)

lbl_plug=Label(RHS,font=("Acumin Variable Concept",10,'bold'),bg='#f4f5f5')    # #f4f5f5(off-white)
lbl_plug.place(x=50,y=150)

lbl_time=Label(RHS,font=("Acumin Variable Concept",20,'bold'),bg='#f4f5f5')    # #f4f5f5(off-white)
lbl_time.place(x=400,y=220)
none()
#####################################################################
######################### speaker####################################
lbl_speaker=Label(RHS,text="Speaker:",font=('arial',10,'bold'),bg="#f4f5f5")
lbl_speaker.place(x=50,y=200)
volume_value=tk.DoubleVar()
def get_current_volume_value():
    return '{: .2f}' .format(volume_value.get())
def volume_changed(event):
    device=AudioUtilities.GetSpeakers()
    interface=device.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(-float(get_current_volume_value()),None)
style= ttk.Style()
style.configure("TScale",background='#f4f5f5')

volume=ttk.Scale(RHS,from_=60,to=0,orient='horizontal',command=volume_changed,variable=volume_value)
volume.place(x=150,y=200)
volume.set(20)
#####################################################################
######################## Brightness #################################
lbl_brightness=Label(RHS, text='Brightness',font=('arial',10,'bold'),bg="#f4f5f5")
lbl_brightness.place(x=50,y=250)

current_value=tk.DoubleVar()
def get_current_value():
    return '{: .2f}'.format(current_value.get())
def brightness_changed(event):
    pct.set_brightness(get_current_value())

brightness= ttk.Scale(RHS,from_=0,to=100,orient='horizontal',command=brightness_changed,variable=current_value)
brightness.place(x=150,y=250)
#####################################################################
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#####################################################################
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def weather():
    app1 =Toplevel()
    app1.geometry('1400x850+300+110')
    app1.title('Weather')
    app1.configure(bg='#f4f5f5')
    app1.resizable(False, False)
    # icon
    image_icon = PhotoImage(file='image/App1.png')
    app1.iconphoto(False, image_icon)

    def getWeather():
        try:
            city = textfield.get()
            geolocator = Nominatim(user_agent="geoapiExercises")
            location = geolocator.geocode(city)
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

            home = pytz.timezone(result)
            local_time = datetime.now(home)
            current_time = local_time.strftime("%I:%M %p")
            clock.config(text=current_time)
            name.config(text="CURRENT WEATHER")

            # weather
            api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=646824f2b7b86caffec1d0b16ea77f79"
            json_data = requests.get(api).json()
            condition = json_data['weather'][0]['main']
            description = json_data['weather'][0]['description']
            temp = int(json_data['main']['temp'] - 273.15)
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            wind = json_data['wind']['speed']

            t.config(text=(temp, "°"))
            c.config(text=(condition, "|", "Feels", "LIKE", temp, '°'))
            w.config(text=wind)
            h.config(text=humidity)
            d.config(text=description)
            p.config(text=pressure)

        except Exception as e:
            messagebox.showerror("Weather App", "Invalid Entry!")

        # search box

    Search_image = PhotoImage(file='image/search1.png')
    myimage = Label(app1, image=Search_image, bg="#f4f5f5")
    myimage.place(x=700, y=20)
    textfield = tk.Entry(app1, justify='center', width=17, font=('poppins', 25, 'bold'), bg='#404040', border=0,
                         fg="white")
    textfield.place(x=750, y=40)
    textfield.focus()

    Search_icon = PhotoImage(file="image/search_icon.png")
    myimage_icon = Button(app1, image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
    myimage_icon.place(x=1170, y=39)
    # logo
    Logo_image = PhotoImage(file="image/logo1.png")
    logo = Label(app1, image=Logo_image, bg="#f4f5f5")
    logo.place(x=200, y=250)
    # bottom box
    Frame_image = PhotoImage(file="image/box11.png")
    frame_myimage = Label(app1, image=Frame_image, bg="#f4f5f5")
    frame_myimage.pack(padx=10, pady=10, side=BOTTOM)
    # time
    name = Label(app1, font=('arial', 20, 'bold'), bg="#f4f5f5")
    name.place(x=30, y=30)
    clock = Label(app1, font=("Helvatica", 40), bg="#f4f5f5")
    clock.place(x=30, y=80)
    # label
    # @@@@@@@@@@@@@@@@@@@@@@@
    label11 = Label(app1, text="*) This application needs strong internet connection to work properly.",
                    font=("Helvatica", 10), fg="black", bg="#f4f5f5")
    label11.place(x=730, y=120)
    label11 = Label(app1, text="*) Use Comma to seperate city and country without space.", font=("Helvatica", 10),
                    fg="black", bg="#f4f5f5")
    label11.place(x=730, y=145)
    # @@@@@@@@@@@@@@@@@@@@@@@
    label1 = Label(app1, text="WIND", font=("Helvatica", 15, 'bold'), fg="white", bg="#1ab5ef")  # (#1ab5ef) blue shade
    label1.place(x=290, y=735)
    label2 = Label(app1, text="HUMIDITY", font=("Helvatica", 15, 'bold'), fg="white", bg="#1ab5ef")
    label2.place(x=460, y=735)
    label3 = Label(app1, text="DESCRIPTION", font=("Helvatica", 15, 'bold'), fg="white", bg="#1ab5ef")
    label3.place(x=650, y=735)
    label4 = Label(app1, text="PRESSURE", font=("Helvatica", 15, 'bold'), fg="white", bg="#1ab5ef")
    label4.place(x=920, y=735)
    t = Label(app1, font=('arial', 100), fg="#ee666d", bg='#f4f5f5')
    t.place(x=700, y=280)
    c = Label(app1, font=('arial', 20, 'bold'), bg='#f4f5f5')
    c.place(x=700, y=480)
    w = Label(app1, text="...", font=('arial', 15, 'bold'), bg="#1ab5ef")
    w.place(x=290, y=765)
    h = Label(app1, text="...", font=('arial', 15, 'bold'), bg="#1ab5ef")
    h.place(x=460, y=765)
    d = Label(app1, text="...", font=('arial', 15, 'bold'), bg="#1ab5ef")
    d.place(x=650, y=765)
    p = Label(app1, text="...", font=('arial', 15, 'bold'), bg="#1ab5ef")
    p.place(x=930, y=765)
    app1.mainloop()
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def clock():
    app2=Toplevel()
    app2.geometry("1400x110+300+10")
    app2.title('Clock')
    app2.configure(bg="#292e2e")
    app2.resizable(False,False)

    # icon
    image_icon=PhotoImage(file="image/App2.png")
    app2.iconphoto(False,image_icon)

    def clock():
        text=strftime('%H:%M:%S %p')
        lbl.config(text=text)
        lbl.after(1000,clock)

    lbl=Label(app2,font=('digital-7',50,'bold'),width=26,bg="#f4f5f5",fg="#292e2e")
    lbl.pack(anchor='center',pady=15)
    clock()

    app2.mainloop()
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def calendar():
    app3=Toplevel()
    app3.geometry("1400x800+300+110")
    app3.title('Calender')
    app3.configure(bg="#dee2e5")
    app3.resizable(False, False)
    bgimg = PhotoImage(file="image/background2.png")
    limg = Label(app3, i=bgimg)
    limg.pack()

    # icon
    image_icon=PhotoImage(file="image/App3.png")
    app3.iconphoto(False,image_icon)
    label1 = Label(app3, text="Calender",
                    font=("Helvatica", 38,'bold'), fg="#ee666d", bg="#f4f5f5")
    label1.place(x=200, y=100)

    # Create Label for displaying selected Date
    lbl = Label(app3, text="")
    lbl.place(x=305,y=550)

    mycal=Calendar(app3,setmode='day',date_pattern='d/m/yy')
    mycal.place(x=200,y=250)

    # Define Function to select the date
    def get_date():
        lbl.config(text=mycal.get_date())

    # Create a button to pick the date from the calendar
    button = Button(app3, text="Select the Date", command=get_date)
    button.place(x=285,y=500)

    app3.mainloop()
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
button_mode=True
def mode():
    global button_mode
    if button_mode:
        LHS.config(bg="#292e2e")
        myimage.config(bg="#292e2e")
        l1.config(bg="#292e2e",fg="#d6d6d6")
        l2.config(bg="#292e2e", fg="#d6d6d6")
        l3.config(bg="#292e2e", fg="#d6d6d6")
        l4.config(bg="#292e2e", fg="#d6d6d6")
        l5.config(bg="#292e2e", fg="#d6d6d6")
        l6.config(bg="#292e2e", fg="#d6d6d6")

        RHB.config(bg="#292e2e")
        app1.config(bg="#292e2e")
        app2.config(bg="#292e2e")
        app3.config(bg="#292e2e")
        app4.config(bg="#292e2e")
        app5.config(bg="#292e2e")
        app6.config(bg="#292e2e")
        app7.config(bg="#292e2e")
        app8.config(bg="#292e2e")
        app9.config(bg="#292e2e")
        app10.config(bg="#292e2e")
        apps.config(bg="#292e2e",fg="#d6d6d6")

        button_mode=False
    else:
        LHS.config(bg="#f4f5f5")
        myimage.config(bg="#f4f5f5")
        l1.config(bg="#f4f5f5",fg="#292e2e")
        l2.config(bg="#f4f5f5", fg="#292e2e")
        l3.config(bg="#f4f5f5", fg="#292e2e")
        l4.config(bg="#f4f5f5", fg="#292e2e")
        l5.config(bg="#f4f5f5", fg="#292e2e")
        l6.config(bg="#f4f5f5", fg="#292e2e")

        RHB.config(bg="#f4f5f5")
        app1.config(bg="#f4f5f5")
        app2.config(bg="#f4f5f5")
        app3.config(bg="#f4f5f5")
        app4.config(bg="#f4f5f5")
        app5.config(bg="#f4f5f5")
        app6.config(bg="#f4f5f5")
        app7.config(bg="#f4f5f5")
        app8.config(bg="#f4f5f5")
        app9.config(bg="#f4f5f5")
        app10.config(bg="#f4f5f5")
        apps.config(bg="#f4f5f5",fg="#292e2e")
        button_mode=True
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def game():
    app5=Toplevel()
    app5.geometry("1400x850+300+110")
    app5.title("Ludo Game")
    app5.configure(bg="#dee2e5") # grayish-blue color
    app5.resizable(False,False)
    bgimg = PhotoImage(file="image/ludo2.png")
    limg = Label(app5, i=bgimg)
    limg.pack()

    # icons
    image_icon=PhotoImage(file='image/App5.png')
    app5.iconphoto(False,image_icon)

    ludo_image=PhotoImage(file="image/ludo back.png")
    Label(app5,image=ludo_image).place(x=200,y=100)

    label=Label(app5,text='',font=("time",150))
    def roll():
        dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        label.configure(text=f'{random.choice(dice)}{random.choice(dice)}', fg="#29232e")
        label.place(x=170,y=420)
    btn_image=PhotoImage(file="image/ludo button.png")
    btn=Button(app5,image=btn_image,bg="#dee2e5",command=roll)
    btn.place(x=240,y=330)
    app5.mainloop()
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def screenshot():
    root.iconify()
    myScreenshot=pyautogui.screenshot()
    file_path=filedialog.asksaveasfilename(defaultextension='.png')
    myScreenshot.save(file_path)
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def file():
    subprocess.Popen(r'explorer /select,"E:\BS-AI 4rth Semester\Programming for AI\pythonProject1\Hajvary_OS"')
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def chrome():
    wb.register('chrome',None)
    wb.open("https://www.google.com/")
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def close_apps():
    wb.register('chrome', None)
    wb.open("https://www.youtube.com/")
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def close_window():
    root.destroy()
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#--------------------------------------------------
RHB=Frame(Body,width=815,height=380,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)  # #f4f5f5(off-white) #adacb1(light-grayish-blue)
RHB.place(x=520,y=370)

apps=Label(RHB,text='Apps',font=("Acumin Variable Concept",15,'bold'),bg='#f4f5f5')
apps.place(x=10,y=10)

app1_image=PhotoImage(file='image/App1.png')
app1=Button(RHB,image=app1_image,bd=0,command=weather)
app1.place(x=40,y=60)

apps1=Label(RHB,text='Weather',font=("Acumin Variable Concept",10),bg='#f4f5f5')
apps1.place(x=35,y=120)

app2_image=PhotoImage(file='image/App2.png')
app2=Button(RHB,image=app2_image,bd=0,command=clock)
app2.place(x=220,y=60)

apps2=Label(RHB,text='Clock',font=("Acumin Variable Concept",10),bg='#f4f5f5')
apps2.place(x=225,y=120)

app3_image=PhotoImage(file='image/App3.png')
app3=Button(RHB,image=app3_image,bd=0,command=calendar)
app3.place(x=400,y=60)

apps2=Label(RHB,text='Calendar',font=("Acumin Variable Concept",10),bg='#f4f5f5')
apps2.place(x=390,y=120)

app4_image=PhotoImage(file='image/App4.png')
app4=Button(RHB,image=app4_image,bd=0,command=mode)
app4.place(x=550,y=60)

apps2=Label(RHB,text='Dark Mode',font=("Acumin Variable Concept",10),bg='#f4f5f5')
apps2.place(x=540,y=120)

app5_image=PhotoImage(file='image/App5.png')
app5=Button(RHB,image=app5_image,bd=0,command=game)
app5.place(x=700,y=60)

apps2=Label(RHB,text='Ludo',font=("Acumin Variable Concept",10),bg='#f4f5f5')
apps2.place(x=705,y=120)

app6_image=PhotoImage(file='image/App6.png')
app6=Button(RHB,image=app6_image,bd=0,command=screenshot)
app6.place(x=40,y=200)

apps6=Label(RHB,text='ScreenShot',font=("Acumin Variable Concept",10),bg='#f4f5f5')
apps6.place(x=30,y=270)

app7_image=PhotoImage(file='image/App7.png')
app7=Button(RHB,image=app7_image,bd=0,command=file)
app7.place(x=220,y=200)

apps7=Label(RHB,text='Files',font=("Acumin Variable Concept",10),bg='#f4f5f5')
apps7.place(x=230,y=270)

app8_image=PhotoImage(file='image/App8.png')
app8=Button(RHB,image=app8_image,bd=0,command=chrome)
app8.place(x=400,y=200)

apps8=Label(RHB,text='Google',font=("Acumin Variable Concept",10),bg='#f4f5f5')
apps8.place(x=400,y=270)

app9_image=PhotoImage(file='image/App9.png')
app9=Button(RHB,image=app9_image,bd=0,command=close_apps)
app9.place(x=550,y=190)

apps9=Label(RHB,text='YouTube',font=("Acumin Variable Concept",10),bg='#f4f5f5')
apps9.place(x=550,y=270)

app10_image=PhotoImage(file='image/App10.png')
app10=Button(RHB,image=app10_image,bd=0,command=close_window)
app10.place(x=700,y=200)

apps10=Label(RHB,text='Close Windows',font=("Acumin Variable Concept",10),bg='#f4f5f5')
apps10.place(x=670,y=270)

root.mainloop()