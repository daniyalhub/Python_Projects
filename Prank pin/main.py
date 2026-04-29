print("="*20)
print("        Pin Quess")
print("="*20)

pin = "1234"
attempt = 3
while True:
    user = input("Enter pin(0 for exit): ")

    if user == "0":
        print("Exiting program......",flush=True)
        break

    if user != pin:
        attempt -= 1
        if attempt > 0:
            print(f"You have {attempt} {'tries' if attempt > 1 else "try" }")
        if attempt == 0:
            print("\nYour pc is locked for 224 centries")
            break
    else:
        print("You are save")
        