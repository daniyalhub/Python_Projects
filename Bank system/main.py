import json
import os
from datetime import datetime

class Account:
    def __init__(self,name,acc_no,balance = 0):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
        self.Created_at = datetime.now().strftime("%B %d, %Y")

    
    def Withdraw(self,amount):
        if amount <= 0:
            raise ValueError
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
    
    def Deposit(self,amount):
        if amount <= 0:
            raise ValueError
        self.balance  += amount

    def Transfer(self,amount,reciever):
        self.Withdraw(amount)
        reciever.Deposit(amount)
    
    def to_dict(self):
        return {
            "Name" : self.name,
            "Account Number" : self.acc_no,
            "Balance" : self.balance,
            "Date" : self.Created_at
        }
    
    def __str__(self):
        return f"[{self.acc_no} {self.name} Balence - {self.balance:.2f}]"
    
class Bank:
    File = "DATA.json"
    def __init__(self):
        self.accounts = {}
        self.Load()

    def Save(self):
        with open(self.File,"w") as f:
            json.dump(
                {k : v.to_dict() for k,v in self.accounts.items()},f, indent = 2
            )
    
    def Load(self):
        data = {}
        if os.path.exists(self.File):
            try:
                with open(self.File) as f:
                    data = json.load(f)
                for k,v in data.items():
                    self.accounts[k] = Account(v["Name"] , v["Account Number"], v["Balance"])

            except json.JSONDecodeError:
                self.data = {}
        
    def Create_Account(self,name):
        acc_no = str(1000 + 1 + len(self.accounts))
        acco = Account(name, acc_no)
        self.accounts[acc_no] = acco
        self.Save()
        print(f"Dear {name} \nYour account has created. Your account number is {acc_no}")

    def Get_Account(self,acc_no):
        acco = self.accounts.get(acc_no)
        if not acco:
            raise KeyError
        return acco
    
    def Withdraw_Amount(self,amount,acc_no):
        acco = self.Get_Account(acc_no)
        acco.Withdraw(amount)
        self.Save()
        print(f"Withdraw {amount} \nNew balance: {acco.balance:.2f}")

    def Deposit_Amount(self,amount,acc_no):
        acco = self.Get_Account(acc_no)
        acco.Deposit(amount)
        self.Save()
        print(f"Deposit {amount} \nNew balance: {acco.balance:.2f}")
    
    def Check_Account(self,acc_no):
        acco = self.Get_Account(acc_no)
        print(acco)

    def Transfer_Amount(self,amount,sender,rec):
        sen = self.Get_Account(sender)
        reciever = self.Get_Account(rec)
        sen.Transfer(amount,reciever)
        self.Save()
        print(f"Amount {amount} transfer from {sender} to {rec}")


def main():
    bank = Bank()
    while True:
        print("1. Create account")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Check balance")
        print("5. Transfer")
        print("0. Exit")
    
        try:
            choice = int(input(">>> "))
            if choice == 1:
                name = input("Name: ")
                bank.Create_Account(name)

            elif choice == 2:
                amount = float(input("Amount: "))
                acc_no = input("Account number")
                bank.Withdraw_Amount(amount,acc_no)
            elif choice == 3:
                amount = float(input("Amount: "))
                acc_no = input("Account number")
                bank.Deposit_Amount(amount,acc_no)

            elif choice == 4:
                acc_no = input("Account Number: ")
                bank.Check_Account(acc_no)
            elif choice == 5:
                amount = float(input(">>> "))
                sender = input("Enter sender account number: ")
                rec = input("Enter reciever account number: ")
                bank.Transfer_Amount(amount,sender,rec)
            elif choice == 0:
                break
            else:
                raise ValueError

        except (ValueError,TypeError) as e:
            print("Error: ", e)

if __name__ == "__main__":
    main()