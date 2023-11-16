from tkinter import *
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
import os

#Initializing tk
root=Tk()
root.geometry("630x700+400+100")
root.title("PDF Viewer")
root.configure(bg="white")

#Main part of program


def browse_files():
    file_name=filedialog.askopenfilename(initialdir=os.getcwd(),
                                         title="Select PDF file",
                                         filetypes=(("PDF File",".pdf"),
                                                    ("PDF File",".PDF"),
                                                    "All Files",".txt"))
    v1=pdf.ShowPdf()
    v2=v1.pdf_view(root,pdf_location=open(file_name,"r"),width=77,height=100)
    v2.pack(pady=(0,0))


Button(root,text="open",command=browse_files,width=40,
        font="arial 20",bd=4).pack()


root.mainloop()