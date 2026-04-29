from tkinter import *
import os

score = 0
ques_no = 0
user_answers = []


questions = [
    {"question":"Capital of Pakistan?", "options":["Lahore","Karachi","Islamabad","Multan"], "answer":"3"},
    {"question":"5 + 7 = ?", "options":["10","11","12","13"], "answer":"3"},
    {"question":"Python is?", "options":["Snake","Programming language","Game","Browser"], "answer":"2"},
    {"question":"Which symbol is used for comments in Python?", "options":["//","#","/*","--"], "answer":"2"},
    {"question":"10 × 5 = ?", "options":["40","45","50","55"], "answer":"3"},
    {"question":"Which is input function in Python?", "options":["print()","input()","int()","str()"], "answer":"2"},
    {"question":"Which is output function?", "options":["print()","input()","len()","type()"], "answer":"1"},
    {"question":"Which data type is number?", "options":["int","str","list","dict"], "answer":"1"},
    {"question":"2² = ?", "options":["2","4","6","8"], "answer":"2"},
    {"question":"Which is used for loop?", "options":["if","for","int","def"], "answer":"2"},
    {"question":"Which is used to store multiple values?", "options":["int","str","list","float"], "answer":"3"},
    {"question":"Which keyword is used for function?", "options":["func","define","def","function"], "answer":"3"},
    {"question":"Which symbol is used for assignment?", "options":["==","=","!=" ,">="], "answer":"2"},
    {"question":"Which is correct extension of Python file?", "options":[".py",".java",".txt",".cpp"], "answer":"1"},
    {"question":"len() function is used for?", "options":["print","input","length","delete"], "answer":"3"},
    {"question":"Which loop runs forever?", "options":["for","while True","if","def"], "answer":"2"},
    {"question":"Which operator is addition?", "options":["+","-","*","/"], "answer":"1"},
    {"question":"Which is string?", "options":["123","Hello","5.6","True"], "answer":"2"},
    {"question":"Which is boolean value?", "options":["True","1","Hello","5.6"], "answer":"1"},
    {"question":"Which is used to exit loop?", "options":["stop","break","exit","end"], "answer":"2"}
]


def show():
    q = questions[ques_no]
    ques.config(text = q["question"])

    for i in range(4):
        button[i].config(text = q["options"][i])

def restart_quiz():
    global ques_no,score,user_answers

    ques_no = 0
    score = 0
    user_answers = []

    for widget in root.winfo_children():
        widget.destroy()

    root.destroy()
    os.system("Quiz_game.py")        


def show_result():
    ques.config(text=f"Your score: {score}")
    Button(root,text = "Restart",font = 'Georgia 12 bold',bg = "#0FB2ED",fg = "white",width = 15 ,height = 2,command = restart_quiz).pack(padx = 5)
    # buttons hide
    for b in button:
        b.pack_forget()

    # show answers
    for i, q in enumerate(questions):
        correct = q["options"][int(q["answer"]) - 1]
        user = q["options"][int(user_answers[i]) - 1]

        if user == correct:
            color = "#46F810"
            status = "✔"
        else:
            color = "#FF0404"
            status = "❌"


        Label(root, text=f"Q{i+1}: {correct} || You: {user} {status}",
            bg="#171F2C",
            fg = color, 
            font=("Arial", 10,'italic'),
            justify = 'left',
            anchor = "w" ).pack(fill = X,
                                padx = 10,
                                pady= 2)


def check(choice):
    global ques_no,score
    q = questions[ques_no]

    if choice == q["answer"]:
        score += 1
    
    ques_no += 1
    user_answers.append(choice)

    if ques_no < len(questions):
        show()
    else:
        show_result()


root = Tk()
root.geometry("650x650")
root.title("Quiz Game")
root.resizable(False,False)
root.configure(bg = "#171F2C")

ques = Label(root,text = "",bg = "#171F2C" ,font = "Georgia 19 bold",fg = "white")
ques.pack(padx = 10 ,pady = 10)

button = []
for i in range(4):
    btn = Button(root,text = "",
                 bg = "#171F2C",
                 fg = "white",
                 width = 20,
                 font = "Georgia 14 italic",
                 command = lambda i=i: check(str(i+1)))
    btn.pack(padx = 5,pady = 5)
    button.append(btn)

show()
root.mainloop()