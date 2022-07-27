import json
from get import *

def add(new_entry):
    accounts = get_accounts()
    accounts.get('users').append(new_entry)
    with open('address.json', 'w') as f:
        f.write(json.dumps(accounts,indent=2))

def add_input():
    clear_screen()
    while True:
        name = input("*Enter name: ") #required
        address = input("*Enter address: ") #required
        email = input("Enter email: ")
        contact = input("Enter contact: ")
        if (name == None or name.strip() == "") or (address == None or address.strip() == ""):
            print("Please enter the required fields.")
        else:
            new_entry = {
                "name" : name,
                "email" : email,
                "address" : address,
                "contact" : contact
            }
            add(new_entry)
            clear_screen()
            print(name + " is successfully added!\n")
            break
