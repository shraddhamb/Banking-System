import tkinter as tk
from tkinter import messagebox
from time import gmtime, strftime


def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0

def check_acc_nmb(num):
    try:
        fpin=open(num+".txt",'r')
    except FileNotFoundError:
        messagebox.showinfo("Error","Enter The Valid Account Number:\nTry Again!")
        return 0
    fpin.close()
    return

def check_acc_name(acc_name):
    try:
        check=open(acc_name+".txt",'r')
    except FileNotFoundError:
        messagebox.showinfo("Error","Enter The Valid User Name:\nTry Again!")
        return 0
    check.close()
    return 

def home_return(master):
    master.destroy()
    Main_Menu()

def write(master,name,oc,pin,user_name):
    
    if( (is_number(name)) or (is_number(oc)==0) or (is_number(pin)==0)or name=="" or user_name==""):
        messagebox.showinfo("Error","Enter Valid Information\nPlease try again.")
        master.destroy()
        return

    x = name.isalpha()
    if(x == True):
        messagebox.showinfo("Error","Enter The Valid Full Name:\nPlease try again.")
        master.destroy()
        return

       
    try:
        check=open(str(user_name)+".txt","r")
    except:
        f1=open("Accnt_Record.txt",'r')
        accnt_no=int(f1.readline())
        accnt_no+=1
        f1.close()

        f1=open("Accnt_Record.txt",'w')
        f1.write(str(accnt_no))
        f1.close()

        fdet=open(str(accnt_no)+".txt","w")

        fdet.write(pin+"\n")
        fdet.write(oc+"\n")
        fdet.write(str(accnt_no)+"\n")
        fdet.write(name+"\n")
        fdet.close()
    
        check=open(str(user_name)+".txt","w")
        check.write(pin+"\n");
        check.write(user_name)
        check.close()

        frec=open(str(accnt_no)+"-rec.txt",'w')
        frec.write("Date                             Credit      Debit     Balance\n")
        frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+oc+"              "+oc+"\n")
        frec.close()
    
        messagebox.showinfo("Details","Your Account Number is:"+str(accnt_no))
        master.destroy()
        return
    else:
        messagebox.showinfo("Warning","User Name Already Taken:\nYou can Also Use A Special Character or Number:")
        master.destroy()
        return
        

def crdt_write(master,amt,accnt,name):

    if(is_number(amt)==0 or amt == "0"):
        messagebox.showwarning("Error","Enter Valid Amount\nPlease try again.")
        master.destroy()
        return 

    fdet=open(accnt+".txt",'r')
    pin=fdet.readline()
    camt=int(fdet.readline())
    acc_no=int(fdet.readline())
    acc_name=fdet.readline()
    fdet.close()
    amti=int(amt)
    cb=amti+camt
    fdet=open(accnt+".txt",'w')
    fdet.write(pin)
    fdet.write(str(cb)+"\n")
    fdet.write(accnt+"\n")
    fdet.write(acc_name+"\n")
    fdet.close()
    frec=open(str(accnt)+"-rec.txt",'a+')
    frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+str(amti)+"              "+str(cb)+"\n")
    frec.close()
    messagebox.showinfo("Operation Successfull!!","Amount Credited Successfully!!")
    master.destroy()
    return

def debit_write(master,amt,accnt,name):

    if(is_number(amt)==0 or amt == "0"):
        messagebox.showwarning("Error","Enter Valid Ammount:\nPlease try again.")
        master.destroy()
        return 
            
    fdet=open(accnt+".txt",'r')
    pin=fdet.readline()
    camt=int(fdet.readline())
    acc_no=int(fdet.readline())
    acc_name=fdet.readline()
    fdet.close()
    if(int(amt)>camt):
        messagebox.showerror("Error!!","You dont have that amount left in your account\nPlease try again.")
    else:
        amti=int(amt)
        cb=camt-amti
        fdet=open(accnt+".txt",'w')
        fdet.write(pin)
        fdet.write(str(cb)+"\n")
        fdet.write(accnt+"\n")
        fdet.write(acc_name+"\n")
        fdet.close()
        frec=open(str(accnt)+"-rec.txt",'a+')
        frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+"              "+str(amti)+"              "+str(cb)+"\n")
        frec.close()
        messagebox.showinfo("Operation Successfull!!","Amount Debited Successfully!!")
        master.destroy()
        return

def Cr_Amt(accnt,name):
    creditwn=tk.Tk()
    creditwn.geometry("900x600")
    creditwn.title("Credit Amount")
    creditwn.configure(bg="orange")
    fr1=tk.Frame(creditwn,bg="blue")
    l_title=tk.Message(creditwn,text="UNITED BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    l1=tk.Label(creditwn,relief="raised",text="Enter Amount to be Credited: ",width="24",height="2",font=("comic sans Ms",12,"bold"))
    e1=tk.Entry(creditwn,relief="raised",width="25",font=("comic sans Ms",12,"bold"))
    l1.place(x=250,y=100)
    e1.place(x=500,y=109)
    b=tk.Button(creditwn,text="Credit",relief="raised",font=("comic sans Ms",12,"bold"),width="13",height="2",command=lambda:crdt_write(creditwn,e1.get(),accnt,name))
    b.place(x=400,y=170)
    creditwn.bind("<Return>",lambda x:crdt_write(creditwn,e1.get(),accnt,name))


def De_Amt(accnt,name):
    debitwn=tk.Tk()
    debitwn.geometry("900x600")
    debitwn.title("Debit Amount")   
    debitwn.configure(bg="orange")
    fr1=tk.Frame(debitwn,bg="blue")
    l_title=tk.Message(debitwn,text="UNITED BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    l1=tk.Label(debitwn,relief="raised",text="Enter Amount to be Debited: ",width="23",height="2",font=("comic sans Ms",12,"bold"))
    e1=tk.Entry(debitwn,relief="raised",width="25",font=("comic sans Ms",12,"bold"))
    l1.place(x=250,y=100)
    e1.place(x=500,y=109)
    b=tk.Button(debitwn,text="Debit",relief="raised",font=("comic sans Ms",12,"bold"),width="13",height="2",command=lambda:debit_write(debitwn,e1.get(),accnt,name))
    b.place(x=400,y=170)
    debitwn.bind("<Return>",lambda x:debit_write(debitwn,e1.get(),accnt,name))




def disp_bal(accnt):
    fdet=open(accnt+".txt",'r')
    fdet.readline()
    bal=fdet.readline()
    fdet.close()
    messagebox.showinfo("Balance",bal)




def disp_tr_hist(accnt):
    disp_wn=tk.Tk()
    disp_wn.geometry("900x600")
    disp_wn.title("Transaction History")
    disp_wn.configure(bg="orange")
    fr1=tk.Frame(disp_wn,bg="blue")
    l_title=tk.Message(disp_wn,text="UNITED BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    fr1=tk.Frame(disp_wn)
    fr1.pack(side="top")
    l1=tk.Message(disp_wn,text="Your Transaction History:",padx=100,pady=20,width=1000,bg="blue",font=("comic sans Ms",15,"bold"),fg="white",relief="raised")
    l1.pack(side="top")
    fr2=tk.Frame(disp_wn)
    fr2.place(x=250,y=100)
    i=0
    frec=open(accnt+"-rec.txt",'r')
    for line in frec:
        l=tk.Message(disp_wn,anchor="w",text=line,relief="raised",width=2000)
        l.place(x=300,y=150+i)
        i = i + 45
    b=tk.Button(disp_wn,text="Quit",relief="raised",width="10",command=disp_wn.destroy)
    b.place(x=400,y=150+i)
    frec.close()

def logged_in_menu(accnt,name):
    rootwn=tk.Tk()
    rootwn.geometry("1600x500")
    rootwn.title("UNITED BANK-"+name)
    rootwn.configure(background='orange')
    fr1=tk.Frame(rootwn)
    fr1.pack(side="top")
    l_title=tk.Message(rootwn,text="SIMPLE BANKING\n SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    label=tk.Label(text="Logged in as: "+name,relief="raised",bg="black",fg="white",anchor="center",justify="center")
    label.pack(side="top")
    img2=tk.PhotoImage(file="credit.gif")
    myimg2=img2.subsample(2,2)
    img3=tk.PhotoImage(file="debit.gif")
    myimg3=img3.subsample(2,2)
    img4=tk.PhotoImage(file="balance1.gif")
    myimg4=img4.subsample(2,2)
    img5=tk.PhotoImage(file="transaction.gif")
    myimg5=img5.subsample(2,2)
    b2=tk.Button(image=myimg2,command=lambda: Cr_Amt(accnt,name))
    b2.image=myimg2
    b3=tk.Button(image=myimg3,command=lambda: De_Amt(accnt,name))
    b3.image=myimg3
    b4=tk.Button(image=myimg4,command=lambda: disp_bal(accnt))
    b4.image=myimg4
    b5=tk.Button(image=myimg5,command=lambda: disp_tr_hist(accnt))
    b5.image=myimg5
    
    img6=tk.PhotoImage(file="logout.gif")
    myimg6=img6.subsample(2,2)
    b6=tk.Button(image=myimg6,relief="raised",command=lambda: logout(rootwn))
    b6.image=myimg6

    
    b2.place(x=100,y=150)
    b3.place(x=100,y=220)
    b4.place(x=900,y=150)
    b5.place(x=900,y=220)
    b6.place(x=500,y=400)

    
def logout(master):
    
    messagebox.showinfo("Logged Out","You Have Been Successfully Logged Out!!")
    master.destroy()
    Main_Menu()

def check_log_in(master,user_name,acc_num,pin):

    if(check_acc_name(user_name)==0):
        master.destroy()
        Main_Menu()
        return

    if(check_acc_nmb(acc_num)==0):
        master.destroy()
        Main_Menu()
        return
    
    check=open(str(user_name)+".txt",'r')
    x=int(check.readline())
    y=check.readline()
    if(y != str(user_name)):
        messagebox.showinfo("Error","Enter The Valid User Name\nPlease try again.")
        master.destroy()
        Main_Menu()
        
    if(x != int(pin)):
        messagebox.showinfo("Error","Enter The Valid Pin\nPlease try again.")
        master.destroy()
        Main_Menu()

    if( (is_number(user_name))  or (is_number(pin)==0) ):
        messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
        master.destroy()
        Main_Menu()
    else:
        master.destroy()
        logged_in_menu(acc_num,user_name)


def log_in(master):
    master.destroy()
    loginwn=tk.Tk()
    loginwn.geometry("1500x850")
    loginwn.title("Log in")
    loginwn.configure(bg="orange")
    fr1=tk.Frame(loginwn,bg="blue")
    l_title=tk.Message(loginwn,text="UNITED BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    l1=tk.Label(loginwn,text="Enter User Name:",relief="raised",width="18",height="2",font=("comic sans Ms",12,"bold"))
    l1.place(x=470,y=120)
    e1=tk.Entry(loginwn,width="30",font=("comic sans Ms",12,"bold"))
    e1.place(x=720,y=125)
    l2=tk.Label(loginwn,text="Enter Account Number:",relief="raised",width="22",height="2",font=("comic sans Ms",12,"bold"))
    l2.place(x=470,y=200)
    e2=tk.Entry(loginwn,width="30",font=("comic sans Ms",12,"bold"))
    e2.place(x=720,y=208)
    l3=tk.Label(loginwn,text="Enter Your PIN:",relief="raised",width="18",height="2",font=("comic sans Ms",12,"bold"))
    l3.place(x=470,y=280)
    e3=tk.Entry(loginwn,show="*",width="30",font=("comic sans Ms",12,"bold"))
    e3.place(x=720,y=285)
    b=tk.Button(loginwn,text="SUBMIT",relief="raised",width="15",height="2",font=("comic sans Ms",12,"bold"),command=lambda: check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
    b.place(x=620,y=360)
    b1=tk.Button(text="HOME",relief="raised",font=("comic sans Ms",12,"bold"),width="15",height="2",bg="black",fg="white",command=lambda: home_return(loginwn))
    b1.place(x=620,y=440)
    loginwn.bind("<Return>",lambda x:check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
    

def Create():
    
    crwn=tk.Tk()
    crwn.geometry("1500x850")
    crwn.title("Create Account")
    crwn.configure(bg="orange")
    fr1=tk.Frame(crwn,bg="blue")
    l_title=tk.Message(crwn,text="UNITED BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    l1=tk.Label(crwn,text="Enter Full Name:",relief="raised",width="18",height="2",font=("comic sans Ms",12,"bold"))
    l1.place(x=470,y=120)
    e1=tk.Entry(crwn,width="30",font=("comic sans Ms",12,"bold"))
    e1.place(x=720,y=125)
    l2=tk.Label(crwn,text="Enter Opening Credit:",relief="raised",width="22",height="2",font=("comic sans Ms",12,"bold"))
    l2.place(x=470,y=200)
    e2=tk.Entry(crwn,width="30",font=("comic sans Ms",12,"bold"))
    e2.place(x=720,y=205)
    l4=tk.Label(crwn,text="Enter User Name:",relief="raised",width="18",height="2",font=("comic sans Ms",12,"bold"))
    l4.place(x=470,y=280)
    e4=tk.Entry(crwn,width="30",font=("comic sans Ms",12,"bold"))
    e4.place(x=720,y=285)
    l3=tk.Label(crwn,text="Enter Desired PIN:",relief="raised",width="18",height="2",font=("comic sans Ms",12,"bold"))
    l3.place(x=470,y=360)
    e3=tk.Entry(crwn,show="*",width="30",font=("comic sans Ms",12,"bold"))
    e3.place(x=720,y=365)
    b=tk.Button(crwn,text="Submit",font=("comic sans Ms",12,"bold"),width="15",height="2",command=lambda: write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip(),e4.get().strip()))
    b.place(x=620,y=420)
    crwn.bind("<Return>",lambda x:write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip(),e4.get().strip()))
    return


def Main_Menu():
    

    rootwn=tk.Tk()
    rootwn.geometry("1500x850")
    rootwn.title("UNITED Bank")
    #rootwn.configure(background='orange')
    fr1=tk.Frame(rootwn)
    fr1.pack(side="top")
    bg_image = tk.PhotoImage(file ="pile1.gif")
    x = tk.Label (image = bg_image)
    x.place(y=-400)
    l_title=tk.Message(text="SIMPLE BANKING\n SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    imgc1=tk.PhotoImage(file="new.gif")
    imglo=tk.PhotoImage(file="login.gif")
    imgc=imgc1.subsample(2,2)
    imglog=imglo.subsample(2,2)

    b1=tk.Button(image=imgc,command=Create)
    b1.image=imgc
    b2=tk.Button(image=imglog,command=lambda: log_in(rootwn))
    b2.image=imglog
    img6=tk.PhotoImage(file="quit.gif")
    myimg6=img6.subsample(2,2)

    b6=tk.Button(image=myimg6,command=rootwn.destroy)
    b6.image=myimg6
    b1.place(x=800,y=300)
    b2.place(x=800,y=200)   
    b6.place(x=920,y=400)

    rootwn.mainloop()

Main_Menu()
