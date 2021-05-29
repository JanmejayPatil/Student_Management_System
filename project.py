from tkinter import *
from tkinter import messagebox
from prettytable import from_db_cursor
import mysql.connector
root= Tk()
root.geometry('600x590')
root.title("SMS")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="j1"
)

def entry():
    mycursor = mydb.cursor()
    fname = txtbox_1.get()
    lname = txtbox_2.get()
    std_id = txtbox_3.get()
    dob = txtbox_4.get()
    phone = txtbox_5.get()
    email = txtbox_6.get()
    err = bool(re.findall('\S+@\S+.\S+', email))
    address = txtbox_7.get(0.0,END)
    roll_no = int(Spinbox.get(spin))
    gender = opt.get()
    if(err == True and len(phone)==10):
        j1 = "INSERT INTO student (fname, lname,std_id,gender,dob,phone,email,roll_no,address) VALUES (%s, %s,%s,%s, %s,%s,%s, %s,%s)"
        val = [
            (fname,lname,std_id,gender,dob,phone,email,roll_no,address)]
        messagebox.showinfo("Thank You","Entry Added Succesfully")
        mycursor.executemany(j1, val)
        mydb.commit()
        print(mycursor.rowcount, "was inserted.")

    elif(len(phone)!=10):
        messagebox.showerror("ERROR","Invalid Length of Phone Number")
    elif (err != True):
        messagebox.showerror("ERROR", "Invalid Email")


def disp():
    window = Tk()
    window.geometry('1200x450')
    window.title("DATA")
    window.configure(background="lavender")
    txtbox_8 = Text(window)
    txtbox_8.place(x=10, y=10, width=1100, height=300)

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM student")
    x=from_db_cursor(mycursor)
    txtbox_8.insert(INSERT, (x))

    b3 = Button(window, text='EXIT', width=20, bg='lightgrey', fg='black', command=window.destroy)
    b3.place(x=380, y=400, height=30, width=200)

def clr():
    txtbox_1.delete(0,END)
    txtbox_2.delete(0, END)
    txtbox_3.delete(0,END)
    txtbox_4.delete(0,END)
    txtbox_5.delete(0,END)
    txtbox_6.delete(0, END)
    txtbox_7.delete(0.0,END)
    opt.set("Select Gender")
    spin.delete(0, END)


label_0 = Label(root, text="STUDENT MANAGEMENT SYSTEM",relief="groove",width=29,bg='lightgrey',fg='black',font=("Bookman Old Style", 22))
label_0.place(x=30,y=30)


label_1 = Label(root, text="Enter First Name",relief="ridge",width=20,bg="lavender",fg='black',font=("bold", 12))
label_1.place(x=30,y=100)

txtbox_1 = Entry(root)
txtbox_1.place(x=300,y=100,width=250,height=25)

label_2 = Label(root, text="Enter Last Name",relief="ridge",width=20,bg="lavender",fg='black',font=("bold", 12))
label_2.place(x=30,y=140)

txtbox_2 = Entry(root)
txtbox_2.place(x=300,y=140,width=250,height=25)

label_3 = Label(root, text="Enter Student ID",relief="ridge",width=20,bg="lavender",fg='black',font=("bold", 12))
label_3.place(x=30,y=180)

txtbox_3 = Entry(root)
txtbox_3.place(x=300,y=180,width=250,height=25)


label_4 = Label(root, text="Enter Date of Birth",relief="ridge",width=20,bg="lavender",fg='black',font=("bold", 12))
label_4.place(x=30,y=220)

txtbox_4 = Entry(root)
txtbox_4.place(x=300,y=220,width=250,height=25)

label_5 = Label(root, text="Enter Gender",relief="ridge",width=20,bg="lavender",fg='black',font=("bold", 12))
label_5.place(x=30,y=260)

opt = StringVar(root)
choices={"   MALE   ","   FEMALE   "}
opt.set("Select Gender")
popupMenu = OptionMenu(root,opt, *choices)
popupMenu.place(x=350,y=260,width=150)

label_6 = Label(root, text="Enter Contact Details",relief="ridge",width=20,bg="lavender",fg='black',font=("bold", 12))
label_6.place(x=30,y=300)

txtbox_5 = Entry(root)
txtbox_5.place(x=300,y=300,width=250,height=25)

label_7 = Label(root, text="Enter Email Address",relief="ridge",width=20,bg="lavender",fg='black',font=("bold", 12))
label_7.place(x=30,y=340)

txtbox_6 = Entry(root)
txtbox_6.place(x=300,y=340,width=250,height=25)

label_8 = Label(root, text="Enter Roll Number",relief="ridge",width=20,bg="lavender",fg='black',font=("bold", 12))
label_8.place(x=30,y=380)

spin = Spinbox(root,from_=0,to=100,width=3,font=("bold",12))
spin.place(x=350,y=380,width=150)

label_9 = Label(root, text="Enter Address",relief="ridge",width=20,bg="lavender",fg='black',font=("bold", 12))
label_9.place(x=30,y=420)

txtbox_7 = Text(root)
txtbox_7.place(x=300,y=420,width=250,height=100)

b1=Button(root, text='ENTER',width=12,bg='lightgrey',fg='black',command=entry)
b1.place(x=20,y=550,height=30,width=150)

b2=Button(root, text='FETCH',width=20,bg='lightgrey',fg='black',command=disp)
b2.place(x=220,y=550,height=30,width=150)

b3=Button(root, text='CLEAR',width=20,bg='lightgrey',fg='black',command=clr)
b3.place(x=420,y=550,height=30,width=150)

root.mainloop()
