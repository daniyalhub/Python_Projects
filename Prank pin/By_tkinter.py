# For a prank

from tkinter import *
from tkinter import messagebox 

pin = "qwer"
attempt = 3

def Check():
    global attempt
    user = pin_var.get()

    if pin == user:
        result_var.set("Corrct \nYou are save")
    else:
        attempt -= 1
        messagebox.showwarning("Warning", f"You have {attempt} {'attempts' if attempt > 1 else 'attempt'} left")
        pin_var.set("")
        if attempt == 0:
            result_var.set("your device is locked for 24 hours")

root = Tk()

root.geometry("400x250")
root.resizable(False,False)
root.configure(bg = "#2D3A50")

Label(root,text = "Enter pin",bg = "#2D3A50", font = "georgia 19 bold",fg = "black").pack(padx = 14,pady=14)
pin_var = StringVar()
pin_entry = Entry(root,bg ="#D0D5DE", font = "georgia 10 bold",fg = "black",textvariable=pin_var )
pin_entry.pack()

check_button = Button(root,text = "Check",command= Check,bg ="#D0D5DE", font = "georgia 10 bold",fg = "black")
check_button.pack(padx = 10,pady = 10)

result_var = StringVar()
result = Label(root,textvariable = result_var,bg = "#2D3A50", font = "georgia 19 bold",fg = "black").pack(padx = 14,pady=14)

root.mainloop()