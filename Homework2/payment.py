import time
import tkinter.messagebox
from tkinter import *
 
root = Tk()
root.title("Employee Payment System")
root.geometry('1370x720+0+0')
root.maxsize(width=1370, height=720)
root.minsize(width=1370, height=720)
root.configure(background="dark gray")
 
Tops = Frame(root, width=1350, height=50, bd=8, bg="dark gray")
Tops.pack(side=TOP)
 
f1 = Frame(root, width=600, height=600, bd=8, bg="dark gray")
f1.pack(side=LEFT)
f2 = Frame(root, width=300, height=700, bd=8, bg="dark gray")
f2.pack(side=RIGHT)
 
fla = Frame(f1, width=600, height=200, bd=8, bg="dark gray")
fla.pack(side=TOP)
flb = Frame(f1, width=300, height=600, bd=8, bg="dark gray")
flb.pack(side=TOP)
 
lbl_information = Label(Tops, font=('arial', 45, 'bold'), text="Employee Payment Management Slip ", relief=GROOVE, bd=10, bg="Dark Gray", fg="Black")
lbl_information.grid(row=0, column=0)
 
#Exit function 
def Exit():
    wayOut = tkinter.messagebox.askyesno("Employee Payment System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return
 
 #resetfunction
def Reset():
    FullName.set("")
    Address.set("")
    Payable.set("")
 
    NetPayable.set("")
    GrossPayable.set("")
    AnnualSalary.set("")
  
    CompanyAgency.set("")
    PhoneNumber.set("")
    txtPaymentSlip.delete("1.0", END)
 
 
def InformationEntry():
    txtPaymentSlip.delete("1.0", END)
    txtPaymentSlip.insert(END, "\t\tPay Slip\n\n")
    txtPaymentSlip.insert(END, "Full Name :\t\t" + FullName.get() + "\n\n")
    txtPaymentSlip.insert(END, "Home Address :\t\t" + Address.get() + "\n\n")
    txtPaymentSlip.insert(END, "Company/Agency :\t\t" + CompanyAgency.get() + "\n\n")
    txtPaymentSlip.insert(END, "Phone Number :\t\t" + PhoneNumber.get() + "\n\n")
    txtPaymentSlip.insert(END, "AnnualSalary:\t\t" + AnnualSalary.get() + "\n\n")
    txtPaymentSlip.insert(END, "Net Payable :\t\t" + NetPayable.get() + "\n\n")
    txtPaymentSlip.insert(END, "Payable :\t\t" + Payable.get() + "\n\n")
 
me = 1250
ve = 1250

def WagesForWeekly():
    
    result= (float(AnnualSalary.get())//12)

    hra = result/2

    if(result >= 25000) :
        grossal = result + me + ve + hra
        
        
    else :
        grossal = "sallary not good"

    Payable.set(grossal)

    nsal = grossal-(me + hra + ve)
    NetPayable.set(nsal)
    

global Payable
global NetPayable


# Variables

taxText = StringVar()
nsalText = StringVar()
FullName = StringVar()
Address = StringVar()
NetPayable = StringVar()

CompanyAgency = StringVar()
PhoneNumber = StringVar()
Payable = StringVar()
GrossPayable = StringVar()
AnnualSalary = StringVar()
Payable = StringVar()
 
# Label Widget
 
labelFirstName = Label(fla, text="Full Name", font=('arial', 16, 'bold'), bd=20, fg="white", bg="dark gray").grid(row=0, column=0)
 
labelAddress = Label(fla, text="Home Address", font=('arial', 16, 'bold'), bd=20, fg="white", bg="dark gray").grid(row=0, column=2)
 
labelCompanyAgency = Label(fla, text="Company/Agency", font=('arial', 16, 'bold'), bd=20, fg="white", bg="dark gray").grid(row=1,
    column=0)

labelPhoneNumber = Label(fla, text="Phone Number", font=('arial', 16, 'bold'), bd=20, fg="white", bg="dark gray").grid(row=1,
    column=2)

labelAnnualSalary = Label(fla, text="AnnualSalary", font=('arial', 16, 'bold'), bd=20, fg="white", bg="dark gray").grid(
    row=2, column=0)

labelGrossPay = Label(fla, text="GrossPay", font=('arial', 16, 'bold'), bd=20, fg="white", bg="dark gray").grid(row=4,
    column=0)
labelNetPay = Label(fla, text="Net Pay", font=('arial', 16, 'bold'), bd=20, fg="white", bg="dark gray").grid(row=4,
    column=2)
 
# Entry Widget
 
txtFullname = Entry(fla, textvariable=FullName, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
txtFullname.grid(row=0, column=1)
 
txtAddress = Entry(fla, textvariable=Address, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
txtAddress.grid(row=0, column=3)
 
txtCompanyAgency = Entry(fla, textvariable=CompanyAgency, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
txtCompanyAgency.grid(row=1, column=1)

txtAnnualSalary = Entry(fla, textvariable=AnnualSalary, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
txtAnnualSalary.grid(row=2, column=1)

txtGrossPayment = Entry(fla, textvariable=Payable, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
txtGrossPayment.grid(row=4, column=1) 

txtNetPayable = Entry(fla, textvariable=NetPayable, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
txtNetPayable.grid(row=4, column=3)
    
txtPhoneNumber = Entry(fla, textvariable=PhoneNumber, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
txtPhoneNumber.grid(row=1, column=3)
 
 
# Text Widget
 
txtPaymentSlip = Text(f2, height=22, width=34, bd=16, font=('arial', 13, 'bold'), fg="black", bg="white")
txtPaymentSlip.grid(row=1, column=0)
 
# buttons
ButtonSalary = Button(flb, text='Monthly Salary', padx=16, pady=16, bd=15, font=('arial', 16, 'bold'), relief="groove", width=14, fg="black",
  command=WagesForWeekly,  bg="dark gray").grid(row=0, column=0)
 
ButtonReset = Button(flb, text='Reset', padx=16, pady=16, bd=15, font=('arial', 16, 'bold'), relief="groove", width=14, command=Reset,
    fg="black", bg="dark gray").grid(row=0, column=1)
 
ButtonPaySlip = Button(flb, text='View Payslip', padx=16, pady=16, bd=15, font=('arial', 16, 'bold'), relief="groove", width=14,
    command=InformationEntry, fg="black", bg="dark gray").grid(row=0, column=2)
 
ButtonExit = Button(flb, text='Exit System', padx=16, pady=16, bd=15, font=('arial', 16, 'bold'), relief="groove", width=14, command=Exit,
fg="black", bg="dark gray").grid(row=0, column=3)
 
 
root.mainloop()