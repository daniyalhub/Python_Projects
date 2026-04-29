# Import Modulea
from tkinter import *
from tkinter import ttk
import string
import random
import os

# Function for showing specific layout for specific task
def Select_task(*arg):

    choice = drop_var.get() # To get drop list value

    lenght_entry.delete(0,END)  # To clear lenght
    password_entry.delete(0,END)# To clear lenght

    if choice == "Generate password":
        # To Hide widgets for "Generate password" selection
        password_label.pack_forget()
        status_bar_label.pack_forget()
        password_entry.pack_forget()
        status_bar.pack_forget()
        check_password_result.pack_forget()
        check_password_button.pack_forget()

        # To Hide widgets for "Generate password" selection
        generated_password_result.pack()
        lenght_label.pack()
        lenght_entry.pack()
        alpha_checkbox.pack()
        symbol_checkbox.pack()
        generate_password_button.pack()
    elif choice == "Check strenght":
        # To Hide widgets for "Check strenght" selection
        lenght_label.pack_forget()
        lenght_entry.pack_forget()
        alpha_checkbox.pack_forget()
        symbol_checkbox.pack_forget()
        generate_password_button.pack_forget()
        generated_password_result.pack_forget()

        # To Hide widgets for "Check strenght" selection
        check_password_result.pack()
        check_password_button.pack()
        password_label.pack()
        status_bar_label.pack()
        password_entry.pack()
        status_bar.pack(padx=5,pady=5)

    else:return 
    
# Function to Generate password    
def Generate_password():
    try:
        # To get value lenght as integar data type
        lenght = int(lenght_entry.get())
    except:
        # If user add other data type
        generated_password_var.set("Enter valid number")
        return   # stop function (NO crash)
    
    # Taking random number from String module

    characters = string.digits

    # If user check alphabets checkbox 

    if alpha_var.get():
        characters += string.ascii_letters

    # If user check symbol checkbox
    if symbol_var.get():
        characters += string.punctuation

    # For mixing letters,symbol,digits for password using "Random module"
    password = ""
    for _ in range(lenght):
        password += random.choice(characters)

    generated_password_var.set(password)

# Function for check strnght
def Check_strenght():
    # To get password in function
    pwd = password_entry.get()
    
    # Add score to store points of password strenght
    score = 0
    if len(pwd) >= 8:
        score += 1
    
    if any(c.isdigit() for c in pwd):
        score += 1
    
    if any(c.isalpha() for c in pwd):
        score += 1
    
    if any(c in string.punctuation for c in pwd):
        score += 1

    # Showing Strenght throught Status bar by colour

    if score == 1:
        status_bar.config(bg = "#F5675A",width = "60")
        strenght = "Weak password"
    elif score == 2:
        status_bar.config(bg = "#F5BF5A",width = "100")
        strenght = "Normal password"
    elif score == 3:
        status_bar.config(bg = "#F5E35A",width = "160")
        strenght = "Strong password"
    else:
        status_bar.config(bg = "#5AF55A",width = "200")
        strenght = "Very Strong password"

    check_password_var.set(strenght)

# Function for Copy Password
def Copy_password():
    root.clipboard_clear()
    root.clipboard_append(generated_password_var.get())


# Function for Save password
def Save_password():
    pwd = generated_password_var.get()

    if pwd == "":
        return
    # If Folder doesn't exist to save_passwordfile the create Folder
    if not os.path.exists("Record"):
        os.makedirs("Record")

    with open("Record/Password.txt","a") as f:
        f.write(f'{pwd} \n------------------\n')    

# Making Geomwtry
root = Tk()

root.title("Pass Master")

root.geometry('450x550')

root.resizable(False,False)

root.configure(bg = "#20292D")

# title
title = Label(root,text = "Pass Master",bg = "#20292D",fg = "#56F1E4",font = "Georgia 24 bold")
title.pack()

# Category
category_label = Label(root,text = "Category",bg = "#20292D",fg = "#F3F4F4",font = "Georgia 8 bold")
category_label.pack()

tasks = ["Generate password","Check strenght"]

drop_var = StringVar()
drop_list = ttk.Combobox(root,values = tasks,font = "Georgia 8 italic",textvariable = drop_var,state = "readonly")
drop_list.pack(padx = 10)

drop_list.bind("<<ComboboxSelected>>",Select_task)

# Lenght
lenght_label = Label(root, text = "lenght",bg = "#20292D",fg = "#F3F4F4",font = "Georgia 8 bold")
lenght_label.pack()

lenght_var = StringVar(value = 8)

lenght_entry = Entry(root,font = "Georgia 8 bold",textvariable = lenght_var,bg = "white" ,fg = "black", insertbackground = "#20292D")
lenght_entry.pack()

# Checkbox
alpha_var = BooleanVar()
alpha_checkbox = Checkbutton(root, text = "Contain alphabets",bg = "#20292D",fg = "white",variable = alpha_var)
alpha_checkbox.pack()

symbol_var = BooleanVar()
symbol_checkbox = Checkbutton(root, text = "Contain symbols",bg = "#20292D",fg = "white",variable = symbol_var)
symbol_checkbox.pack()
# Taking password for Checking strength
password_label = Label(root, text = "Enter password",bg = "#20292D",fg = "#F3F4F4",font = "Georgia 8 bold")
password_label.pack()

password_entry_var = StringVar()

password_entry = Entry(root,font = "Georgia 8 bold",textvariable = password_entry_var,bg = "white" ,fg = "black", insertbackground = "#20292D")
password_entry.pack()
password_entry.bind("<KeyRelease>", lambda e: Check_strenght())


# Status Bar for strenght
status_bar_label = Label(root, text = "Stenght Bar",bg = "#20292D",fg = "#F3F4F4",font = "Georgia 8 bold")
status_bar_label.pack()
status_bar = Frame(root,bg = "#62EA7F",width = 100 ,height = 20)
status_bar.pack(pady = 5,padx = 5)

# Generated Password Button and result
generate_password_button = Button(root,text= "Generate password",width = 15,height = 2,bg ="#20292D" ,fg="white",font = "Georgia 8 bold",command = Generate_password)
generate_password_button.pack(pady = 5)

generated_password_var = StringVar()
generated_password_result = Label(root,textvariable = generated_password_var, bg = "#20292D" ,fg="#56F1E4",font = "Georgia 16 bold")
generated_password_result.pack()

# Check Password Button and result
check_password_button = Button(root,text= "Check password",width = 15,height = 2,bg = "#20292D" ,fg="white",font = "Georgia 8 bold",command = Check_strenght)
check_password_button.pack(pady = 5)

check_password_var = StringVar()
check_password_result = Label(root,textvariable = check_password_var, bg = "#20292D" ,fg="#56F1E4",font = "Georgia 16 bold")
check_password_result.pack()

# Copy password button
copy_password = Button(root,text = "Copy", height = 1,width = 8,command = Copy_password,bg = "#20292D" ,fg="white",font = "Georgia 8 bold")
copy_password.pack()

# Save password button
save_password = Button(root,text = "Save", height = 1,width = 8,command = Save_password,bg = "#20292D" ,fg="white",font = "Georgia 8 bold")
save_password.pack(padx = 5,pady =5)
# Exit window Button
exit_window = Button(root,text = "exit", height = 1,width = 8,command = root.quit,bg = "red" ,fg="white",font = "Georgia 8 bold")
exit_window.pack(padx = 5,pady =5)

root.mainloop()