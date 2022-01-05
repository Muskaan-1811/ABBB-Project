from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time;
import datetime
import mysql.connector as mc
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt

#=================Table Creation=============================================================================================================================

mydb=mc.connect(host='localhost',user='root',passwd='ips18',database='bbmi')

mycursor=mydb.cursor()
mycursor.execute('''create table pd1(
                 Patient_ID varchar(20) primary key,
                 Name varchar(55),
                 Age varchar(13),
                 Blood_Group varchar(54),
                 Gender varchar(45),
                 Date varchar(65),
                 Contact_No varchar(23),
                 Amount varchar(75))''')

mydb=mc.connect(host='localhost',user='root',passwd='ips18',database='bbmi')

mycursor=mydb.cursor()
mycursor.execute('''create table dd1(
                 Donor_ID varchar(20) primary key,
                 Name varchar(55),
                 Age varchar(13),
                 Blood_Group varchar(54),
                 Gender varchar(45),
                 Date varchar(65),
                 Contact_No varchar(23),
                 Amount varchar(75))''')


#=================Blood Details Graph========================================================================================================================

def graph():

        n = 8
        y2016 = (21.23, 0.66, 33.52, 1.42, 33.26, 1.40, 8.23, 0.28)
        y2017 = (21.8, 0.94, 34.40, 1.41, 32.39, 1.43, 7.38, 0.25)
        y2018 = (21.07, 0.75, 33.09, 0.81, 35.56, 1.13, 7.51, 0.08)
        y2019 = (21.06, 0.86, 34.51, 1.46, 32.74, 1.04, 8.08, 0.25)

        fig, ax = plt.subplots()
        index = np.arange(n)
        bar_width = 0.15
        opacity = 0.9

        ax.bar(index, y2016, bar_width, alpha=opacity, color='red',
                        label='2016')
        ax.bar(index+bar_width, y2017, bar_width, alpha=opacity, color='yellow',
                        label='2017')
        ax.bar(index+2*bar_width, y2018, bar_width, alpha=opacity,
                color='green', label='2018')
        ax.bar(index+3*bar_width, y2019, bar_width, alpha=opacity,
                color='blue', label='2019')

        ax.set_xlabel('Blood Groups')
        ax.set_ylabel('Percentage Distribution')
        ax.set_title('Percentage Distribution of various Blood Groups')
        ax.set_xticks(index + bar_width)
        ax.set_xticklabels(('A+','A-','B+','B-','O+','O-','AB+','AB-'))
        ax.legend(ncol=4)
        fig.canvas.set_window_title('Blood Details')

        plt.show()

#=============Home Window====================================================================================================================================


class Window1:
    def __init__(self, root):
        self.root = root
        self.root.title("Blood Bank Management System")
        self.root.geometry("1350x750+0+0")

        self.Username= StringVar()
        self.Password= StringVar()

        self.logo=ImageTk.PhotoImage(file="blood.jpeg")
        bg=Label(self.root,image=self.logo).place(x=10,y=0,width=400,height=500)

        frame1=Frame(self.root)
        frame1.place(x=410,y=0,width=1200,height=900)

        self.bg=ImageTk.PhotoImage(file="Picture1.jpg")
        bg=Label(frame1,image=self.bg).place(x=0,y=0)

        frame2=Frame(self.root,bg='black')
        frame2.place(x=10,y=500,width=400,height=200)

                
        self.Title = Label(frame1,text='Aarogya Bharat Blood Bank',font=("Monotype Corsiva",35,"bold"),fg='black')
        self.Title.place(x=285,y=70)
        
        self.Title = Label(frame2,text='A single pint \n can save three lives,\n a single gesture can create \n a million smiles',
                           bg='black',font=("Monotype Corsiva",25,"bold"),fg='yellow')
        self.Title.place(x=0,y=0,relwidth=1,relheight=1)
        
        self.lblUsername=Label(frame1,text='Username',font=('arial',15,'bold'),fg='dark blue',bd=15)
        self.lblUsername.place(x=310,y=140)
        self.txtUsername=Entry(frame1,font=('arial',15,'bold'),bd=15,textvariable=self.Username)
        self.txtUsername.place(x=450,y=140)

        
        self.lblPassword=Label(frame1,text='Password',font=('arial',15,'bold'),fg='dark blue',bd=15)
        self.lblPassword.place(x=310,y=210)
        self.txtPassword=Entry(frame1,font=('arial',15,'bold'),bd=15,textvariable=self.Password,show='*').place(x=450,y=210)

        self.btnLogin = Button(frame1,text='Login',width=14,font=("arial",15,"bold"),fg='dark blue',command = self.Login_System)
        self.btnLogin.place(x=280,y=280)

        self.btnReset = Button(frame1,text='Reset',width=14,font=("arial",15,"bold"),fg='dark blue',command = self.Reset)
        self.btnReset.place(x=440,y=280)
        
        self.btnExit = Button(frame1,text='Exit',width=14,font=("arial",15,"bold"),fg='dark blue',command = self.Exit)
        self.btnExit.place(x=600,y=280)

        self.btnregis = Button(frame1,state= DISABLED,text='Patient Details',width=14,font=("arial",15,"bold"),fg='dark blue',command = self.regis_window)
        self.btnregis.place(x=430,y=360)
        
        self.btndonor = Button(frame1,state= DISABLED,text='Donor Details',width=14,font=("arial",15,"bold"),fg='dark blue',command = self.donor_window)
        self.btndonor.place(x=430,y=440)

        self.btnblood = Button(frame1,state= DISABLED,text='Blood Details',width=14,font=("arial",15,"bold"),fg='dark blue',command = graph)
        self.btnblood.place(x=430,y=520)
        
#================Main Window Commands========================================================================================================================

    def Login_System(self):
        user=(self.Username.get())
        pas=(self.Password.get())

        if (user==str('ABBB')) and (pas==str('1234')):
            self.btnregis.config(state= NORMAL)
            self.btndonor.config(state= NORMAL)
            self.btnblood.config(state= NORMAL)
        else:
            tkinter.messagebox.askretrycancel('Blood Bank Management System','You have entered invalid login details')
            self.btnregis.config(state= DISABLED)
            self.btndonor.config(state= DISABLED)
            self.btnblood.config(state= DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

        

    def Reset(self):
        
        self.btnregis.config(state= DISABLED)
        self.btndonor.config(state= DISABLED)
        self.btnblood.config(state= DISABLED)
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()
        


    def Exit(self):
        self.Exit=tkinter.messagebox.askyesno('Blood Bank Management System','Confirm if you want to exit')
        if self.Exit>0:
            self.root.destroy()
            return
    def regis_window(self):
        self.newWindow = Toplevel(self.root)
        self.app = Window2(self.newWindow)
       
    def donor_window(self):
        self.newWindow = Toplevel(self.root)
        self.app = Window3(self.newWindow)

    def blood(self):
        self.newWindow = Toplevel(self.root)
        self.app = Window4(self.newWindow)
            

#=======================Patient Details======================================================================================================================

class Window2:



    
    def __init__(self, root):
        global my_tree,p_id_txt,name_txt,age_txt,gender_txt,Blood_Group_txt,date_txt,phone_txt,amt_txt,del_id_txt

        #Window Details
        
        self.root = root
        self.root.title("Patient Details")
        self.root.geometry("1350x750")
        self.frame = Frame(self.root)
        self.frame.pack()

        #Variables for Entry

        self.p_id_v=StringVar()
        self.name_v=StringVar()
        self.age_v=StringVar()
        self.gender_v=StringVar()
        self.Blood_Group_v=StringVar()
        self.date_v=StringVar()
        self.phone_v=StringVar()
        self.amt_v=StringVar()
        self.del_id_v=StringVar()

        #Window Frame

        frame1=Frame(self.root)
        frame1.place(x=0,y=0,width=1350,height=750)


        self.bg=ImageTk.PhotoImage(file="bg3.jpg")
        bg=Label(frame1,image=self.bg).place(x=0,y=0)
        self.logo=ImageTk.PhotoImage(file="blood1.1.jpg")
        bg=Label(self.root,image=self.logo).place(x=10,y=0)

        title_frame = Frame(frame1, bg="white")
        title_frame.place(x=105,y=0,width=1250,height=103)

        Title_label= Label(title_frame,text="Patient Details", bg="Black",fg="White",
                      font=("monotype corsiva",50,"bold"),borderwidth=4)
        Title_label.place(relwidth=1,relheight=1)

        #Labels & Entry Boxes

        p_id=Label(frame1,text='Patient Id ',font=("times new roman",20,"bold"),fg='black',width=9)
        p_id.place(x=20,y=140)
        p_id_txt=Entry(frame1,font=('times new roman',20,'bold'),bd=5,textvariable=self.p_id_v,width=17)
        p_id_txt.place(x=180,y=140)

        name=Label(frame1,text='Name',font=("times new roman",20,"bold"),fg='black',width=9)
        name.place(x=20,y=200)
        name_txt=Entry(frame1,font=('times new roman',20,'bold'),bd=5,textvariable=self.name_v,width=17)
        name_txt.place(x=180,y=200)

        age=Label(frame1,text='Age',font=("times new roman",20,"bold"),fg='black',width=9)
        age.place(x=20,y=260)
        age_txt=Entry(frame1,font=('times new roman',20,'bold'),bd=5,textvariable=self.age_v,width=17)
        age_txt.place(x=180,y=260)

        Blood_Group=Label(frame1,text='Blood Group',font=("times new roman",20,"bold"),fg='black',width=9)
        Blood_Group.place(x=20,y=380)
        Blood_Group_txt=ttk.Combobox(frame1,font=('times new roman',20,'bold'),textvariable=self.Blood_Group_v,width=16,state='readonly',justify=CENTER)
        Blood_Group_txt['values']=('Select','A+','A-','B+','B-','O+','O-','AB+','AB-')
        Blood_Group_txt.place(x=180,y=380)
        Blood_Group_txt.current(0)

        gender=Label(frame1,text='Gender',font=("times new roman",20,"bold"),fg='black',width=9)
        gender.place(x=20,y=320)
        gender_txt=ttk.Combobox(frame1,font=('times new roman',20,'bold'),textvariable=self.gender_v,width=16,state='readonly',justify=CENTER)
        gender_txt['values']=('Select','Male','Female','Other')
        gender_txt.place(x=180,y=320)
        gender_txt.current(0)
        
        date=Label(frame1,text='Date',font=("times new roman",20,"bold"),fg='black',width=9)
        date.place(x=20,y=440)
        date_txt=Entry(frame1,font=('times new roman',20,'bold'),bd=5,textvariable=self.date_v,width=17)
        date_txt.place(x=180,y=440)

        phone=Label(frame1,text='Ph. Number',font=("times new roman",20,"bold"),fg='black',width=9)
        phone.place(x=20,y=500)
        phone_txt=Entry(frame1,font=('times new roman',20,'bold'),bd=5,textvariable=self.phone_v,width=17)
        phone_txt.place(x=180,y=500)

        amt=Label(frame1,text='Amt.Req',font=("times new roman",20,"bold"),fg='black',width=9)
        amt.place(x=20,y=560)
        amt_txt=Entry(frame1,font=('times new roman',20,'bold'),bd=5,textvariable=self.amt_v,width=17)
        amt_txt.place(x=180,y=560)

        del_id=Label(frame1,text='Delete Id',font=("times new roman",20,"bold"),fg='black',width=9)
        del_id.place(x=496,y=580)
        del_id_txt=Entry(frame1,font=('times new roman',20,'bold'),textvariable=self.del_id_v,bd=5,width=17)
        del_id_txt.place(x=656,y=580)

        #Buttons

        add=Button(frame1,text='Add',font=("times new roman",15,"bold"),bg='black',fg='yellow',width=7,command = lambda:[self.add(),self.add_record()])
        add.place(x=20,y=625)

        clear=Button(frame1,text='Clear',font=("times new roman",15,"bold"),bg='black',fg='yellow',width=7,command = lambda:[self.clear(),self.remove()])
        clear.place(x=125,y=625)

        reset=Button(frame1,text='Reset',font=("times new roman",15,"bold"),bg='black',fg='yellow',width=7, command = self.reset)
        reset.place(x=230,y=625)

        exi=Button(frame1,text='Exit',font=("times new roman",15,"bold"),bg='black',fg='yellow',width=7,command = self.Exit)
        exi.place(x=335,y=625)
        
#================Treeview 1==================================================================================================================================

        frame2=Frame(self.root)
        frame2.place(x=495,y=115,width=800,height=460)

        tree_scroll= Scrollbar(frame2)
        tree_scroll.pack(side=RIGHT,fill=Y)

        my_tree = ttk.Treeview(frame2,height=540,yscrollcommand=tree_scroll.set,selectmode='browse')
        my_tree.place(x=496,y=116)
        my_tree.pack()

        tree_scroll.config(command=my_tree.yview)
        
        my_tree['columns']=('Patient Id','Name','Age','Gender','Blood Group','date','phone no.','amt')
        my_tree.column('#0',width=10,stretch=NO)
        my_tree.column('Patient Id',anchor=W,width=90)
        my_tree.column('Name',anchor=W,width=160)
        my_tree.column('Age',anchor=W,width=50)
        my_tree.column('Gender',anchor=W,width=90)
        my_tree.column('Blood Group',anchor=W,width=80)
        my_tree.column('date',anchor=W,width=100)
        my_tree.column('phone no.',anchor=W,width=100)
        my_tree.column('amt',anchor=W,width=50)

        my_tree.heading('#0',text='',anchor=W)
        my_tree.heading('Patient Id',text='Patient Id',anchor=W)
        my_tree.heading('Name',text='Name',anchor=W)
        my_tree.heading('Age',text='Age',anchor=W)
        my_tree.heading('Gender',text='Gender',anchor=W)
        my_tree.heading('Blood Group',text='Blood Group',anchor=W)
        my_tree.heading('date',text='date',anchor=W)
        my_tree.heading('phone no.',text='phone no.',anchor=W)
        my_tree.heading('amt',text='amt',anchor=W)
        
        #Default Entry in the Treeview
        
        my_tree.insert(parent='',index='end',iid=0,text='',values=('23456','Debjit','20','Male','A+','12-12-2019','8765984320','45'))

#==========Commands==========================================================================================================================================

    #To add data to sql database

    def add(self):
        global p_id_txt,name_txt,age_txt,gender_txt,Blood_Group_txt,date_txt,phone_txt,amt_txt
    
        p_id_z=(self.p_id_v.get())
        name_z=(self.name_v.get())
        age_z=(self.age_v.get())
        Blood_Group_z=(self.Blood_Group_v.get())
        gender_z=(self.gender_v.get())
        date_z=(self.date_v.get())
        phone_z=(self.phone_v.get())
        amt_z=(self.amt_v.get())

        if(p_id_z=="" or name_z=="" or age_z=="" or Blood_Group_z=="" or gender_z=="" or date_z=="" or phone_z=="" or amt_z==""):
            tkinter.messagebox.showinfo("Insert Status","All Fields are required")
        else:
            mydb=mc.connect(host='localhost',user='root',passwd='ips18',database='bbmi')
            mycursor=mydb.cursor()
            mycursor.execute("insert into pd1 values('{}','{}','{}','{}','{}','{}','{}','{}')".format(p_id_z,name_z,age_z,Blood_Group_z,
                                                                                                      gender_z,date_z,phone_z,amt_z))
            mydb.commit()

    #To delete data from sql database

    def clear(self):
        global p_id_txt,name_txt,age_txt,gender_txt,Blood_Group_txt,date_txt,phone_txt,amt_txt,del_id_txt
    
        p_id_z=(self.p_id_v.get())
        name_z=(self.name_v.get())
        age_z=(self.age_v.get())
        Blood_Group_z=(self.Blood_Group_v.get())
        gender_z=(self.gender_v.get())
        date_z=(self.date_v.get())
        phone_z=(self.phone_v.get())
        amt_z=(self.amt_v.get())
        del_id_z=(self.del_id_v.get())

        mydb=mc.connect(host='localhost',user='root',passwd='ips18',database='bbmi')
        mycursor=mydb.cursor()
        mycursor.execute("delete from pd1 where Patient_ID='{}'".format(del_id_z))
        mydb.commit()
    
    #To add data to Treeview     

    def add_record(self):
        count=1
        
        global my_tree
        my_tree.insert(parent='',index='end',iid=count,text='',values=(self.p_id_v.get(),self.name_v.get(),
                                                                           self.age_v.get(),self.gender_v.get(),self.Blood_Group_v.get(),
                                                                        self.date_v.get(),self.phone_v.get(),self.amt_v.get()))
        
        count+=1
            
    #To delete data from Treeview

    def remove(self):
        global x
        x= my_tree.selection()[0]
        my_tree.delete(x)


    #To Exit Window

    def Exit(self):
        self.root.destroy()

    #To reset all entries

    def reset(self):
        global p_id_txt,name_txt,age_txt,gender_txt,Blood_Group_txt,date_txt,phone_txt,amt_txt,del_id_txt
        
        l=[p_id_txt,name_txt,age_txt,gender_txt,Blood_Group_txt,date_txt,phone_txt,amt_txt,del_id_txt]
        for i in l:
            i.delete(0,END)

        gender_txt.set('Select')
        Blood_Group_txt.set('Select')

#=================Donor Window===============================================================================================================================
        

        
class Window3:
    def __init__(self, root):
        global my_tree,p_id_txt,name_txt,age_txt,gender_txt,Blood_Group_txt,date_txt,phone_txt,amt_txt,del_id_txt
        
        #Window Details

        self.root = root
        self.root.title("Donor Details")
        self.root.geometry("1350x750")
        self.frame = Frame(self.root)
        self.frame.pack()

        #Variables for Entry

        self.p_id_v=StringVar()
        self.name_v=StringVar()
        self.age_v=StringVar()
        self.gender_v=StringVar()
        self.Blood_Group_v=StringVar()
        self.date_v=StringVar()
        self.phone_v=StringVar()
        self.amt_v=StringVar()
        self.del_id_v=StringVar()

        #Window Frame

        frame1=Frame(self.root)
        frame1.place(x=0,y=0,width=1350,height=750)


        self.bg=ImageTk.PhotoImage(file="bg3.jpg")
        bg=Label(frame1,image=self.bg).place(x=0,y=0)
        self.logo=ImageTk.PhotoImage(file="blood1.1.jpg")
        bg=Label(self.root,image=self.logo).place(x=10,y=0)

        title_frame = Frame(frame1, bg="white")
        title_frame.place(x=105,y=0,width=1250,height=103)

        Title_label= Label(title_frame,text="Donor Details", bg="Black",fg="White",
                      font=("monotype corsiva",50,"bold"),borderwidth=4)
        Title_label.place(relwidth=1,relheight=1)

        #Labels & Entry Boxes

        p_id=Label(frame1,text='Donor ID',font=("times new roman",20,"bold"),fg='black',width=9)
        p_id.place(x=20,y=140)
        p_id_txt=Entry(frame1,font=('times new roman',20,'bold'),bd=5,textvariable=self.p_id_v,width=17)
        p_id_txt.place(x=180,y=140)

        name=Label(frame1,text='Name',font=("times new roman",20,"bold"),fg='black',width=9)
        name.place(x=20,y=200)
        name_txt=Entry(frame1,font=('times new roman',20,'bold'),bd=5,textvariable=self.name_v,width=17)
        name_txt.place(x=180,y=200)

        age=Label(frame1,text='Age',font=("times new roman",20,"bold"),fg='black',width=9)
        age.place(x=20,y=260)
        age_txt=Entry(frame1,font=('times new roman',20,'bold'),bd=5,textvariable=self.age_v,width=17)
        age_txt.place(x=180,y=260)

        Blood_Group=Label(frame1,text='Blood Group',font=("times new roman",20,"bold"),fg='black',width=9)
        Blood_Group.place(x=20,y=380)
        Blood_Group_txt=ttk.Combobox(frame1,font=('times new roman',20,'bold'),textvariable=self.Blood_Group_v,width=16,state='readonly',justify=CENTER)
        Blood_Group_txt['values']=('Select','A+','A-','B+','B-','O+','O-','AB+','AB-')
        Blood_Group_txt.place(x=180,y=380)
        Blood_Group_txt.current(0)
        
        gender=Label(frame1,text='Gender',font=("times new roman",20,"bold"),fg='black',width=9)
        gender.place(x=20,y=320)
        gender_txt=ttk.Combobox(frame1,font=('times new roman',20,'bold'),textvariable=self.gender_v,width=16,state='readonly',justify=CENTER)
        gender_txt['values']=('Select','Male','Female','Other')
        gender_txt.place(x=180,y=320)
        gender_txt.current(0)

        date=Label(frame1,text='Date',font=("times new roman",20,"bold"),fg='black',width=9)
        date.place(x=20,y=440)
        date_txt=Entry(frame1,font=('times new roman',20,'bold'),bd=5,textvariable=self.date_v,width=17)
        date_txt.place(x=180,y=440)

        phone=Label(frame1,text='Ph. Number',font=("times new roman",20,"bold"),fg='black',width=9)
        phone.place(x=20,y=500)
        phone_txt=Entry(frame1,font=('times new roman',20,'bold'),bd=5,textvariable=self.phone_v,width=17)
        phone_txt.place(x=180,y=500)

        amt=Label(frame1,text='Amt.Req',font=("times new roman",20,"bold"),fg='black',width=9)
        amt.place(x=20,y=560)
        amt_txt=Entry(frame1,font=('times new roman',20,'bold'),bd=5,textvariable=self.amt_v,width=17)
        amt_txt.place(x=180,y=560)

        del_id=Label(frame1,text='Delete Id',font=("times new roman",20,"bold"),fg='black',width=9)
        del_id.place(x=496,y=580)
        del_id_txt=Entry(frame1,font=('times new roman',20,'bold'),textvariable=self.del_id_v,bd=5,width=17)
        del_id_txt.place(x=656,y=580)

        #Buttons

        add=Button(frame1,text='Add',font=("times new roman",15,"bold"),bg='black',fg='yellow',width=7,command = lambda:[self.add(),self.add_record()])
        add.place(x=20,y=625)

        clear=Button(frame1,text='Clear',font=("times new roman",15,"bold"),bg='black',fg='yellow',width=7,command = lambda:[self.clear(),self.remove()])
        clear.place(x=125,y=625)

        reset=Button(frame1,text='Reset',font=("times new roman",15,"bold"),bg='black',fg='yellow',width=7, command = self.reset)
        reset.place(x=230,y=625)

        exi=Button(frame1,text='Exit',font=("times new roman",15,"bold"),bg='black',fg='yellow',width=7,command = self.Exit)
        exi.place(x=335,y=625)

#================Treeview 2==================================================================================================================================

        frame2=Frame(self.root)
        frame2.place(x=495,y=115,width=800,height=460)

        tree_scroll= Scrollbar(frame2)
        tree_scroll.pack(side=RIGHT,fill=Y)

        my_tree = ttk.Treeview(frame2,height=540,yscrollcommand=tree_scroll.set,selectmode='browse')
        my_tree.place(x=496,y=116)
        my_tree.pack()

        tree_scroll.config(command=my_tree.yview)
        
        my_tree['columns']=('Donor ID','Name','Age','Gender','Blood Group','date','phone no.','amt')
        my_tree.column('#0',width=10,stretch=NO)
        my_tree.column('Donor ID',anchor=W,width=90)
        my_tree.column('Name',anchor=W,width=160)
        my_tree.column('Age',anchor=W,width=50)
        my_tree.column('Gender',anchor=W,width=90)
        my_tree.column('Blood Group',anchor=W,width=80)
        my_tree.column('date',anchor=W,width=100)
        my_tree.column('phone no.',anchor=W,width=100)
        my_tree.column('amt',anchor=W,width=50)

        my_tree.heading('#0',text='',anchor=W)
        my_tree.heading('Donor ID',text='Donor ID',anchor=W)
        my_tree.heading('Name',text='Name',anchor=W)
        my_tree.heading('Age',text='Age',anchor=W)
        my_tree.heading('Gender',text='Gender',anchor=W)
        my_tree.heading('Blood Group',text='Blood Group',anchor=W)
        my_tree.heading('date',text='date',anchor=W)
        my_tree.heading('phone no.',text='phone no.',anchor=W)
        my_tree.heading('amt',text='amt',anchor=W)

        #Default Entry in the Treeview
        
        my_tree.insert(parent='',index='end',iid=0,text='',values=('28476','Sakshi','25','Female','B+','12-12-2020','8765984320','55'))

#===========Commands=========================================================================================================================================

    #To add data to sql database

    def add(self):
        global p_id_txt,name_txt,age_txt,gender_txt,Blood_Group_txt,date_txt,phone_txt,amt_txt
    
        p_id_z=(self.p_id_v.get())
        name_z=(self.name_v.get())
        age_z=(self.age_v.get())
        Blood_Group_z=(self.Blood_Group_v.get())
        gender_z=(self.gender_v.get())
        date_z=(self.date_v.get())
        phone_z=(self.phone_v.get())
        amt_z=(self.amt_v.get())

        if(p_id_z=="" or name_z=="" or age_z=="" or Blood_Group_z=="" or gender_z=="" or date_z=="" or phone_z=="" or amt_z==""):
            tkinter.messagebox.showinfo("Insert Status","All Fields are required")
        else:
            mydb=mc.connect(host='localhost',user='root',passwd='ips18',database='bbmi')
            mycursor=mydb.cursor()
            mycursor.execute("insert into dd1 values('{}','{}','{}','{}','{}','{}','{}','{}')".format(p_id_z,name_z,age_z,Blood_Group_z,
                                                                                                      gender_z,date_z,phone_z,amt_z))
            mydb.commit()

    #To delete data from sql database

    def clear(self):
        global p_id_txt,name_txt,age_txt,gender_txt,Blood_Group_txt,date_txt,phone_txt,amt_txt,del_id_txt
    
        p_id_z=(self.p_id_v.get())
        name_z=(self.name_v.get())
        age_z=(self.age_v.get())
        Blood_Group_z=(self.Blood_Group_v.get())
        gender_z=(self.gender_v.get())
        date_z=(self.date_v.get())
        phone_z=(self.phone_v.get())
        amt_z=(self.amt_v.get())
        del_id_z=(self.del_id_v.get())

        

        mydb=mc.connect(host='localhost',user='root',passwd='ips18',database='bbmi')
        mycursor=mydb.cursor()
        mycursor.execute("delete from dd1 where Donor_ID='{}'".format(del_id_z))
        mydb.commit()

    #To add data to Treeview     
         
    def add_record(self):
        count=1
        
        global my_tree
        my_tree.insert(parent='',index='end',iid=count,text='',values=(self.p_id_v.get(),self.name_v.get(),
                                                                           self.age_v.get(),self.gender_v.get(),self.Blood_Group_v.get(),
                                                                        self.date_v.get(),self.phone_v.get(),self.amt_v.get()))
        
        count+=1
            
    #To delete data from Treeview     

    def remove(self):
        global x
        x= my_tree.selection()[0]
        my_tree.delete(x)

    #To Exit Window

    def Exit(self):
        self.root.destroy()

    #To reset all entries

    def reset(self):
        global p_id_txt,name_txt,age_txt,gender_txt,Blood_Group_txt,date_txt,phone_txt,amt_txt,del_id_txt
        
        l=[p_id_txt,name_txt,age_txt,gender_txt,Blood_Group_txt,date_txt,phone_txt,amt_txt,del_id_txt]
        for i in l:
            i.delete(0,END)

        gender_txt.set('Select')
        Blood_Group_txt.set('Select')
        

#============================================================================================================================================================
        
if __name__ == '__main__':
    root =tkinter.Tk()
    app = Window1(root)
    root.mainloop()
    
#============================================================================================================================================================
