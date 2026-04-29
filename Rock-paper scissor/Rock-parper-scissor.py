import random
def get_data(user,comp):
    if user == comp:
        return 'draw'
    
    elif (
        (user == "rock"    and comp == "scissor") or 
        ( user == "scissor" and comp == "paper") or 
        ( user == "paper"   and comp == "rock")
        ):
        return 'user'
    
    else:
        return 'comp'
    
def play_game():
    print("=-="*18)
    print("Rock paper scissors")
    print("=-="*18)
    choices = ["rock","paper","scissor"]

    u_score = 0
    c_score = 0
    while True:
        user = input("Enter your choice(type exit to leave): ").lower()
        comp = random.choice(choices)
    
        if user == 'exit':
            print("\nThanks! for coming")
            break
        
        if user not in choices:
            print("Invalid choice")
            continue
        
        result = get_data(user,comp)

        if result == "draw":
            print("Its draw")

        elif result == 'user':
            print("You wins")
            u_score += 1
        
        else:
            print("Comp wins")
            c_score += 1

        print(f"Score -> You: {u_score} | Computer: {c_score}")

    print(f"FinalScore -> You: {u_score} | Computer: {c_score}")

play_game()