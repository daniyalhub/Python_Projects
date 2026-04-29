from tkinter import *
from tkinter import ttk,messagebox
def Conversion():
    value = float(ery_var.get())
    conver = con_var.get()
    try:
        if conver == "Meter to Kilometer":
            result = value / 1000
            unit = "Km"
        elif conver == "Kilometer to Meter":
            result = value * 1000
            unit = "m"
        elif conver == "Gram to Kilogram":
            result = value / 1000
            unit = "Kg"
        elif conver == "Kilogram to Gram":
            result = value * 1000
            unit = "g"
        elif conver == "Celsius to Kelvin":
            result = value + 273.15
            unit = "K"
        elif conver == "Celsius to Fahrenheit":
            result = (value * (9 / 5)) + 32
            unit = "F"
        elif conver == "Fahrenheit to Kelvin":
            result = (value - 32)* 5/9 + 273.15
            unit = "K"
        elif conver == "Fahrenheit to Celsius":
            result = (value - 32) * 5/9
            unit = "C"
        elif conver == "Kelvin to Celsius":
            result = value - 273.15
            unit = "C"
        elif conver == "Kelvin to Fahrenheit":
            result = (value - 273.15) * 9/5 +32
            unit = "F"

        else:
            return
        
        result_var.set(f"Result: {result:.2f}{unit}")

    except:
        messagebox.showerror('Error',"Invalid input")




root = Tk()
root.title("Unit Convertor")

root.geometry("500x300")
root.resizable(False,False)
root.configure(bg = "#1D364D")

Label(root, text = "Unit Convertor",bg = "#1D364D",fg = "White",font = "Georgia 20 bold").pack(padx = 5 ,pady = 5)
con_var = StringVar()
conversion = ["Meter to Kilometer",
            "Kilometer to Meter",
            "Gram to Kilogram",
            "Kilogram to Gram",
            "Celsius to Kelvin",
            "Celsius to Fahrenheit",
            "Fahrenheit to Kelvin",
            "Fahrenheit to Celsius",
            "Kelvin to Celsius",
            "Kelvin to Fahrenheit"]


li_st = ttk.Combobox(root,value = conversion,textvariable = con_var,font = "Georgia 10",state = "readonly")
li_st.pack()

Label(root, text = "Enter value",bg = "#1D364D",fg = "White",font = "Georgia 10 bold").pack(padx = 5 ,pady = 5)

ery_var = StringVar()
entry = Entry(root,bg = "#274663",fg = "white",font = "Georgia 12",textvariable = ery_var)
entry.pack(padx = 5,pady = 5)

result_var = StringVar()
Label(root,textvariable = result_var,bg = "#1D364D",fg = "White",font = "Georgia 10 bold").pack(padx = 5 ,pady = 5)

Button(root, text = "Convert",bg = "#FC3503",fg = "White",font = "Georgia 10 bold",command = Conversion).pack(padx = 5 ,pady = 5)
root.mainloop()