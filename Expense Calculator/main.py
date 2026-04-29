import os
print("="*12)
print("Expense calculator")
print("="*12)

store = []


while True:
    name = input("Enter name of expense: ")
    expense = int(input("Enter amount of expense: "))
    date = input("Enter Date(YYYY-MM-DD): ")

    store.append((name,expense,date))
    
    exi_t = input("Are you want to add more(y/n): ")

    if exi_t == "n":
        break



if not os.path.exists("data"):
    os.mkdir("data")

with open("data/data.txt","a") as f:
    for i in store:
        f.write(f"{i[0]}: {i[1]}\n -------------------------------------\n")



total = 0
for item in store:
    total += item[1]


print(f"The total expense is { total}")

montly = input("You want monthly report (y/n): ")

if montly == "y":
    month = input("Enter month (YYYY-MM): ")

    total_month = 0

    print("\n--- Monthly Report ---")

    for item in store:
        date = item[2]
        name = item[0]
        expense = item[1]

        if date.startswith(month):
            print(date, name, expense)
            total_month += expense

    print("\nMonthly Total:", total_month)







