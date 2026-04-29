from datetime import datetime

print("It calculate the dats,weeks,months,years")
print("Please enter the date in this format YYYY-MM-DD(eg: 2000-01-01)")

while True:
    try:
        d1 = input("Enter 1st date(0 to exit)").strip()
        if d1 == "0":break 
        d2 = input("Enter 2nd date").strip() 

        date_1 = datetime.strptime(d1,"%Y-%m-%d")
        date_2 = datetime.strptime(d2,"%Y-%m-%d")

        if date_1 > date_2:
            date_1,date_2 = date_2,date_1

        diff = date_2 - date_1
        days = diff.days
        weeks = days // 7
        left_over_days = days % 7
        months = days // 30
        left_over_days_from_months = days % 30
        years = days // 365

        print(f"\nDays - {days}")
        print(f"Weeks - {weeks} and {left_over_days}")
        print(f"Months - {months} and {left_over_days_from_months}")
        print(f"Years - {years}")

    except ValueError as v:
        print("Error:",v)

print("Thanks for using this program!")