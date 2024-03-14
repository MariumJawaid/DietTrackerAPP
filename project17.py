from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyodbc
from PIL import Image,ImageTk
m=Tk()
m.geometry('600x750')
m.title("DIET TRACKER")

#frames
frame1=Frame(m,bg="#3d6466",width=600,height=750)
frame2=Frame(m,bg="#3d6466")
frame_=Frame(m,bg="white")
frame3=Frame(m,bg="#3d6466")
frame11=Frame(m,bg="#3d6466")
frame4=Frame(m,bg="#3d6466")
frame5=Frame(m,bg="#3d6466")
frame6=Frame(m,bg="#3d6466")
for frame in (frame1,frame2,frame_,frame3,frame4,frame5,frame6):
    frame.grid(row=0,column=0,sticky="nesw")

con1 = pyodbc.connect((r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                       r'DBQ=c:\Users\Admin\desktop\data.accdb;'))
def insert():
    cursor1 = con1.cursor()
    cursor3 = con1.cursor()
    cursor4 = con1.cursor()
    cursor1.execute(f"INSERT INTO records(Uname,Password,BCALORIES,LCALORIES,DCALORIES) values('{var1.get()}','{var2.get()}','{var3.get()}',"
                    f"'{var4.get()}','{var5.get()}')")

    con1.commit()
    messagebox.showinfo("One record has been added")

cursor1 = con1.cursor()
cursor1.execute("select * from breakfast")
table = cursor1.fetchall()

B=[]
for i in table:
    food = i[0]
    quantity = i[2]
    calories = i[1]
    B.append(quantity + " " + food + " contains "+
                          calories + " calories ")


cursor2 = con1.cursor()
cursor2.execute("select * from lunch")
data = cursor2.fetchall()
L=[]
for i in data:
    food = i[0]
    quantity = i[2]
    calories = i[1]

    L.append(quantity + " of " + food + " contains "
                    + calories + " calories ")

cursor3 = con1.cursor()
cursor3.execute("select * from dinner")
data = cursor3.fetchall()
D=[]
for i in data:
    food = i[0]
    quantity = i[2]
    calories = i[1]

    D.append(quantity + " of " + food + " contains "
                    + calories + " calories ")
    con1.commit()


def clear_widget(frame):
    for widget in frame.winfo_children():
        widget.destroy()

#frame1
def load_frame1():
    frame1.tkraise()
    frame1.pack_propagate(False)
    clear_widget(frame2)
#Adding logo image
    logo_img = PhotoImage(file="diet tracker (4).png")
    logo_widget = Label(frame1, image=logo_img, bg="#3d6466")
    logo_widget.image = logo_img
    logo_widget.pack()
    l1=Label(frame1,text="Manage your diet here!",fg="white",bg="#3d6466",
             font=("italic",25),width=25).pack(pady=5)
    b1=Button(frame1,text="NEXT",bg="black",fg="white",width=15,command=lambda:
              load_frame2()).pack(pady=10)

#frame2
def load_frame2():
    frame2.tkraise()
    clear_widget(frame1)
#adding logo
    logo_img = PhotoImage(file="d4.png")
    logo_widget = Label(frame2, image=logo_img, bg="#3d6466",bd=0)
    logo_widget.image = logo_img
    logo_widget.pack(pady=10)
#adding button image1

    logo_img1 = PhotoImage(file="DIET PLAN (2).png")
    logo_widget = Label(frame2, image=logo_img1, bg="#3d6466")
    logo_widget.image = logo_img1
    b2 = Button(frame2,image=logo_img1,bd=0,command=lambda:load_frame3()
    )
    b2.pack(pady=20)
#adding button image2
    logo_img2 = PhotoImage(file="Body Mass Index (3).png")
    logo_widget = Label(frame2, image=logo_img2, bg="#3d6466")
    logo_widget.image = logo_img2
    b3 = Button(frame2, command=lambda:load_frame_(),image=logo_img2,bd=0)
    b3.pack(pady=20)
    b_=Button(frame2,text="BACK",bg="black",fg="white",width=15,command=lambda:
              load_frame1()).pack(pady=10)
top=PhotoImage(file="top.png")
top2=Label(frame_,image=top,bg="#3d6466")
top2.image=top
top2.pack(side=TOP,fill=X)

#bottom box
Label(frame_,width=72,height=25,bg="light blue").pack(side=BOTTOM,fill=X)

    #two boxes
box=PhotoImage(file="box.png")
m=Label(frame_,image=box,bg="white")
m.image=box
m.place(x=50,y=100)
n= Label(frame_,image=box,bg="white")
n.image=box
n.place(x=330,y=100)

    #scale
scale=PhotoImage(file="scale.png")
x=Label(frame_,image=scale,bg="light blue",width=10)
x.image=scale
x.place(x=10,y=370)
def load_frame_():
    clear_widget(frame1)
    clear_widget(frame2)

    frame_.tkraise()

    def BMI():
        clear_widget(frame1)
        h=float(Height.get())
        w=float(Weight.get())
        m=h/100
        bmi=round(float(w/m**2),1)
        l1.config(text=bmi)
        if bmi<=18.5:
            l2.config(text="Underweight!!")
            l3.config(text="You have lower weight than normal body!")
        elif bmi>18.5 and bmi<=25:
            l2.config(text="Normal!!")
            l3.config(text="It indicates that you are healthy!")
        elif bmi>25 and bmi<=30:
            l2.config(text="Overweight!!")
            l3.config(text="It indicates that you are slighthly overweight!")
        else:
            l2.config(text="Obes!!")
            l3.config(text="Health may be at risk!")


    def get_current_value():
        return'{: .2f}'.format(currentvalue.get())


    def slider_changed(event):
        Height.set(get_current_value())
        size=int(float(get_current_value()))
        img=(Image.open("man.png"))
        resized_image=img.resize((50,10+size))
        photo2=ImageTk.PhotoImage(resized_image)
        man.image= photo2
        man.config(image=photo2)
        man.place(x=80,y=600-size)

    #slider1
    currentvalue=DoubleVar()
    style=ttk.Style()
    style.configure("TScale",bg="white")
    slider=ttk.Scale(frame_,from_=0,to=220,orient='horizontal',style="TScale",command=slider_changed,variable=currentvalue)
    slider.place(x=100,y=250)

    #slider2
    def get_current_value2():
        return'{: .2f}'.format(currentvalue2.get())


    def slider_changed2(event):
        Weight.set(get_current_value2())

    currentvalue2=DoubleVar()
    style2=ttk.Style()
    style2.configure("TScale",bg="white")
    slider2=ttk.Scale(frame_,from_=0,to=220,orient='horizontal',style="TScale",command=slider_changed2,variable=currentvalue2)
    slider2.place(x=390,y=250)

    #entry box
    Height=StringVar()
    Weight=StringVar()
    height=Entry(frame_,textvariable=Height,width=5,font="Ariel 50",bg="#fff",fg="#000",bd=0,justify=CENTER)
    height.place(x=60,y=160)
    weight=Entry(frame_,textvariable=Weight,width=5,font="Ariel 50",bg="#fff",fg="#000",bd=0,justify=CENTER)
    weight.place(x=350,y=160)

    #man image
    man=Label(frame_,bg="light blue")
    man.place(x=50,y=170)
    b=Button(frame_,text="VIEW REPORT",width=15,height=2,font=("bold",15),command=lambda:BMI(),bg="#3d6466",fg="white")
    b.place(x=400,y=370)
    l1=Label(frame_,font="arial 50 bold",bg="lightblue",fg="#3d6466")
    l1.place(x=220,y=370)
    l2=Label(frame_,font="arial 30 bold",bg="lightblue",fg="black")
    l2.place(x=220,y=470)
    l3=Label(frame_,font="arial 13 bold",bg="lightblue",fg="black")
    l3.place(x=220,y=550)
    Label(frame_,text="HEIGHT",width=15,height=1,font="arial").place(x=60,y=290)
    Label(frame_,text="WEIGHT",width=15,height=1,font="arial").place(x=350,y=290)
    bz = Button(frame_, text="BACK", bg="black", fg="white", width=15,height=2, command=lambda:
    load_frame2())
    bz.place(x=440,y=600)

def load_frame3():
    clear_widget(frame2)
    clear_widget(frame3)

    l1=Label(frame3,text="Select the option to enter food!",fg="white",bg="#3d6466",
             font=("italic",19,"bold"),width=30).pack(pady=5)
    frame3.tkraise()
    logo_img3 = PhotoImage(file="BREAKFAST.png")
    logo_widget = Label(frame3, image=logo_img3, bg="#3d6466")
    logo_widget.image = logo_img3
    b4 = Button(frame3, text="CALORIE",image=logo_img3,bd=0,command=lambda:load_frame4()).pack(pady=30)

    logo_img4 = PhotoImage(file="lunch.png")
    logo_widget = Label(frame3, image=logo_img3, bg="#3d6466")
    logo_widget.image = logo_img4
    b5 = Button(frame3,image=logo_img4,bd=0,command=lambda:load_frame5()).pack(pady=30)

    logo_img5 = PhotoImage(file="dinner.png")
    logo_widget = Label(frame3, image=logo_img3, bg="#3d6466")
    logo_widget.image = logo_img5
    b6 = Button(frame3,image=logo_img5,bd=0,command=lambda:load_frame6()).pack(pady=30)
    b7=Button(frame3,text="BACK",bg="black",fg="white",width=15,command=lambda:
              load_frame2()).pack(pady=10)

var1=StringVar()
var2=StringVar()
Search=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()

def calories():
    a=int(e1.get())
    b=int(e2.get())
    c=int(e3.get())
    d=int(e4.get())
    e=int(e5.get())
    f=int(e6_.get())
    g=int(e7_.get())
    h=int(e8_.get())

    x=a+b+c+d+e+f+g+h
    l=Label(frame4, text=x, bg="#3d6466",font=13, fg="steel blue2", width=4).place(x=532, y=520)
    l1=Label(frame4,text=400-x, bg="#3d6466",font=13 ,fg="steel blue2", width=4).place(x=510, y=545)

def load_frame4():
    frame4.tkraise()
    clear_widget(frame3)
for i in B:
    l1 = Label(frame4, text=i, bg="#3d6466", fg="white", font=("TkMenuFont", 12)).pack(pady=15)
    b7 = Button(frame4, text="Click Here to calculate", bg="#3d6466", fg="black", width=20,
                font=("TkMenuFont", 15, "bold"),command=lambda:calories(), bd=0).place(x=1, y=500)
    b8 = Button(frame4, text="BACK", bg="black", fg="white", width=13,
                font=("TkMenuFont", 15, "bold"), command=lambda:load_frame3(), bd=0).place(x=1, y=550)

    l2=Label(frame4,text="Total Calories:400", font=("TkMenuFont", 13),bg="#3d6466",fg="steel blue2",width=15).place(x=420,y=500)
    l3 = Label(frame4, text="Calories Taken:", font=("TkMenuFont", 13), bg="#3d6466", fg="steel blue2",
               width=15).place(x=407, y=520)
    l4 = Label(frame4, text="Remaining:", font=("TkMenuFont", 13), bg="#3d6466", fg="steel blue2",
               width=15).place(x=394, y=545)
e1 = Entry(frame4,  bg="white", fg="black", width=15)
e1.place(x=470,y=20)
e2 = Entry(frame4, bg="white", fg="black", width=15)
e2.place(x=470, y=75)
e3 = Entry(frame4, bg="white", fg="black", width=15)
e3.place(x=470, y=125)
e4 = Entry(frame4,  bg="white", fg="black", width=15)
e4.place(x=470, y=185)
e5 = Entry(frame4, bg="white", fg="black", width=15)
e5.place(x=470, y=235)
e6_ = Entry(frame4, bg="white", fg="black", width=15)
e6_.place(x=470, y=290)
e7_ = Entry(frame4, bg="white", fg="black", width=15)
e7_.place(x=470, y=345)
e8_ = Entry(frame4, bg="white", fg="black", width=15)
e8_.place(x=470, y=395)


def load_frame5():
    frame5.tkraise()

for i in L:
    l1 = Label(frame5, text=i, bg="#3d6466", fg="white", font=("TkMenuFont", 12)).pack(pady=15)
    b7 = Button(frame5, text="Click Here to calculate",command=lambda:calories1(), bg="#3d6466", fg="black", width=20,
                    font=("TkMenuFont", 15, "bold"), bd=0).place(x=1, y=500)
    b8 = Button(frame5, text="BACK", bg="BLACK", fg="white", width=13,
                    font=("TkMenuFont", 15, "bold"), command=lambda:load_frame3(), bd=0).place(x=1, y=550)

    l2 = Label(frame5, text="Total Calories:700", font=("TkMenuFont", 13), bg="#3d6466", fg="steel blue2",
                   width=15).place(x=420, y=500)
    l3 = Label(frame5, text="Calories Taken:", font=("TkMenuFont", 13), bg="#3d6466", fg="steel blue2",
                   width=15).place(x=407, y=520)
    l4 = Label(frame5, text="Remaining:", font=("TkMenuFont", 13), bg="#3d6466", fg="steel blue2",
                   width=15).place(x=394, y=545)

def calories1():
    a=int(e6.get())
    b=int(e7.get())
    c=int(e8.get())
    d=int(e9.get())
    e=int(e10.get())
    f=int(e11_.get())
    y=a+b+c+d+e+f
    l=Label(frame5, text=y, bg="#3d6466",font=13, fg="steel blue2", width=4).place(x=532, y=520)
    l1=Label(frame5,text=700-y, bg="#3d6466",font=13 ,fg="steel blue2", width=4).place(x=510, y=545)
e6 = Entry(frame5,  bg="white", fg="black", width=15)
e6.place(x=480,y=20)
e7 = Entry(frame5, bg="white", fg="black", width=15)
e7.place(x=480, y=75)
e8 = Entry(frame5, bg="white", fg="black", width=15)
e8.place(x=480, y=125)
e9 = Entry(frame5,  bg="white", fg="black", width=15)
e9.place(x=480, y=180)
e10 = Entry(frame5, bg="white", fg="black", width=15)
e10.place(x=480, y=235)
e11_ = Entry(frame5, bg="white", fg="black", width=15)
e11_.place(x=480, y=290)

def load_frame6():
    frame6.tkraise()

for i in D:
    l1 = Label(frame6, text=i, bg="#3d6466", fg="white", font=("TkMenuFont", 12)).pack(pady=15)
    b7 = Button(frame6, text="Click Here to calculate",command=lambda:calories2(), bg="#3d6466", fg="black", width=20,
                    font=("TkMenuFont", 15, "bold"), bd=0).place(x=1, y=500)
    b8 = Button(frame6, text="Insert Record", bg="#3d6466", fg="black", width=13,
                    font=("TkMenuFont", 15, "bold"), command=lambda: data(), bd=0).place(x=400, y=570)
    b9 = Button(frame6, text="BACK", bg="#3d6466", fg="black" ,width=13,
                    font=("TkMenuFont", 15, "bold"),command=lambda:load_frame3() ,bd=0).place(x=1, y=550)
    l2 = Label(frame6, text="Total Calories:700", font=("TkMenuFont", 13), bg="#3d6466", fg="steel blue2",
                   width=15).place(x=420, y=500)
    l3 = Label(frame6, text="Calories Taken:", font=("TkMenuFont", 13), bg="#3d6466", fg="steel blue2",
                   width=15).place(x=407, y=520)
    l4 = Label(frame6, text="Remaining:", font=("TkMenuFont", 13), bg="#3d6466", fg="steel blue2",
                   width=15).place(x=394, y=545)


def calories2():
    a=int(e11.get())
    b=int(e12.get())
    c=int(e13.get())
    d=int(e14.get())
    e=int(e15.get())
    f = int(e16.get())
    z=a+b+c+d+e+f
    l=Label(frame6, text=z, bg="#3d6466",font=13, fg="steel blue2", width=4).place(x=532, y=520)
    l1=Label(frame6,text=700-z, bg="#3d6466",font=13 ,fg="steel blue2", width=4).place(x=510, y=545)
e11 = Entry(frame6,  bg="white", fg="black", width=15)
e11.place(x=480,y=20)
e12 = Entry(frame6, bg="white", fg="black", width=15)
e12.place(x=480, y=75)
e13 = Entry(frame6, bg="white", fg="black", width=15)
e13.place(x=480, y=125)
e14 = Entry(frame6,  bg="white", fg="black", width=15)
e14.place(x=480, y=180)
e15 = Entry(frame6, bg="white", fg="black", width=15)
e15.place(x=480, y=235)
e16 = Entry(frame6, bg="white", fg="black", width=15)
e16.place(x=480, y=285)

def data():
    frame6.pack_propagate(False)
    clear_widget(frame6)
    la=Label(frame6,text="USER NAME",fg="black",bg="light blue"
             ,width=20).place(x=100,y=30)
    la1 = Label(frame6, text="Password", bg="lightblue",fg="black",
                width=20).place(x=100, y=70)
    la2 = Label(frame6, text="BREAKFAST CALORIES", bg="lightblue",fg="black",
                width=20).place(x=100, y=110)
    la3 = Label(frame6, text="LAUNCH CALORIES", bg="lightblue",fg="black",
                width=20).place(x=100, y=150)
    la4 = Label(frame6, text="DINNER CALORIES", bg="lightblue",fg="black",
                width=20).place(x=100, y=190)
    e1=Entry(frame6,textvariable=var1,bg="white",fg="black",width=20).place(x=300,y=30)
    e2 = Entry(frame6,textvariable=var2, bg="white", fg="black", width=20).place(x=300,y=70)
    e3 = Entry(frame6,textvariable=var3, bg="white", fg="black", width=20).place(x=300,y=110)
    e4 = Entry(frame6,textvariable=var4, bg="white", fg="black", width=20).place(x=300,y=150)
    e5 = Entry(frame6,textvariable=var5, bg="white", fg="black", width=20).place(x=300,y=190)
    b=Button(frame6,text="SAVE",bg="black",fg="white",width=15,command=insert).place(x=100,y=230)
    b=Button(frame6,text="SEARCH",bg="black",fg="white",width=15,command=lambda:SearchRecord()).place(x=100,y=270)
    e3 = Entry(frame6,textvariable=Search, bg="white", fg="black", width=20).place(x=300,y=275)

    dtable=ttk.Treeview(frame6,height=80,columns=("Uname","Password","BCALORIES","LCALORIES","DCALORIES") ,show='headings')
    dtable.place(x=90,y=340)
    dtable.column("Uname",anchor=CENTER,stretch=NO,width=70)
    dtable.column("Password", anchor=CENTER, stretch=NO, width=70)
    dtable.column("BCALORIES", anchor=CENTER, stretch=NO, width=70)
    dtable.column("LCALORIES", anchor=CENTER, stretch=NO, width=70)
    dtable.column("DCALORIES", anchor=CENTER, stretch=NO, width=70)
    dtable.heading("Uname", text="Uname")
    dtable.heading("Password",text="pasword")
    dtable.heading("BCALORIES",text="BCALORIES")
    dtable.heading("LCALORIES",text="LCALORIES")
    dtable.heading("DCALORIES",text="DCALORIES")

    def SearchRecord():
            # select query with where clause
        cursor2 = con1.cursor()
        cursor2.execute("SELECT * FROM records WHERE Password=?", (Search.get()))
            # fetch all matching records
        fetch = cursor2.fetchall()
            # loop for displaying all records into GUI
        f=[]
        for i in fetch:
            f.append(i)
            for i in f:
                dtable.insert('',END,values=i)
load_frame1()
m.mainloop()