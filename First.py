from tkinter import *
from Birth import *
from Income import *
import pymysql
import os


class Home:


    def __init__(self,master,uidai):
        master.geometry('300x300+650+200')
        master.title("Certificates")
        self.master=master
        master.wm_iconbitmap('C:\\Users\\jerin\\OneDrive\\Desktop\\favicon.ico')
        self.uidai=uidai
        self.f = Frame(master, width=300, height=300, background='purple')
        self.f.place(x='0', y='0')

        menu = Menu(master)
        master.config(menu=menu)
        subMenu = Menu(menu,tearoff=0)
        menu.add_cascade(label="Options", menu=subMenu)
        #subMenu.add_command(label="Home")
        #subMenu.add_separator()
        subMenu.add_command(label="Exit", command=master.quit)

        self.b1 = Button(self.f, text="Birth Cerificate", relief="raised", width=20,font='Courier 10')
        self.b1.bind("<Button-1>", self.birth)
        self.b1.place(x='60', y='80')

        self.b1 = Button(self.f, text="Income Certificate", relief="raised", width=20 , font='Courier 10')
        self.b1.bind("<Button-1>", self.income)
        self.b1.place(x='60', y='120')

    def birth(self,event):
        db = pymysql.connect("localhost", "root", "root", "adv")
        cursor = db.cursor()
        sql = "SELECT BIRTH FROM cia WHERE UIDAI = {}".format(self.uidai)
        try :
            cursor.execute(sql)
            result=cursor.fetchone()
            if result[0]==0 :
                b=Birth(self.master,self.uidai)
            else :
                print('jerry')
                os.startfile(str(self.uidai)+"b.docx")
                os.startfile(str(self.uidai)+"b.docx","print")
                exit(0)
        except pymysql.Error as e:
            print(e)

    def income(self,event):
            db = pymysql.connect("localhost", "root", "root", "adv")
            cursor = db.cursor()
            sql = "SELECT INCOME FROM cia WHERE UIDAI = {}".format(self.uidai)
            try:
                cursor.execute(sql)
                result = cursor.fetchone()
                if result[0] == 0:
                     i = Income(self.master, self.uidai)
                else:
                    os.startfile(str(self.uidai) + "i.docx")
                    os.startfile(str(self.uidai) + "i.docx", "print")
                    exit(0)

            except pymysql.Error as e:
                print(e)
