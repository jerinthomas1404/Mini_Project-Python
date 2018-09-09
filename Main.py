import pymysql
from tkinter import *
from tkinter import messagebox
from First import *
root = Tk()
num=0

class Login:


    def __init__(self, master):
        master.geometry('400x400+650+200')
        master.title("Login Page")
        master.wm_iconbitmap('C:\\Users\\jerin\\OneDrive\\Desktop\\favicon.ico')
        self.f = Frame(master, width=400, height=400,background='purple')
        self.f.place(x='0', y='0')
        '''img = PhotoImage(file="C:\\Users\\jerin\\OneDrive\\Desktop\\pic.png")
        l = Label(self.f, image=img)
        l.image = img
        l.place(x='0', y='0')'''
        self.l1 = Label(self.f,text=" Enter UIDAI:", borderwidth=2, relief="flat" , width =14, font='Courier 14')
        self.l1.place(x='20', y='140')
        self.l2=Label(self.f,text="CIA",borderwidth=3,relief='solid',width =10,font='Times 35',background='yellow')
        self.l2.place(x='65',y='30')

        self.t1 = Entry(self.f, width=14,relief="sunken",show='*',font='Courier 14')
        self.t1.place(x='190', y='140')

        self.b1=Button(self.f,text="SUBMIT",relief="raised",width=10)
        self.b1.bind("<Button-1>",self.ins)
        self.b1.place(x='145',y='180')

    def ins(self,event):
        a=self.t1.get()
        if a.isnumeric and len(a)== 12 :

            db = pymysql.connect("localhost", "root", "root", "adv")
            uidai=a
            # prepare a cursor object using cursor() method
            cursor = db.cursor()

            # Prepare SQL query to INSERT a record into the database.
            sql = "INSERT INTO cia(UIDAI)VALUES({})".format(a)

            try:
                # Execute the SQL command
                cursor.execute(sql)
                # Commit your changes in the database
                db.commit()
                h=Home(root,uidai)
            except pymysql.IntegrityError as a:
                db.rollback()
                if a.args[0]==1062 :
                    h=Home(root,uidai)
                    db.commit()
            except pymysql.Error as e:
                db.rollback()
                # Rollback in case there is any error
                print(e)

            # disconnect from server
            db.close()
        else :
            messagebox.showerror("Login Credentials", "Enter 12 digit UIDAI")
            self.t1.delete(0,'end')


l = Login(root)
root.mainloop()
