print("="*36)
print("*"*36)
print("             Calculator")
print("*"*36)
print("="*36)

print("Its is a simple calculator")
print("Type Exit to exit calculator")
print("Otherwise start your operation")


while True:
    
    in_put = input("Enter the first number")
    
    if in_put.lower() == "exit":
        break
    
    try:
        num1 = float(in_put)
    except:
        print("\n Invalid Input")
    op = input("Enter the operation \n\t1.\t +\n\t2.\t -\n\t3.\t x\n\t4.\t / \n")

    try:
        num2 = float(input("Enter the second number"))
    except ValueError:
        print("Invalid input")
        continue

    if op == "+":
        print(f"The sum is {num1+num2}")
    elif op == "-":
        print(f"The difference is {num1-num2}")
    elif op == "x":
        print(f"The product is {num1*num2}")
    elif op == "/":
        if num2 != 0:
            print(f"The division  is {num1/num2}")
        else:
            print("nError\n 0 is no divisible as 2nd denominator")
    else:
        print("Invalid choice")


print("\nThanks for using , and bye!")