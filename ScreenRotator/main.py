from tkinter import *
import rotatescreen

def Screen_rotation(enter):
    screen=rotatescreen.get_primary_display()

    if enter =="up":
        screen.set_landscape()
    elif enter == "right":
        screen.set_portrait_flipped()
    elif enter == "down":
        screen.set_landscape_flipped()
    elif enter == "left":
        screen.set_portrait()


root=Tk()
root.geometry("500x500")
root.title("Screen Rotation")
root.configure(bg="#54c5d1")

#adding the background image
photo=PhotoImage(file="background.png")
myImage=Label(image=photo)
myImage.pack(padx=2,pady=2)
#creating buttons
Button(root,text="Up",command=lambda:Screen_rotation("up"),bg="white",font="arial 18",width=5).place(x=200,y=50)
Button(root,text="right",command=lambda:Screen_rotation("right"),bg="white",font="arial 18",width=5).place(x=20,y=230)
Button(root,text="left",command=lambda:Screen_rotation("left"),bg="white",font="arial 18",width=5).place(x=410,y=230)
Button(root,text="down",command=lambda:Screen_rotation("down"),bg="white",font="arial 18",width=5).place(x=230,y=400)


root.mainloop()