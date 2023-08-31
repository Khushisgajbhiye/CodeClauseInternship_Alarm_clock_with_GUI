from tkinter import *
import datetime
import time
import winsound



def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        
        if now == set_alarm_timer:
            print("WAKE UP")
            winsound.PlaySound("Alarm.wav",winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title("Alarm Clock")
clock.geometry("500x300")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="purple",bg="black",font="Helvetica").place(x=80,y=140)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 200)
setYourAlarm = Label(clock,text = "Set Alarm Time",fg="red",relief = "solid",font=("Helevetica",12,"bold")).place(x=50, y=30)


hour = StringVar()
min = StringVar()
sec = StringVar()


hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=200,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=240,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=290,y=30)


submit = Button(clock,text = "Set Alarm",fg="cyan",width = 18,command = actual_time).place(x =240,y=90)

clock.mainloop()


