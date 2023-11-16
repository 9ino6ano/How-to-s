from tkinter import *
from tkcalendar import *

root = Tk()


def select_date():
    myDate=myCal.get_date()
    selectedDate=Label(text=myDate)
    selectedDate.pack(padx=2,pady=2)


myCal=Calendar(root,setmode="day",date_pattern='d/mm/yy')
myCal.pack(padx=15,pady=15)

open_cal=Button(root,text="Select Date",command=select_date)
open_cal.pack(padx=15,pady=15)

root.geometry("300x300")
root.title("Calender")
root.configure(bg="lightblue")
root.mainloop()