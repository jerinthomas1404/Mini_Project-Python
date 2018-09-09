
from tkinter import *
root  = Tk()

class Index:


    def pk(self):
        print("okay")

    def __init__(self, master):
        master.geometry('500x500+650+200')
        master.title("Login Page")
        master.wm_iconbitmap('C:\\Users\\jerin\\OneDrive\\Desktop\\favicon.ico')
        img=PhotoImage(file="C:\\Users\\jerin\\OneDrive\\Desktop\\pic.png")
        self.f = Frame(master, width=1000, height=500)
        self.f.place(x='0', y='0')
        l= Label(self.f, image=img)
        l.image=img
        l.place(x='0', y='0')

        self.l1 = Label(self.f, text=" Enter UIDAI:", borderwidth=10, relief="solid" , width =10)
        self.l1.place(x='30', y='100')
        self.t1 = Entry(self.f, width=20, relief="ridge")
        self.t1.place(x='110', y='100')
        a= (self.t1.get())
        #self.b1 = Button(self.f, text="Submit", relief="solid")
        print(a)

    def display(self, a):

            print("Number :",a)

m=Index(root)
root.mainloop()




