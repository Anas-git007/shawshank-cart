from tkinter import *
from tkinter.messagebox import showerror, showinfo
from PIL import Image, ImageTk
from datetime import datetime
import ast

class Start(Frame):
    def __init__(self, master,p , *pargs):
        Frame.__init__(self, master, *pargs)

        self.image = Image.open("images/bg.png")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)
        self.p = p
        self.u = User(p)
        

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)

    def login_page(self):
        self.root = Tk()
        self.root.title("SHAWSHANK OFFICIAL - Login Page")
        self.root.iconbitmap("images/ico.ico")
        self.root.geometry("850x400")
        self.root.resizable(False, False)
        bg_image = Image.open("images/bg.png")
        bg_photo = ImageTk.PhotoImage(bg_image)

        # Create a Label widget to display the background image
        bg_label = Label(self.root, image=bg_photo)
        bg_label.place(relwidth=1, relheight=1)
        f1 = Frame(self.root, bg='#e1c1b2', width=100, height=200)
        lab = Label(f1,text='Welcome to Shawshank Official', foreground='black', bg='#e1c1b2',  font=("helvetica", "30", "bold"), pady=15, padx=30)
        lab.pack(anchor='center')
        f1.place(x=100,y=100)
        f2 = Frame(f1, bg='#e1c1b2')
        lab2 = Label(f2,text='username ', foreground='black', bg='#e1c1b2',  font=("helvetica", "15", "bold"))
        lab2.pack(side="left")
        self.username = Entry(f2, bg='white', bd=0, width=30)
        self.username.pack(side="right")
        f2.pack()
        f3 = Frame(f1, bg='#e1c1b2')
        lab3 = Label(f3,text='password ', foreground='black', bg='#e1c1b2',  font=("helvetica", "15", "bold"))
        lab3.pack(side="left")
        self.password = Entry(f3, bg='white', bd=0, width=30)
        self.password.pack(side="right")
        f3.pack()
        f4 = Frame(f1, bg='#e1c1b2')
        lab = Label(f4, foreground='black', bg='#e1c1b2', pady=0.01)
        lab.pack()
        button = Button(f4,text='login', font=("Times ", "12", "bold"), width=10, height=1, fg='white', bg='#bc6c25',activebackground='#e1c1b2', activeforeground='white',command=lambda: [ self.get_username(), self.get_password(), self.u.login_info()] )
        button.pack()
        button2 = Button(f4,text='back', font=("Times ", "12", "bold"), width=10, height=1, fg='white', bg='#bc6c25',activebackground='#e1c1b2', activeforeground='white',
                         command=lambda:[self.root.destroy(), self.signup_page()])
        button2.pack()
        lab = Label(f4, foreground='black', bg='#e1c1b2', pady=0.1)
        lab.pack()
        f4.pack()
        self.root.mainloop()
     
    def get_username(self):
        return self.username.get()   
    def get_password(self):
        return self.password.get()   
        
    def get_window(self):
        return self.root
    
    def signup_page(self):
        self.root = Tk()
        self.root.title("SHAWSHANK OFFICIAL - signup Page")
        self.root.iconbitmap("images/ico.ico")
        self.root.geometry("850x480")
        self.root.resizable(False, False)
        bg_image = Image.open("images/bg.png")
        bg_photo = ImageTk.PhotoImage(bg_image)

        # Create a Label widget to display the background image
        bg_label = Label(self.root, image=bg_photo)
        bg_label.place(relwidth=1, relheight=1)
        f1 = Frame(self.root, bg='#e1c1b2', width=100, height=200)
        lab = Label(f1,text='Welcome to Shawshank Official', foreground='black', bg='#e1c1b2',  font=("helvetica", "30", "bold"), pady=15, padx=30)
        lab.pack(anchor='center')
        f1.place(x=100,y=100)
        f5 = Frame(f1, bg='#e1c1b2')
        lab2 = Label(f5,text='First name ', foreground='black', bg='#e1c1b2',  font=("helvetica", "15", "bold"))
        lab2.pack(side="left")
        Firstname = Entry(f5, bg='white', bd=0, width=30).pack(side="right")
        f5.pack()
        f6 = Frame(f1, bg='#e1c1b2')
        lab2 = Label(f6,text='Last name ', foreground='black', bg='#e1c1b2',  font=("helvetica", "15", "bold"))
        lab2.pack(side="left")
        lastname = Entry(f6, bg='white', bd=0, width=30).pack(side="right")
        f6.pack()
        f2 = Frame(f1, bg='#e1c1b2')
        lab2 = Label(f2,text='Username ', foreground='black', bg='#e1c1b2',  font=("helvetica", "15", "bold"))
        lab2.pack(side="left")
        self.username = Entry(f2, bg='white', bd=0, width=30)
        self.username.pack(side="right")
        f2.pack()
        f3 = Frame(f1, bg='#e1c1b2')
        lab3 = Label(f3,text='Password ', foreground='black', bg='#e1c1b2',  font=("helvetica", "15", "bold"))
        lab3.pack(side="left")
        self.password = Entry(f3, bg='white', bd=0, width=30)
        self.password.pack(side="right")
        f3.pack()
        f4 = Frame(f1, bg='#e1c1b2')
        lab = Label(f4, bg='#e1c1b2', pady=1)
        lab.pack()
        button = Button(f4,text='signup', font=("Times ", "12", "bold"), width=10, height=1, fg='white', bg='#bc6c25',activebackground='#e1c1b2', activeforeground='white', command=lambda: [ self.get_username(), self.get_password(), self.u.signup_info()])
        button.pack()
        lab = Label(f4, bg='#e1c1b2', pady=1)
        lab.pack()
        f4.pack()
        self.root.mainloop()
        
    def DisplayWelcomeMessage(self,r):
        f2 = Frame(r, bg='#e1c1b2').pack()
        f4 = Frame(f2, bg='#e1c1b2')
        b = Button(f4,text='Signup', font=("Times ", "12", "bold"), width=10, height=1, fg='white', bg='#bc6c25',activebackground='#e1c1b2', activeforeground='white',padx=10,pady=10, command=lambda: [r.destroy(), self.signup_page()])
        b.pack()
        lab = Label(f4, foreground='black', bg='#e1c1b2',  font=("helvetica", "30", "bold"), pady=2)
        lab.pack()
        bu = Button(f4,text='Login', font=("Times ", "12", "bold"), width=10, height=1, fg='white', bg='#bc6c25',activebackground='#e1c1b2', activeforeground='white',padx=10,pady=10, command=lambda: [r.destroy(), self.login_page()])
        bu.pack()
        f4.place(x=220, y=130)

class User:
    def __init__(self,p):
        self.p = p
        self.acc = []
        self.f=open('accounts.txt')
        self.f.seek(0)
        self.acc = eval(self.f.read())
        self.f.close()
    def send_username(self, username):
        self.p.receive(username)
    def signup_info(self):
        self.username = s.get_username()
        self.send_username(self.username)
        self.password = s.get_password()
        self.root = s.get_window()
        try:
            for dictionary in self.acc:
                if self.username in dictionary:
                    raise NameError
                elif self.username == '':
                    raise TypeError
                else:
                    if len(self.password) >= 7 and ('0' in self.password or '1' in self.password or '2' in self.password or '3' in self.password or '4' in self.password or '5' in self.password or '6' in self.password or '7' in self.password or '8' in self.password or '9' in self.password) and ('_' in self.password or '-' in self.password or '*' in self.password or '&' in self.password or '^' in self.password or '%' in self.password or '$' in self.password or '#' in self.password or '@' in self.password or '!' in self.password):
                        self.f=open('accounts.txt','w')
                        self.acc.append({self.username:self.password})
                        self.f.write(str(self.acc))
                        self.f.close()
                        self.root.destroy()
                        p.page()
                    else:
                        raise ValueError    
        except ValueError:
            showerror(title='Oops! Error -_-', message='Please Enter Correct password!!\n(Password must have 7 characters, a number and a special character)')
        except TypeError:
            showerror(title='Oops! Error -_-',message='Username is a required field')
        except NameError:
            showerror(title='Oops! Error -_-',message='Username already in use!\nTry different one <3')
        
    def login_info(self):
        self.username = s.get_username()
        self.send_username(self.username)
        self.password = s.get_password()
        self.root = s.get_window()
        username_found = False
        if self.username == '':
            showerror(title='Oops! Error -_-', message='Username is a required field')
            return
        for dictionary in self.acc:
            if self.username in dictionary:
                username_found = True
                if dictionary[self.username] == self.password:
                    showinfo(message='Login successfully! ^_^ ')
                    self.root.destroy()
                    p.page()
                    return
                else:
                    showerror(title='Oops! Error -_-', message='Please Enter Correct password!!')
                    return

        if not username_found:
            showerror(title='Oops! Error -_-', message='There is no username like that kindly sign up :)')
class Product:
    def __init__(self):
        self.get_products()
        self.cart = []
    def receive(self,username):
        self.username = username
    def page(self):   
        r = Tk()
        r.title("SHAWSHANK OFFICIAL - Products")
        r.geometry("1920x1080")
        r.configure(background="#e1c1b2")
        r.resizable(False, False)
        
        f1 = Frame(r,bg='#e1c1b2').place()
        prodno = Label(f1, text = 'S.no', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=0,row=0,padx=1,pady=1)
        prodchk = Label(f1, text = 'Add to cart', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=1,row=0,padx=1,pady=1)
        prodimg = Label(f1, text = 'Image', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=2,row=0,padx=1,pady=1)
        prodname = Label(f1, text = 'Name', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=3,row=0,padx=1,pady=1)
        prodprice = Label(f1, text = 'Price', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=4,row=0,padx=1,pady=1)
        prodstock = Label(f1, text = 'Item in Stock', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=5,row=0,padx=1,pady=1)
        prodtotal = Label(f1, text = 'Total price', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=6,row=0,padx=1,pady=1)
        prodquant = Label(f1, text = 'Quantity', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=7,row=0,padx=1,pady=1)
        interception = Label(f1, text = '-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold")).grid(column=0,row=1,columnspan=8)

        f = Frame(r,bg='#e1c1b2',width=100, height=200).place()
        self.checker1 = IntVar()
        chk_img = Image.open('images/check.png')
        unchk_img = Image.open('images/uncheck.png')
        chk_img = chk_img.resize((30,30))
        unchk_img = unchk_img.resize((30,30))
        chk_p = ImageTk.PhotoImage(chk_img)
        unchk_p = ImageTk.PhotoImage(unchk_img)
        self.Quantity1 = StringVar()
        prodno1 = Label(f, text = '1.', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=0,row=2,padx=1,pady=10)
        chk1 = Checkbutton(f, variable=self.checker1, onvalue=1, offvalue=0,indicatoron=False, image=unchk_p, selectimage=chk_p, bg='#e1c1b2', relief='solid').grid(column=1,row=2,padx=1,pady=10)
        pic1 = Image.open(self.prodlist[0][0])
        pic1 = pic1.resize((100,100))
        pic1 = ImageTk.PhotoImage(pic1)
        prod_1img = Label(f, image=pic1, pady=20, padx=10).grid(column=2,row=2,padx=10,pady=10)
        prod1 = Label(f, text = self.prodlist[0][1], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=3,row=2,padx=1,pady=10)
        prod1_price = Label(f, text = self.prodlist[0][2], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=4,row=2,padx=1,pady=10)
        self.prod1_stock = Label(f, text = self.prodlist[0][3], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10)
        self.prod1_stock.grid(column=5,row=2,padx=1,pady=10)
        prod1_quantity = Spinbox(f, from_=0, to=10, width=10, relief="sunken", repeatdelay=500, repeatinterval=100, textvariable=self.Quantity1, font=("Arial", 12), bg="#e1c1b2", fg="black",justify='center').grid(column=7,row=2,padx=1,pady=10)
        self.prod1_total = Label(f, text=self.Quantity1.get(), foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=2, padx=1)
        self.prod1_total.grid(column=6,row=2,padx=1,pady=1)
        self.Quantity1.trace_add('write', self.update_label1)
        
        interception = Label(f, text = '-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold")).grid(column=0,row=3,columnspan=8)
    # Product 2
        f2 = Frame(r,bg='#e1c1b2',width=100, height=200).place()
        self.checker2 = IntVar()
        chk_img2 = Image.open('images/check.png')
        unchk_img2 = Image.open('images/uncheck.png')
        chk_img2 = chk_img2.resize((30,30))
        unchk_img2 = unchk_img2.resize((30,30))
        chk_p2 = ImageTk.PhotoImage(chk_img2)
        unchk_p2 = ImageTk.PhotoImage(unchk_img2)
        self.Quantity2 = StringVar()
        prodno2 = Label(f2, text = '2.', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=0,row=4,padx=1,pady=10)
        chk2 = Checkbutton(f2, variable=self.checker2, onvalue=1, offvalue=0,indicatoron=False, image=unchk_p2, selectimage=chk_p2, bg='#e1c1b2', relief='solid').grid(column=1,row=4,padx=1,pady=10)
        pic2 = Image.open(self.prodlist[1][0])
        pic2 = pic2.resize((100,100))
        pic2 = ImageTk.PhotoImage(pic2)
        prod_2img = Label(f2, image=pic2, pady=20, padx=10, bg='#e1c1b2').grid(column=2,row=4,padx=10,pady=10)
        prod2 = Label(f2, text = self.prodlist[1][1], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=3,row=4,padx=1,pady=10)
        prod2_price = Label(f2, text = self.prodlist[1][2], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=4,row=4,padx=1,pady=10)
        self.prod2_stock = Label(f2, text = self.prodlist[1][3], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10)
        self.prod2_stock.grid(column=5,row=4,padx=1,pady=10)
        prod2_quantity = Spinbox(f2, from_=0, to=10, width=10, relief="sunken", repeatdelay=500, repeatinterval=100, textvariable=self.Quantity2, font=("Arial", 12), bg="#e1c1b2", fg="black",justify='center').grid(column=7,row=4,padx=1,pady=10)
        self.prod2_total = Label(f2, text=self.Quantity2.get(), foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=2, padx=1)
        self.prod2_total.grid(column=6,row=4,padx=1,pady=1)
        self.Quantity2.trace_add('write', self.update_label2)

        interception = Label(f, text = '-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold")).grid(column=0,row=5,columnspan=8)
    #product 3
        f3 = Frame(r,bg='#e1c1b2',width=100, height=200).place()
        self.checker3 = IntVar()
        chk_img3 = Image.open('images/check.png')
        unchk_img3 = Image.open('images/uncheck.png')
        chk_img3 = chk_img3.resize((30,30))
        unchk_img3 = unchk_img3.resize((30,30))
        chk_p3 = ImageTk.PhotoImage(chk_img3)
        unchk_p3 = ImageTk.PhotoImage(unchk_img3)
        self.Quantity3 = StringVar()
        prodno3 = Label(f3, text = '3.', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=0,row=6,padx=1,pady=10)
        chk3 = Checkbutton(f3, variable=self.checker3, onvalue=1, offvalue=0,indicatoron=False, image=unchk_p3, selectimage=chk_p3, bg='#e1c1b2', relief='solid').grid(column=1,row=6,padx=1,pady=10)
        pic3 = Image.open(self.prodlist[2][0])
        pic3 = pic3.resize((100,100))
        pic3 = ImageTk.PhotoImage(pic3)
        prod_3img = Label(f3, image=pic3, pady=20, padx=10, bg='#e1c1b2').grid(column=2,row=6,padx=10,pady=10)
        prod3 = Label(f3, text = self.prodlist[2][1], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=3,row=6,padx=1,pady=10)
        prod3_price = Label(f3, text = self.prodlist[2][2], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=4,row=6,padx=1,pady=10)
        self.prod3_stock = Label(f3, text = self.prodlist[2][3], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10)
        self.prod3_stock.grid(column=5,row=6,padx=1,pady=10)
        prod3_quantity = Spinbox(f3, from_=0, to=10, width=10, relief="sunken", repeatdelay=500, repeatinterval=100, textvariable=self.Quantity3, font=("Arial", 12), bg="#e1c1b2", fg="black",justify='center').grid(column=7,row=6,padx=1,pady=10)
        self.prod3_total = Label(f3, text=self.Quantity3.get(), foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=2, padx=1)
        self.prod3_total.grid(column=6,row=6,padx=1,pady=1)
        self.Quantity3.trace_add('write', self.update_label3)
        
        interception = Label(f, text = '-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold")).grid(column=0,row=7,columnspan=8)
    #product 4
        f4 = Frame(r,bg='#e1c1b2',width=100, height=200).place()
        self.checker4 = IntVar()
        chk_img4 = Image.open('images/check.png')
        unchk_img4 = Image.open('images/uncheck.png')
        chk_img4 = chk_img4.resize((30,30))
        unchk_img4 = unchk_img4.resize((30,30))
        chk_p4 = ImageTk.PhotoImage(chk_img4)
        unchk_p4 = ImageTk.PhotoImage(unchk_img4)
        self.Quantity4 = StringVar()
        prodno4 = Label(f4, text = '4.', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=0,row=8,padx=1,pady=10)
        chk4 = Checkbutton(f, variable=self.checker4, onvalue=1, offvalue=0,indicatoron=False, image=unchk_p4, selectimage=chk_p4, bg='#e1c1b2', relief='solid').grid(column=1,row=8,padx=1,pady=10)
        pic4 = Image.open(self.prodlist[3][0])
        pic4 = pic4.resize((120,150))
        pic4 = ImageTk.PhotoImage(pic4)
        prod_4img = Label(f4, image=pic4, pady=20, padx=10, bg='#e1c1b2').grid(column=2,row=8,padx=10,pady=10)
        prod4 = Label(f4, text = self.prodlist[3][1], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=3,row=8, padx=1,pady=10)
        prod4_price = Label(f4, text = self.prodlist[3][2], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=4,row=8,padx=1,pady=10)
        self.prod4_stock = Label(f4, text = self.prodlist[3][3], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10)
        self.prod4_stock.grid(column=5,row=8,padx=1,pady=10)
        prod1_quantity = Spinbox(f4, from_=0, to=10, width=10, relief="sunken", repeatdelay=500, repeatinterval=100, textvariable=self.Quantity4, font=("Arial", 12), bg="#e1c1b2", fg="black",justify='center').grid(column=7,row=8,padx=1,pady=10)
        self.prod4_total = Label(f4, text=self.Quantity4.get(), foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=2, padx=1)
        self.prod4_total.grid(column=6,row=8,padx=1,pady=1)
        self.Quantity4.trace_add('write', self.update_label4)
        
        interception = Label(f, text = '-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold")).grid(column=0,row=9,columnspan=8)
    #product 5
        f5 = Frame(r,bg='#e1c1b2',width=100, height=200).place()
        self.checker5 = IntVar()
        chk_img5 = Image.open('images/check.png')
        unchk_img5 = Image.open('images/uncheck.png')
        chk_img5 = chk_img5.resize((30,30))
        unchk_img5 = unchk_img5.resize((30,30))
        chk_p5 = ImageTk.PhotoImage(chk_img5)
        unchk_p5 = ImageTk.PhotoImage(unchk_img5)
        self.Quantity5 = StringVar()
        prodno5 = Label(f5, text = '5.', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=0,row=10,padx=1,pady=10)
        chk5 = Checkbutton(f5, variable=self.checker5, onvalue=1, offvalue=0,indicatoron=False, image=unchk_p5, selectimage=chk_p5, bg='#e1c1b2', relief='solid').grid(column=1,row=10,padx=1,pady=10)
        pic5 = Image.open(self.prodlist[4][0])
        pic5 = pic5.resize((100,100))
        pic5 = ImageTk.PhotoImage(pic5)
        prod_5img = Label(f, image=pic5, pady=20, padx=10, bg='#e1c1b2').grid(column=2,row=10,padx=10,pady=10)
        prod5 = Label(f5, text = self.prodlist[4][1], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=3,row=10,padx=1,pady=10)
        prod5_price = Label(f5, text = self.prodlist[4][2], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=4,row=10,padx=1,pady=10)
        self.prod5_stock = Label(f5, text = self.prodlist[4][3], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10)
        self.prod5_stock.grid(column=5,row=10,padx=1,pady=10)
        prod5_quantity = Spinbox(f5, from_=0, to=10, width=10, relief="sunken", repeatdelay=500, repeatinterval=100, textvariable=self.Quantity5, font=("Arial", 12), bg="#e1c1b2", fg="black",justify='center').grid(column=7,row=10,padx=1,pady=10)
        self.prod5_total = Label(f5, text=self.Quantity5.get(), foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=2, padx=1)
        self.prod5_total.grid(column=6,row=10,padx=1,pady=1)
        self.Quantity5.trace_add('write', self.update_label5)
        
        interception = Label(f, text = '-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold")).grid(column=0,row=11,columnspan=8)
        Btn = Button(f,text='Next', font=("Times ", "12", "bold"),width=10, fg='white', bg='#bc6c25',activebackground='#e1c1b2', activeforeground='white',padx=10,pady=10, command=lambda: [r.destroy(),self.add_to_cart1(), self.otherpage()]).grid(column=3,row=12,columnspan=2)
        r.mainloop()
        
    def otherpage(self):
    # product 6
        self.r = Tk()
        self.r.title("SHAWSHANK OFFICIAL - Products")
        self.r.geometry("1920x1080")
        self.r.configure(background="#e1c1b2")   
        self.r.resizable(False, False) 
        f1 = Frame(self.r,bg='#e1c1b2').place()
        prodno = Label(f1, text = 'S.no', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=0,row=0,padx=1,pady=1)
        prodchk = Label(f1, text = 'Add to cart', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=1,row=0,padx=1,pady=1)
        prodimg = Label(f1, text = 'Image', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=2,row=0,padx=1,pady=1)
        prodname = Label(f1, text = 'Name', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=3,row=0,padx=1,pady=1)
        prodprice = Label(f1, text = 'Price', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=4,row=0,padx=1,pady=1)
        prodstock = Label(f1, text = 'Item in Stock', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=5,row=0,padx=1,pady=1)
        prodtotal = Label(f1, text = 'Total price', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=6,row=0,padx=1,pady=1)
        prodquant = Label(f1, text = 'Quantity', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=7,row=0,padx=1,pady=1)
        interception = Label(f1, text = '-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold")).grid(column=0,row=1,columnspan=8)

        f6 = Frame(self.r,bg='#e1c1b2',width=100, height=200).place()
        self.checker6 = IntVar()
        chk_img6 = Image.open('images/check.png')
        unchk_img6 = Image.open('images/uncheck.png')
        chk_img6 = chk_img6.resize((30,30))
        unchk_img6 = unchk_img6.resize((30,30))
        chk_p6 = ImageTk.PhotoImage(chk_img6)
        unchk_p6 = ImageTk.PhotoImage(unchk_img6)
        self.Quantity6 = StringVar()
        prodno6 = Label(f6, text = '6.', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=0,row=12,padx=1,pady=10)
        chk6 = Checkbutton(f6, variable=self.checker6, onvalue=1, offvalue=0,indicatoron=False, image=unchk_p6, selectimage=chk_p6, bg='#e1c1b2', relief='solid').grid(column=1,row=12,padx=1,pady=10)
        pic6 = Image.open(self.prodlist[5][0])
        pic6 = pic6.resize((100,100))
        pic6 = ImageTk.PhotoImage(pic6)
        prod_6img = Label(f6, image=pic6, pady=20, padx=10, bg='#e1c1b2').grid(column=2,row=12,padx=10,pady=10)
        prod6 = Label(f6, text = self.prodlist[5][1], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=3,row=12,padx=1,pady=10)
        prod6_price = Label(f6, text = self.prodlist[5][2], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=4,row=12,padx=1,pady=10)
        self.prod6_stock = Label(f6, text = self.prodlist[5][3], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10)
        self.prod6_stock.grid(column=5,row=12,padx=1,pady=10)
        prod6_quantity = Spinbox(f6, from_=0, to=10, width=10, relief="sunken", repeatdelay=500, repeatinterval=100, textvariable=self.Quantity6, font=("Arial", 12), bg="#e1c1b2", fg="black",justify='center').grid(column=7,row=12,padx=1,pady=10)
        self.prod6_total = Label(f6, text=self.Quantity6.get(), foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=2, padx=1)
        self.prod6_total.grid(column=6,row=12,padx=1,pady=1)
        self.Quantity6.trace_add('write', self.update_label6)
        
        interception = Label(f6, text = '-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold")).grid(column=0,row=13,columnspan=8)
        
    # product 7
        f7 = Frame(self.r,bg='#e1c1b2',width=100, height=200).place()
        self.checker7 = IntVar()
        chk_img7 = Image.open('images/check.png')
        unchk_img7 = Image.open('images/uncheck.png')
        chk_img7 = chk_img7.resize((30,30))
        unchk_img7 = unchk_img7.resize((30,30))
        chk_p7 = ImageTk.PhotoImage(chk_img7)
        unchk_p7 = ImageTk.PhotoImage(unchk_img7)
        self.Quantity7 = StringVar()
        prodno7 = Label(f7, text = '7.', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=0,row=14,padx=1,pady=10)
        chk7 = Checkbutton(f7, variable=self.checker7, onvalue=1, offvalue=0,indicatoron=False, image=unchk_p7, selectimage=chk_p7, bg='#e1c1b2', relief='solid').grid(column=1,row=14,padx=1,pady=10)
        pic7 = Image.open(self.prodlist[6][0])
        pic7 = pic7.resize((100,100))
        pic7 = ImageTk.PhotoImage(pic7)
        prod_7img = Label(f7, image=pic7, pady=20, padx=10, bg='#e1c1b2').grid(column=2,row=14,padx=10,pady=10)
        prod7 = Label(f7, text = self.prodlist[6][1], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=3,row=14,padx=1,pady=10)
        prod7_price = Label(f7, text = self.prodlist[6][2], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=4,row=14,padx=1,pady=10)
        self.prod7_stock = Label(f7, text = self.prodlist[6][3], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10)
        self.prod7_stock.grid(column=5,row=14,padx=1,pady=10)
        prod7_quantity = Spinbox(f7, from_=0, to=10, width=10, relief="sunken", repeatdelay=500, repeatinterval=100, textvariable=self.Quantity7, font=("Arial", 12), bg="#e1c1b2", fg="black",justify='center').grid(column=7,row=14,padx=1,pady=10)
        self.prod7_total = Label(f7, text=self.Quantity7.get(), foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=2, padx=1)
        self.prod7_total.grid(column=6,row=14,padx=1,pady=1)
        self.Quantity7.trace_add('write', self.update_label7)
        
        interception = Label(f7, text = '-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold")).grid(column=0,row=15,columnspan=8)
        
    # product 8   
        f8 = Frame(self.r,bg='#e1c1b2',width=100, height=200).place()
        self.checker8 = IntVar()
        chk_img8 = Image.open('images/check.png')
        unchk_img8 = Image.open('images/uncheck.png')
        chk_img8 = chk_img8.resize((30,30))
        unchk_img8 = unchk_img8.resize((30,30))
        chk_p8 = ImageTk.PhotoImage(chk_img8)
        unchk_p8 = ImageTk.PhotoImage(unchk_img8)
        self.Quantity8 = StringVar()
        prodno8 = Label(f8, text = '8.', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=0,row=16,padx=1,pady=10)
        chk8 = Checkbutton(f8, variable=self.checker8, onvalue=1, offvalue=0,indicatoron=False, image=unchk_p8, selectimage=chk_p8, bg='#e1c1b2', relief='solid').grid(column=1,row=16,padx=1,pady=10)
        pic8 = Image.open(self.prodlist[7][0])
        pic8 = pic8.resize((100,100))
        pic8 = ImageTk.PhotoImage(pic8)
        prod_8img = Label(f8, image=pic8, pady=20, padx=10, bg='#e1c1b2').grid(column=2,row=16,padx=10,pady=10)
        prod8 = Label(f8, text = self.prodlist[7][1], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=3,row=16,padx=1,pady=10)
        prod8_price = Label(f8, text = self.prodlist[7][2], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=4,row=16,padx=1,pady=10)
        self.prod8_stock = Label(f8, text = self.prodlist[7][3], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10)
        self.prod8_stock.grid(column=5,row=16,padx=1,pady=10)
        prod1_quantity8 = Spinbox(f8, from_=0, to=10, width=10, relief="sunken", repeatdelay=500, repeatinterval=100, textvariable=self.Quantity8, font=("Arial", 12), bg="#e1c1b2", fg="black",justify='center').grid(column=7,row=16,padx=1,pady=10)
        self.prod8_total = Label(f8, text=self.Quantity8.get(), foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=2, padx=1)
        self.prod8_total.grid(column=6,row=16,padx=1,pady=1)
        self.Quantity8.trace_add('write', self.update_label8)
        
        interception = Label(f8, text = '-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold")).grid(column=0,row=17,columnspan=8)
        
        f9 = Frame(self.r,bg='#e1c1b2',width=100, height=200).place()
        self.checker9 = IntVar()
        chk_img9 = Image.open('images/check.png')
        unchk_img9 = Image.open('images/uncheck.png')
        chk_img9 = chk_img9.resize((30,30))
        unchk_img9 = unchk_img9.resize((30,30))
        chk_p9 = ImageTk.PhotoImage(chk_img9)
        unchk_p9 = ImageTk.PhotoImage(unchk_img9)
        self.Quantity9 = StringVar()
        prodno9 = Label(f9, text = '9.', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=0,row=18,padx=1,pady=10)
        chk9 = Checkbutton(f9, variable=self.checker9, onvalue=1, offvalue=0,indicatoron=False, image=unchk_p9, selectimage=chk_p9, bg='#e1c1b2', relief='solid').grid(column=1,row=18,padx=1,pady=10)
        pic9 = Image.open(self.prodlist[8][0])
        pic9 = pic9.resize((100,100))
        pic9 = ImageTk.PhotoImage(pic9)
        prod_9img = Label(f9, image=pic9, pady=20, padx=10, bg='#e1c1b2').grid(column=2,row=18,padx=10,pady=10)
        prod9 = Label(f9, text = self.prodlist[8][1], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=3,row=18,padx=1,pady=10)
        prod9_price = Label(f9, text = self.prodlist[8][2], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=4,row=18,padx=1,pady=10)
        self.prod9_stock = Label(f9, text = self.prodlist[8][3], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10)
        self.prod9_stock.grid(column=5,row=18,padx=1,pady=10)
        prod9_quantity = Spinbox(f9, from_=0, to=10, width=10, relief="sunken", repeatdelay=500, repeatinterval=100, textvariable=self.Quantity9, font=("Arial", 12), bg="#e1c1b2", fg="black",justify='center').grid(column=7,row=18,padx=1,pady=10)
        self.prod9_total = Label(f9, text=self.Quantity9.get(), foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=2, padx=1)
        self.prod9_total.grid(column=6,row=18,padx=1,pady=1)
        self.Quantity9.trace_add('write', self.update_label9)
    
               
        interception = Label(f8, text = '-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold")).grid(column=0,row=19,columnspan=8)
        
        
        f10 = Frame(self.r,bg='#e1c1b2',width=100, height=200).place()
        self.checker10 = IntVar()
        chk_img10 = Image.open('images/check.png')
        unchk_img10 = Image.open('images/uncheck.png')
        chk_img10 = chk_img10.resize((30,30))
        unchk_img10 = unchk_img10.resize((30,30))
        chk_p10 = ImageTk.PhotoImage(chk_img10)
        unchk_p10 = ImageTk.PhotoImage(unchk_img10)
        self.Quantity10 = StringVar()
        prodno10 = Label(f10, text = '10.', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=0,row=20,padx=1,pady=10)
        chk10 = Checkbutton(f10, variable=self.checker10, onvalue=1, offvalue=0,indicatoron=False, image=unchk_p10, selectimage=chk_p10, bg='#e1c1b2', relief='solid').grid(column=1,row=20,padx=1,pady=10)
        pic10 = Image.open(self.prodlist[9][0])
        pic10 = pic10.resize((100,100))
        pic10 = ImageTk.PhotoImage(pic10)
        prod_10img = Label(f10, image=pic10, pady=20, padx=10, bg='#e1c1b2').grid(column=2,row=20,padx=10,pady=10)
        prod10 = Label(f10, text = self.prodlist[9][1], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=3,row=20,padx=1,pady=10)
        prod10_price = Label(f10, text = self.prodlist[9][2], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=4,row=20,padx=1,pady=10)
        self.prod10_stock = Label(f10, text = self.prodlist[9][3], foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10)
        self.prod10_stock.grid(column=5,row=20,padx=1,pady=10)
        prod10_quantity = Spinbox(f10, from_=0, to=10, width=10, relief="sunken", repeatdelay=500, repeatinterval=100, textvariable=self.Quantity10, font=("Arial", 12), bg="#e1c1b2", fg="black",justify='center').grid(column=7,row=20,padx=1,pady=10)
        self.prod10_total = Label(f10, text=self.Quantity10.get(), foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=2, padx=1)
        self.prod10_total.grid(column=6,row=20,padx=1,pady=1)
        self.Quantity10.trace_add('write', self.update_label10)
        
        interception = Label(f8, text = '-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold")).grid(column=0,row=21,columnspan=8)
        
        Btn = Button(f10,text='back', font=("Times ", "12", "bold"),width=10, fg='white', bg='#bc6c25',activebackground='#e1c1b2', activeforeground='white',padx=10,pady=10, command=lambda: [self.r.destroy(), self.page()]).grid(column=3,row=22)
        
        Btn2 = Button(f10,text='View cart', font=("Times ", "12", "bold"),width=10, fg='white', bg='#bc6c25',activebackground='#e1c1b2', activeforeground='white',padx=10,pady=10, command=lambda: [self.add_to_cart2(),self.return_cart(), self.create_instance()]).grid(column=4,row=22)
        
        self.r.mainloop()
    def create_instance(self):
        try:
            if len(self.cart) == 0:
                    raise Exception
            for i in range(len(self.cart)):
                if self.cart[i][1] == "0":
                    del self.cart[i]
                    raise Exception
                    
            self.r.destroy()
            myCart = Cart(self,self.cart,self.username)
                
                
        except Exception:
            showerror(title='Oops! Error -_-', message='There is nothing in the cart :)\nOr Any product has 0 quantity selected!!')
            
    def update_label1(self,*args):
        self.prod1_total.config(text = int(self.prodlist[0][2]) * int(self.Quantity1.get()))
        self.prod1_stock.config(text= int(self.prodlist[0][3]) - int(self.Quantity1.get()))
    
    def update_label2(self,*args):
        self.prod2_total.config(text = int(self.prodlist[1][2]) * int(self.Quantity2.get()))
        self.prod2_stock.config(text= int(self.prodlist[1][3]) - int(self.Quantity2.get()))
    
    def update_label3(self,*args):
        self.prod3_total.config(text = int(self.prodlist[2][2]) * int(self.Quantity3.get()))
        self.prod3_stock.config(text= int(self.prodlist[2][3]) - int(self.Quantity3.get()))
    
    def update_label4(self,*args):
        self.prod4_total.config(text = int(self.prodlist[3][2]) * int(self.Quantity4.get()))
        self.prod4_stock.config(text= int(self.prodlist[3][3]) - int(self.Quantity4.get()))
    def update_label5(self,*args):
        self.prod5_total.config(text = int(self.prodlist[4][2]) * int(self.Quantity5.get()))
        self.prod5_stock.config(text= int(self.prodlist[4][3]) - int(self.Quantity5.get()))
    
    def update_label6(self,*args):
        self.prod6_total.config(text = int(self.prodlist[5][2]) * int(self.Quantity6.get()))
        self.prod6_stock.config(text= int(self.prodlist[5][3]) - int(self.Quantity6.get()))
    
    def update_label7(self,*args):
        self.prod7_total.config(text = int(self.prodlist[6][2]) * int(self.Quantity7.get()))
        self.prod7_stock.config(text= int(self.prodlist[6][3]) - int(self.Quantity7.get()))
    
    def update_label8(self,*args):
        self.prod8_total.config(text = int(self.prodlist[7][2]) * int(self.Quantity8.get()))
        self.prod8_stock.config(text= int(self.prodlist[7][3]) - int(self.Quantity8.get()))

    def update_label9(self,*args):
        self.prod9_total.config(text = int(self.prodlist[8][2]) * int(self.Quantity9.get()))
        self.prod9_stock.config(text= int(self.prodlist[8][3]) - int(self.Quantity9.get()))
    
    def update_label10(self,*args):
        self.prod10_total.config(text = int(self.prodlist[9][2]) * int(self.Quantity10.get()))
        self.prod10_stock.config(text= int(self.prodlist[9][3]) - int(self.Quantity10.get()))
    
    def add_to_cart1(self):
        checkers = [self.checker1, self.checker2, self.checker3, self.checker4, self.checker5]
        quant = [self.Quantity1.get(), self.Quantity2.get(), self.Quantity3.get(), self.Quantity4.get(), self.Quantity5.get()]
        for i, checker in enumerate(checkers):
            if checker.get() == 1:
                self.cart.append([self.prodlist[i],quant[i]])
    
    def add_to_cart2(self):
        checkers = ['','','','','',self.checker6.get(), self.checker7.get(), self.checker8.get(), self.checker9.get(), self.checker10.get()]
        quant = ['','','','','',self.Quantity6.get(), self.Quantity7.get(), self.Quantity8.get(), self.Quantity9.get(), self.Quantity10.get()]
        for i, checker in enumerate(checkers):
            if checker == 1:
                self.cart.append([self.prodlist[i],quant[i]])
    
    def return_cart(self):
        return self.cart        
    
    def get_products(self):
        f=open('productlist.txt')
        self.prodlist = eval(f.read())
        f.close()
        
class Cart:
    def __init__(self, p, cart,username):
        self.hist = []
        self.cart = cart
        self.prod = p
        self.username = username
        self.ViewCart()
    def ViewCart(self):
        self.root = Tk()
        self.root.title("SHAWSHANK OFFICIAL-Cart")
        self.root.geometry("1400x1200")
        self.root.configure(background="#e1c1b2")
        self.root.resizable(False, True)
                # Create a canvas and a scrollbar
        canvas = Canvas(self.root, bg="#e1c1b2")
        scrollbar = Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg="#e1c1b2")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Placing widgets inside the scrollable frame
        f1 = Frame(scrollable_frame, bg="#e1c1b2")
        f1.pack()
        #f1 = Frame(self.root).place()
        prodsno = Label(f1, text = 'S.no', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=0,row=0,padx=1,pady=1)
        prodimg = Label(f1, text = 'Image', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=1,row=0,padx=1,pady=1)
        prodname = Label(f1, text = 'Name', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=2,row=0,padx=1,pady=1)
        prodprice = Label(f1, text = 'Price', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=3,row=0,padx=1,pady=1)
        prodquant = Label(f1, text = 'Quantity', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=4,row=0,padx=1,pady=1)
        prodtotal = Label(f1, text = 'Total price', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10).grid(column=5,row=0,padx=1,pady=1)
        
        labels = {
            'prodsno': {},
            'pic': {},
            'prodimg': {},
            'prodname': {},
            'prodprice': {},
            'prodquant': {},
            'prodtotal': {},
            'button': {}
        }
        
        total_amount = 0
        for i in range(len(self.cart)):
            labels['pic'][i] = Image.open(self.cart[i][0][0])
            labels['pic'][i] = labels['pic'][i].resize((100, 100))
            labels['pic'][i] = ImageTk.PhotoImage(labels['pic'][i])
            labels['prodimg'][i] = Label(f1, image=labels['pic'][i], bg='#e1c1b2')
            labels['prodimg'][i].image = labels['pic'][i]  # Keep a reference to the image to avoid garbage collection
            labels['prodsno'][i] = Label(f1, text = i+1, foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10)
            labels['prodname'][i] = Label(f1, text=self.cart[i][0][1], foreground='black', bg='#e1c1b2', font=("Times", "15", "bold"), pady=20, padx=10)
            labels['prodprice'][i] = Label(f1, text=self.cart[i][0][2], foreground='black', bg='#e1c1b2', font=("Times", "15", "bold"), pady=20, padx=10)
            labels['prodquant'][i] = Label(f1, text=self.cart[i][1], foreground='black', bg='#e1c1b2', font=("Times", "15", "bold"), pady=20, padx=10)
            product_total = int(self.cart[i][0][2]) * int(self.cart[i][1])
            total_amount += product_total
            labels['prodtotal'][i] = Label(f1, text=product_total, foreground='black', bg='#e1c1b2', font=("Times", "15", "bold"), pady=20, padx=10)
            labels['button'][i] = Button(f1, text='Remove', font=("Times", "12", "bold"), width=8, fg='white', bg='#bc6c25', activebackground='#e1c1b2', activeforeground='white', padx=2, pady=2,command=lambda i=i: self.remove_product(i))
            
            # Place labels in the grid
            row = 2 * i
            labels['prodsno'][i].grid(row=row+2, column=0, padx=1, pady=1)
            labels['prodimg'][i].grid(row=row+2, column=1, padx=1, pady=1)
            labels['prodname'][i].grid(row=row+2, column=2, padx=1, pady=1)
            labels['prodprice'][i].grid(row=row+2, column=3, padx=1, pady=1)
            labels['prodquant'][i].grid(row=row+2, column=4, padx=1, pady=1)
            labels['prodtotal'][i].grid(row=row+2, column=5, padx=1, pady=1)
            labels['button'][i].grid(row=row+2, column=6, padx=1, pady=1)
            
            # Add interception line
            Label(f1, text='-' * 160, foreground='black', bg='#e1c1b2', font=("Times", "15", "bold")).grid(column=0, row=row+1, columnspan=8)
        # Calculate total amount with tax
        tax = total_amount * 0.05
        total_with_tax = total_amount + tax

        # Display the total amount and tax
        total_label = Label(f1, text=f"Payable Amount: {total_amount} + Tax (5%): {tax:.2f} = {total_with_tax:.2f}", foreground='black', bg='#e1c1b2', font=("Times", "15", "bold"), pady=20, padx=10)
        total_label.grid(row=3*len(self.cart), column=0, columnspan=6)
        
        Btn = Button(f1,text='back', font=("Times ", "12", "bold"),width=10, fg='white', bg='#bc6c25',activebackground='#e1c1b2', activeforeground='white',padx=10,pady=10, command=lambda: [self.root.destroy(), self.prod.otherpage() ]).grid(column=2,row=4*len(self.cart))
        
        Btn2 = Button(f1,text='checkout', font=("Times ", "12", "bold"),width=10, fg='white', bg='#bc6c25',activebackground='#e1c1b2', activeforeground='white',padx=10,pady=10, command=lambda: [self.root.destroy(), self.shophist(), checkout(self.username,self.prod,self.hist)]).grid(column=3,row=4*len(self.cart))
        
        root.mainloop()
    def remove_product(self, index):
        # Remove the product from the cart
        del self.cart[index]
        self.root.destroy()
        # Refresh the widgets
        if len(self.cart) != 0:
            self.ViewCart()
        else:
            showinfo(title='Shawshank Official', message='There is nothing left in the cart\nShop again :\\')
            self.prod.page()
 

    def shophist(self):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            with open(f'history/history {self.username}.txt', 'r') as file:
                existing_content = file.read()
                # Convert existing content back to a list of lists
                if existing_content:
                    self.hist = eval(existing_content)
        except FileNotFoundError:
        # If file doesn't exist, start with an empty list
            self.hist = []
        for item in self.cart:
            item_with_timestamp = item + [timestamp]
            self.hist.append(item_with_timestamp)
        with open(f'history/history {self.username}.txt', 'w') as file:
            file.write(str(self.hist))
class checkout(Cart):
    def __init__(self,username,prod,hist):
        self.hist = hist
        self.username = username
        self.prod = prod
        root = Tk()
        root.title("SHAWSHANK OFFICIAL - Checkout")
        root.geometry("800x400")
        root.configure(background="#e1c1b2")
        root.resizable(False, False)
        bg_image = Image.open("images/bg.png")
        bg_photo = ImageTk.PhotoImage(bg_image)
        root.bg_photo = bg_photo
        # Create a Label widget to display the background image
        bg_label = Label(root, image=bg_photo)
        bg_label.place(relwidth=1, relheight=1)
        #f2 = Frame(root, bg='#e1c1b2').place(x=220, y=130)
        f4 = Frame(root, bg='#e1c1b2')
        b = Button(f4,text='View Shopping History', font=("Times ", "12", "bold"), width=25, height=1, fg='white', bg='#bc6c25',activebackground='#e1c1b2', activeforeground='white',padx=10,pady=10, command=lambda: [root.destroy(), self.shop_hist()])
        b.pack()
        lab = Label(f4, foreground='black', bg='#e1c1b2',  font=("helvetica", "15", "bold"), pady=2)
        lab.pack()
        bu = Button(f4,text='Start Shopping again', font=("Times ", "12", "bold"), width=25, height=1, fg='white', bg='#bc6c25',activebackground='#e1c1b2', activeforeground='white',padx=10,pady=10, command=lambda: [root.destroy(), self.prod.page()])
        bu.pack()
        lab2 = Label(f4, foreground='black', bg='#e1c1b2',  font=("helvetica", "15", "bold"), pady=2)
        lab2.pack()
        but = Button(f4,text='Exit', font=("Times ", "12", "bold"), width=10, height=1, fg='white', bg='#bc6c25',activebackground='#e1c1b2', activeforeground='white',padx=10,pady=10, command= lambda: [root.destroy()])
        but.pack()
        f4.place(x=220, y=130)
    
    def shop_hist(self):
        self.root = Tk()
        self.root.title("SHAWSHANK OFFICIAL-Shopping History")
        self.root.geometry("1200x1400")
        self.root.configure(background="#e1c1b2")
        self.root.resizable(False, True)

        # Create a canvas and a scrollbar
        canvas = Canvas(self.root, bg="#e1c1b2")
        scrollbar = Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg="#e1c1b2")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Placing widgets inside the scrollable frame
        f1 = Frame(scrollable_frame, bg="#e1c1b2")
        f1.pack()

        labels = {
            'prodsno': {},
            'pic': {},
            'prodimg': {},
            'prodname': {},
            'prodprice': {},
            'prodquant': {},
            'prodtotal': {},
            'prodtime': {},
        }

        prodsno = Label(f1, text='S.no', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10)
        prodimg = Label(f1, text='Image', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10)
        prodname = Label(f1, text='Name', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10)
        prodprice = Label(f1, text='Price', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10)
        prodquant = Label(f1, text='Quantity', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10)
        prodtotal = Label(f1, text='Total price', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10)
        prodtime = Label(f1, text='Time n Date', foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10)

        prodsno.grid(column=0, row=0, padx=1, pady=1)
        prodimg.grid(column=1, row=0, padx=1, pady=1)
        prodname.grid(column=2, row=0, padx=1, pady=1)
        prodprice.grid(column=3, row=0, padx=1, pady=1)
        prodquant.grid(column=4, row=0, padx=1, pady=1)
        prodtotal.grid(column=5, row=0, padx=1, pady=1)
        prodtime.grid(column=6, row=0, padx=1, pady=1)

        total_amount = 0
        for i in range(len(self.hist)):
            labels['pic'][i] = Image.open(self.hist[i][0][0])
            labels['pic'][i] = labels['pic'][i].resize((100, 100))
            labels['pic'][i] = ImageTk.PhotoImage(labels['pic'][i])
            labels['prodimg'][i] = Label(f1, image=labels['pic'][i], bg='#e1c1b2')
            labels['prodimg'][i].image = labels['pic'][i]  # Keep a reference to the image to avoid garbage collection
            labels['prodsno'][i] = Label(f1, text=i+1, foreground='black', bg='#e1c1b2',  font=("Times", "15", "bold"), pady=20, padx=10)
            labels['prodname'][i] = Label(f1, text=self.hist[i][0][1], foreground='black', bg='#e1c1b2', font=("Times", "15", "bold"), pady=20, padx=10)
            labels['prodprice'][i] = Label(f1, text=self.hist[i][0][2], foreground='black', bg='#e1c1b2', font=("Times", "15", "bold"), pady=20, padx=10)
            labels['prodquant'][i] = Label(f1, text=self.hist[i][1], foreground='black', bg='#e1c1b2', font=("Times", "15", "bold"), pady=20, padx=10)
            product_total = int(self.hist[i][0][2]) * int(self.hist[i][1])
            total_amount += product_total
            labels['prodtotal'][i] = Label(f1, text=product_total, foreground='black', bg='#e1c1b2', font=("Times", "15", "bold"), pady=20, padx=10)
            labels['prodtime'][i] = Label(f1, text=self.hist[i][2], foreground='black', bg='#e1c1b2', font=("Times", "15", "bold"), pady=20, padx=10)

            # Place labels in the grid
            row = 2 * i
            labels['prodsno'][i].grid(row=row+2, column=0, padx=1, pady=1)
            labels['prodimg'][i].grid(row=row+2, column=1, padx=1, pady=1)
            labels['prodname'][i].grid(row=row+2, column=2, padx=1, pady=1)
            labels['prodprice'][i].grid(row=row+2, column=3, padx=1, pady=1)
            labels['prodquant'][i].grid(row=row+2, column=4, padx=1, pady=1)
            labels['prodtotal'][i].grid(row=row+2, column=5, padx=1, pady=1)
            labels['prodtime'][i].grid(row=row+2, column=6, padx=1, pady=1)

            # Add interception line
            Label(f1, text='-' * 160, foreground='black', bg='#e1c1b2', font=("Times", "15", "bold")).grid(column=0, row=row+1, columnspan=8)

        # Calculate total amount with tax
        tax = total_amount * 0.05
        total_with_tax = total_amount + tax

        # Display the total amount and tax
        total_label = Label(f1, text=f"Payable Amount: {total_amount} + Tax (5%): {tax:.2f} = {total_with_tax:.2f}", foreground='black', bg='#e1c1b2', font=("Times", "15", "bold"), pady=20, padx=10)
        total_label.grid(row=3*len(self.hist), column=0, columnspan=6)

        Btn = Button(f1, text='back', font=("Times", "12", "bold"), width=10, fg='white', bg='#bc6c25', activebackground='#e1c1b2', activeforeground='white', padx=10, pady=10, command=lambda: [self.root.destroy(), self.__init__(self.hist,self.username,self.prod)]).grid(column=2, row=4*len(self.hist))

        lab2 = Label(f1, foreground='black', bg='#e1c1b2',  font=("helvetica", "15", "bold"), pady=2)
        lab2.grid(column=2, row=4*len(self.hist)+1)
        lab2 = Label(f1, foreground='black', bg='#e1c1b2',  font=("helvetica", "15", "bold"), pady=2)
        lab2.grid(column=2, row=4*len(self.hist)+2)
        

        self.root.mainloop()

root = Tk()
root.title("SHAWSHANK OFFICIAL")
root.geometry("600x400")
root.configure(background="#e1c1b2")
p = Product()
s = Start(root,p)
s.pack(fill=BOTH, expand=YES)
s.DisplayWelcomeMessage(root)
root.mainloop()

