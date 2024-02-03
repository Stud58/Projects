from  tkinter import *

root=Tk()
root.geometry("1000x500")
root.title("Bill Management")
root.resizable(False,False)

def Reset():
    entry_Chapo.delete(0,END)
    entry_Juice.delete(0,END)
    entry_Fish.delete(0,END)
    entry_Soda.delete(0,END)
    entry_Chips.delete(0,END)
    entry_Cookies.delete(0,END)
    entry_Beans.delete(0,END)

def Total():
    try:a1=int(Chapo.get())
    except:a1=0
    try:a2=int(Soda.get())
    except:a2=0
    try:a3=int(Beans.get())
    except:a3=0
    try:a4=int(Chips.get())
    except:a4=0
    try:a5=int(Cookies.get())
    except:a5=0
    try:a6=int(Fish.get())
    except:a6=0
    try:a7=int(Juice.get())
    except:a7=0

    c1=20*a1
    c2=40*a2
    c3=25*a3
    c4=50*a4
    c5=30*a5
    c6=100*a6
    c7=70*a7

    lbl_total=Label(f2,font=('aria',20,'bold'),text="Total",width=16,fg="magenta",bg="black")
    lbl_total.place(x=0,y=50)

    entry_total=Entry(f2,font=('aria',20,'bold'),textvariable=Total_Bill,bd=6,width=15,bg="lightgreen")
    entry_total.place(x=20,y=100)

    totalcost=c1+c2+c3+c4+c5+c6+c7
    string_bill="Kshs.",str('%.2f'%totalcost)
    # noinspection PyTypeChecker
    Total_Bill.set(string_bill)

Label(text="BILL MANAGEMENT",bg="blue",fg="white",font=("calibri",33),width="300",height="2").pack()

#menu card

f=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=90,y=0)

Label(f,font=("Lucida Calligraphy",15,'bold'),text="Chapo.....Kshs.20/plate",fg="black",
      bg="lightgreen").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Soda.....Kshs.40/bottle",fg="black",
      bg="lightgreen").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Beans.....Kshs.25/plate",fg="black",
      bg="lightgreen").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Chips.....Kshs.50/packet",fg="black",
      bg="lightgreen").place(x=10,y=170)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Cookies.....Kshs.30/plate",fg="black",
      bg="lightgreen").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Fish.....Kshs.100/plate",fg="black",
      bg="lightgreen").place(x=10,y=230)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Juice.....Kshs.70/glass",fg="black",
      bg="lightgreen").place(x=10,y=260)

f2=Frame(root,bg="magenta",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text="Bill",font=('calibri',20),bg="magenta")
Bill.place(x=120,y=10)

f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

Chapo=StringVar()
Soda=StringVar()
Beans=StringVar()
Chips=StringVar()
Cookies=StringVar()
Fish=StringVar()
Juice=StringVar()
Total_Bill=StringVar()

lbl_Chapo=Label(f1,font=("aria",20,'bold'),text="Chapo",width=12,fg="blue4")
lbl_Soda=Label(f1,font=("aria",20,'bold'),text="Soda",width=12,fg="blue4")
lbl_Beans=Label(f1,font=("aria",20,'bold'),text="Beans",width=12,fg="blue4")
lbl_Chips=Label(f1,font=("aria",20,'bold'),text="Chips",width=12,fg="blue4")
lbl_Cookies=Label(f1,font=("aria",20,'bold'),text="Cookies",width=12,fg="blue4")
lbl_Fish=Label(f1,font=("aria",20,'bold'),text="Fish",width=12,fg="blue4")
lbl_Juice=Label(f1,font=("aria",20,'bold'),text="Juice",width=12,fg="blue4")

lbl_Chapo.grid(row=1,column=0)
lbl_Soda.grid(row=2,column=0)
lbl_Beans.grid(row=3,column=0)
lbl_Chips.grid(row=4,column=0)
lbl_Cookies.grid(row=5,column=0)
lbl_Fish.grid(row=6,column=0)
lbl_Juice.grid(row=7,column=0)


entry_Chapo=Entry(f1,font=("aria",20,'bold'),textvariable=Chapo,bd=6,width=8,bg="lightpink")
entry_Soda=Entry(f1,font=("aria",20,'bold'),textvariable=Soda,bd=6,width=8,bg="lightpink")
entry_Beans=Entry(f1,font=("aria",20,'bold'),textvariable=Beans,bd=6,width=8,bg="lightpink")
entry_Chips=Entry(f1,font=("aria",20,'bold'),textvariable=Chips,bd=6,width=8,bg="lightpink")
entry_Cookies=Entry(f1,font=("aria",20,'bold'),textvariable=Cookies,bd=6,width=8,bg="lightpink")
entry_Fish=Entry(f1,font=("aria",20,'bold'),textvariable=Fish,bd=6,width=8,bg="lightpink")
entry_Juice=Entry(f1,font=("aria",20,'bold'),textvariable=Juice,bd=6,width=8,bg="lightpink")

entry_Chapo.grid(row=1,column=1)
entry_Soda.grid(row=2,column=1)
entry_Beans.grid(row=3,column=1)
entry_Chips.grid(row=4,column=1)
entry_Cookies.grid(row=5,column=1)
entry_Fish.grid(row=6,column=1)
entry_Juice.grid(row=7,column=1)

btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)

root.mainloop()