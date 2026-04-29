import json

print("="* 22)
print("Contact book")
print("="* 22)

contact = []

# ----------ADD Contact ----------
def Add(contact):
    name = input("Name: ")
    number = input("Contact number: ")
    email = input("Email: ")

    contact.append({"Name":name,"Contact number" : number ,"Email": email  })

    print("Saved\n",flush=True)

# -------------Save Contact------------

def Save(contact):
    with open("Data.json", "w") as f:
        return json.dump(contact,f)
    
# ------------Search Contact-----------

def Search(contact):
    query = input("Search: ").lower()
    for i in contact:
        if (query in i["Name"].lower()):
            print(f"Name: {i['Name']} \n Contact number: {i["Contact number"]} \n Email: {i["Email"]} ") 
        else:
            print("It is not present in Data")

# ------------Delete Contact-----------

def Delete(contact):
    name = input("USER: ").lower()

    for i in contact:
        if i["Name"].lower() == name:
            contact.remove(i)
            print("Data is deleted!")
        
        else:
            print("Not found")

# ------------ Load ---------

def Load():
    try:
        with open("Data.json") as f:
            return json.load(f)
    
    except:
        return []



contact = Load()
while True:
    print("ADD(1) \nSEARCH(2) \nDELETE(3) \nQUIT(0)\n ")
    try:
        choice = int(input(">>> "))
        if (choice == 1):
            Add(contact)
            Save(contact)
        elif (choice == 2):
            Search(contact)
        elif (choice == 3):
            Delete(contact)
        else:
            break
    except:
        print("Enter a Valid number.....")    
