# Import Modules
from tkinter import *
from tkinter import ttk,messagebox
import math

# functions
def update(*args):
    shape = shapes_var.get()# Taking value from user

    # clear inputs
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    entry_3.delete(0, END)

    # show all first
    entry_2.pack()
    entry_3.pack()

    # Circle
    if shape == "Circle":
        label_1.config(text="Enter Radius")
        label_2.config(text="")
        label_3.config(text="")
        entry_2.pack_forget()
        entry_3.pack_forget()

    # Square
    elif shape == "Square":
        label_1.config(text="Enter Side")
        label_2.config(text="")
        label_3.config(text="")
        entry_2.pack_forget()
        entry_3.pack_forget()

    # Triangle
    elif shape == "Triangle":
        label_1.config(text="Enter Base")
        label_2.config(text="Enter Height")
        label_3.config(text="")
        entry_3.pack_forget()

    # Rectangle
    elif shape == "Rectangle":
        label_1.config(text="Enter Length")
        label_2.config(text="Enter Width")
        label_3.config(text="")
        entry_3.pack_forget()

    # Parallelogram
    elif shape == "Parallelogram":
        label_1.config(text="Enter Base")
        label_2.config(text="Enter Height")
        label_3.config(text="")
        entry_3.pack_forget()

    # Trapezium
    elif shape == "Trapezium":
        label_1.config(text="Enter Base 1")
        label_2.config(text="Enter Base 2")
        label_3.config(text="Enter Height")

    # Rhombus
    elif shape == "Rhombus":
        label_1.config(text="Enter Diagonal 1")
        label_2.config(text="Enter Diagonal 2")
        label_3.config(text="")
        entry_3.pack_forget()

    # Ellipse
    elif shape == "Ellipse":
        label_1.config(text="Enter Axis a")
        label_2.config(text="Enter Axis b")
        label_3.config(text="")
        entry_3.pack_forget()


def Calculation():

    shape = shapes_var.get() # Taking value from user

    try:

        if entry_1.get():
            a = float(entry_1.get())
        else:
            a = 0

        if entry_2.get():
            b = float(entry_2.get())
        else:
            b = 0

        if entry_3.get():
            c = float(entry_3.get())
        else:
            c = 0

        if shape == "Circle":
            if a <= 0: raise ValueError
            area = math.pi * a**2

        elif shape == "Square":
            if a <= 0: raise ValueError
            area = a**2

        elif shape == "Triangle":
            if a <= 0 or b <= 0 : raise ValueError
            area = 0.5 * a * b

        elif shape == "Rectangle":
            if a <= 0 or b <= 0 : raise ValueError
            area = a * b
        
        elif shape == "Parallelogram":
            if a <= 0 or b <= 0 : raise ValueError
            area = a * b

        elif shape == "Trapezium":
            if a <= 0 or b <= 0 or c <= 0: raise ValueError
            area = 0.5 * (a + b) * c
        
        elif shape == "Rhombus":
            if a <= 0 or b <= 0 : raise ValueError
            area = 0.5 * a * b
        
        elif shape == "Ellipse":
            if a <= 0 or b <= 0 : raise ValueError
            area = math.pi * a * b 
        
        else:return

        result_var.set(f"Result: {area:.2f}")

    except:
        messagebox.showerror('Error',"Invalid input")

# ------ Main Geometry ------
root = Tk()
root.geometry("500x500")
root.title("Area Finder")
root.configure(bg = "#242A38")

# Style

style = ttk.Style()
style.theme_use("alt")
style.configure("TCombobox",
                fieldbackground="Grey",
                background="Grey",
                foreground="white")

# Title

Label(root,text = "Area Finder",
      font = "Arial 19 bold",
      fg = "Cyan",
      bg = "#242A38").pack(pady = 10)

# list

shapes = ["Circle", "Square", "Triangle", "Rectangle",
          "Parallelogram", "Trapezium", "Rhombus", "Ellipse"]

shapes_var = StringVar()

drop_list = ttk.Combobox(root , value = shapes , textvariable = shapes_var, state = 'readonly')
drop_list.pack(padx = 10)
drop_list.bind("<<ComboboxSelected>>",update)

# ------ Labels & Entry ------

label_1 = Label(root, text = "",
               bg = "#242A38",
               fg = "white")
label_1.pack()

entry_1 = Entry(root, bg = "#54555A",fg = "#FFFFFF",insertbackground = "#F4F6FC")
entry_1.pack(padx = 5)


label_2 = Label(root, text = "",
               bg = "#242A38",
               fg = "white")
label_2.pack()

entry_2 = Entry(root, bg = "#54555A",fg = "#FFFFFF",insertbackground = "#E2EAFE")
entry_2.pack(padx = 5)

label_3 = Label(root, text = "",
               bg = "#242A38",
               fg = "white")
label_3.pack()

entry_3 = Entry(root, bg = "#54555A",fg = "#FFFFFF",insertbackground = "#F6F9FF")
entry_3.pack(padx = 5)

# Result
result_var = StringVar()
result = Label(root, textvariable = result_var,
               bg = "#242A38",
               fg = "#00ffcc",
               font = "Georgia 19 bold")
result.pack(padx = 15,pady = 10)

# Buttons
calculate_button = Button(root , text = "Calculate",width = 15,height = 2,fg = "white",bg = "#00aa88",command = Calculation,font = "Georgia 8 bold")
calculate_button.pack(padx = 15)

save_button = Button(root , text = "Exit",width = 15,height = 2,fg = "white",bg = "red",command = root.quit,font = "Georgia 8 bold")
save_button.pack(padx = 10,pady = 10)



root.mainloop()