import random

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

random.shuffle(questions)

score = 0

print("======================")
print("      QUIZ GAME       ")
print("======================\n")

for q in questions:
    print(f"\n{q["question"]}")

    for i,option in enumerate(q["options"], start = 1):
        print(f"{i}.{option}")

    ans = input("Enter the answer: ")
    if ans == q["answer"]:
        print("Correct✅")
        score += 1
    else:
        c_ans = q["options"][int(q['answer'])- 1]
        print(f"Wrong❌! \n Correct answer is {c_ans}")

print("=-="* 10 )
print(f'Your score is {score}/{len(questions)}')
print("=-="* 10 )