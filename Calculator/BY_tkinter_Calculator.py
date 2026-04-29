from tkinter import *

def Click(task):

    text = task.widget["text"]

    if text == "C":
        entry_widget.delete(0,END)
        
    elif text == "=":
        try:
            result = eval(entry_widget.get())
            entry_widget.delete(0,END)
            entry_widget.insert(END,result)

        except:
            entry_widget.delete(0,END)
            entry_widget.insert(END,"Error!")
    elif text == "⌫":
        current = entry_widget.get()
        entry_widget.delete(0,END)
        entry_widget.insert(END,current [:-1])

    else:
            entry_widget.insert(END,text)



root = Tk()
root.title("Calculator")
root.geometry("410x500")
root.resizable(False,False)
root.configure(bg = "#435F6E")

entry_widget = Entry(root, font = "Georgia 30",width = 25 ,bg = "#49F4F1",bd = 5,justify = "right")
entry_widget.pack(pady = 5,padx = 12)

btn_frame = Frame(root,bg = "#435F6E")
btn_frame.pack(padx = 10 ,pady = 10)

buttons = [['C',"⌫","%","/"],
           ["7","8","9","*"],
           ["4","5","6","-"],
           ["1","2","3","+"],
           ["0","00",".","="]]


for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        btn = Button(btn_frame, text = buttons[i][j],font = "Georgia 12  bold",width = 7,height= 3,bg = "#57798B")
        btn.grid(row = i,column = j,padx = 5,pady = 5)
        btn.bind("<Button-1>",Click)
root.mainloop()