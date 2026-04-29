import json
import os


class Account:
    def __init__(self,name , acc_no,balance = 0):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def withdraw(self,amount):
        if(amount <= 0 ):
            raise ValueError
        if(amount > self.balance):
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def deposit(self, amount):
        if(amount <= 0):
            raise ValueError("Invalid amount")
        self.balance += amount
    
    def to_dict(self):
        return {
            "name": self.name,
            "account_number": self.acc_no,
            "balance": self.balance
        }
    
    def transfer(self, there,amount):
        self.withdraw(amount)
        there.deposit(amount)
    
    def __str__(self):
        return f"[{self.acc_no}] {self.name} — Balance: Rs.{self.balance:.2f}"


class Bank:
    File = "Data.json"
    def __init__(self):
        self.accounts={}
        self.load()

    def save(self):
     
        with open(self.File,"w") as f:
            json.dump(
                { k : v.to_dict() for k,v in self.accounts.items()}, f, indent=2
            )

    def load(self):
        data = {}
        if os.path.exists(self.File):
            try:
                with open(self.File,"r") as f:
                    data =  json.load(f)
                for k,v in data.items():
                    self.accounts[k] = Account(v["name"], v["account_number"], v["balance"])
            except json.JSONDecodeError:
                self.data ={}
        
    
    def create_account(self,name):
        acc_no = str(1000 + len(self.accounts)+1)
        acc = Account(name , acc_no)
        self.accounts[acc_no] = acc
        self.save()
        print(f"Dear {name} \n Your account is created your account number is {acc_no}")

    def get_account(self,acc_no):
        acc = self.accounts.get(acc_no)
        if not acc:
            raise KeyError("Account not Found")
        return acc
    def Withdraw(self, acc_no,amount):
        acc = self.get_account(acc_no)
        acc.withdraw(amount)
        self.save()
        print(f"Withdraw {amount} - New balance is {acc.balance:.2f} ")
        
    def Deposit(self,acc_no , amount):
        acc = self.get_account(acc_no)
        acc.deposit(amount)
        self.save()
        print(f"Deposit {amount} - New balance is {acc.balance:.2f} ")

    def Balance(self,acc_no):
        acc = self.get_account(acc_no)
        print(acc)

    def Transfer(self,from_,there,amount):
        sender = self.get_account(from_)
        transfer_acc = self.get_account(there)
        sender.transfer(transfer_acc, amount)
        print(f"Transferred Rs.{amount} from {from_} to {there}")

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
                bank.create_account(name)
                
            
            elif choice == 2:
                withdraw_amount = float(input("Enter amount: "))   
                acc_no =input("Account number: ")
                bank.Withdraw(acc_no,withdraw_amount)
            
            elif choice == 3:
                deposit_amount = float(input("Enter amount: "))   
                acc_no = input("Account number: ")
                bank.Deposit(acc_no,deposit_amount)

            elif choice == 4:
                acc_no = input("Account number: ")
                bank.Balance(acc_no)

            elif choice == 5:
                from_ = input("Enter account: ")
                there = input("Enter Transfer account: ")
                amount = float(input("Enter Amount"))
                bank.Transfer(from_,there,amount)

            elif choice == 0:
                print("Goodbye!")
                break

            else:
                raise TypeError

        except (TypeError,ValueError) as v:
            print("Error",v)
            continue


if __name__ == "__main__":
    main()