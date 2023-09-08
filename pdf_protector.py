from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
#pip install PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader   
import os

root=Tk()
root.title("Pdf Protector")
root.geometry("600x430+300+100")
root.resizable(False,False)


def browse():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",filetype=(('PDF File','*.pdf'),('all files','*.*')))

    entry1.insert(END,filename)


def Protect():
    mainfile=source.get()
    protectfile = target.get()
    code = password.get()

    if mainfile=="" and protectfile=="" and password.get()=="":
        messagebox.showerror("Invalid", "All entries are empty!!")

    elif mainfile=="":
        messagebox.showerror("Invalid","Please Type Source PDF Filename")

    elif protectfile=="":
        messagebox.showerror("Invalid","Please Type Target PDF Filename!!")

    elif password.get() == "":
        messagebox.showerror("Invalid","Please Type Password")

    else:
        try:
            out=PdfFileWriter()
            file = PdfFileReader(filename)
            num = file.numPages

            for idx in range(num):
                page=file.getPage(idx)
                out.addPage(page)

            #password
            out.encrypt(code)

            with open(protectfile, "wb") as f:
                out.write(f)

            source.set("")
            target.set("")
            password.set("")

            messagebox.showinfo("info","Successfully done!!")


        except:
            messagebox.showerror("Invalid","Invalid Entry!!")
#icons
image_icon= PhotoImage(file="Images/icon.png")
root.iconphoto(False,image_icon)

#main picture of the app
Top_image=PhotoImage(file="Images/main_image.png")
Label(root,image=Top_image).pack()


frame = Frame(root,width=580,height=290,bd=5,relief=GROOVE)
frame.place(x=10,y=130)

############################################################
source = StringVar()
Label(frame,text="Source PDF File:", font="arial 10 bold",fg="#4c4541").place(x=30,y=50)
entry1=Entry(frame,width=30,textvariable=source,font="arial 15", bd=1)
entry1.place(x=150,y=48)

Button_icon=PhotoImage(file="Images/button.png")
Button(frame,image=Button_icon,width=35,height=24,bg='#d3cdcd',command=browse).place(x=500,y=47)

############################################################
target = StringVar()
Label(frame,text="Target PDF File:", font="arial 10 bold",fg="#4c4541").place(x=30,y=100)
entry2=Entry(frame,width=30,textvariable=target,font="arial 15", bd=1)
entry2.place(x=150,y=100)

############################################################
password = StringVar()
Label(frame,text="Set User Password:", font="arial 10 bold",fg="#4c4541").place(x=15,y=150)
entry3=Entry(frame,width=30,textvariable=password,font="arial 15", bd=1)
entry3.place(x=150,y=150)

button_icon = PhotoImage(file="Images/button image.png")
Protect = Button(root,text="Protect PDF File",compound=LEFT,image=button_icon,width=230,height=50,bg="#bfb9b9", font="arial 14 bold",command=Protect)
Protect.pack(side=BOTTOM,pady=40)


root.mainloop()

