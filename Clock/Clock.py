import time

def Clock():
    print("Press CTRL+C to exit")
    try:
        while True:
            print(time.strftime("%H:%M:%S"),end=" ",flush=True)
            time.sleep(1)
            print("\r",end="",flush=True)
    except KeyboardInterrupt:
        print("\nThanks for coming\n")

def Timer():
    print("Timer is started.Press CTRL + C to exit")
    try:
        second = int(input("Enter Second: "))
    except:
        print("Invalid Input")
        return
    try:
        while second > 0:
            mins ,sec = divmod(second,60)
        
            print(f"\r{mins:2}:{sec:2}",end="",flush=True)
            time.sleep(1)
            second -= 1
        print("Times up!")
    except KeyboardInterrupt:
        print("\nThanks for coming\n")

def Stopwatch():
    print("Press CTRL+C to exit")
    start = time.time()
    try:
        while True:
            elapsed = time.time() - start
            mins ,sec = divmod(int(elapsed),60)
            ms = int(elapsed - int(elapsed)) * 1000
            print(f"\r{mins:02}:{sec:02}:{ms:03}", end="", flush=True)
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("\nThanks for coming.\n")

print("==== Clock ====")
print("\nMenu:\n\t\u2022 Clock\n\t\u2022 Timer\n\t\u2022 Stopwatch")
while True:
    try:
        choice = input("Choice: ").lower()
        if choice =="exit":break
        elif choice == "clock":Clock()
        elif choice == "timer":Timer()
        elif choice == "stopwatch":Stopwatch()
        else:raise TypeError
    except:
        raise ValueError