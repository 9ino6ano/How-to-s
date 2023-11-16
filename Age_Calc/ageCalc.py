from tkinter import *
from datetime import date
root =Tk()
root.geometry("800x600")
root.resizable(False,False)
root.title("Age Calculator")

photo=PhotoImage(file="Age calculator  .png")
myimage=Label(image=photo)
myimage.pack(padx=15,pady=15)

def calculateAge():
    today=date.today()
    birthdate=date(int(yearEntry.get()),int(monEntry.get()),int(dayEntry.get()))
    age=today.year - birthdate.year - ((today.month,today.day)<(birthdate.month,birthdate.day))
    Label(text=f"{fullnameValue.get()}, Your Age Is {age}",font=30).place(x=300,y=500)


Label(text="Full_Name",font=23).place(x=200,y=250)
Label(text="Year",font=23).place(x=200,y=300)
Label(text="Month",font=23).place(x=200,y=350)
Label(text="Date",font=23).place(x=200,y=400)

fullnameValue=StringVar()
yearValue=StringVar()
monValue=StringVar()
dayValue=StringVar()

nameEntry=Entry(root, textvariable=fullnameValue,width=30,bd=3,font=20)
nameEntry.place(x=300,y=250)
yearEntry=Entry(root, textvariable=yearValue,width=30,bd=3,font=20)
yearEntry.place(x=300,y=300)
monEntry=Entry(root, textvariable=monValue,width=30,bd=3,font=20)
monEntry.place(x=300,y=350)
dayEntry=Entry(root, textvariable=dayValue,width=30,bd=3,font=20)
dayEntry.place(x=300,y=400)

Button(text="Calculate",font=20,bg="black",fg="white",width=11,height=2,command=calculateAge).place(x=350,y=450)

root.mainloop()