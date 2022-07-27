import json
import os
from get import *
from add import *
from search import *


def menu():
    while True:
        print("\nWelcome to Address Book!\n")
        print("[1]. Display Users")
        print("[2]. Add User")
        print("[3]. Search Users")
        print("[4]. Update Users")
        print("[5]. Delete Users")
        while True:
            # try:
            selection = int(input("Enter menu selection: "))
            if selection == 1:
                clear_screen()
                display_accounts(get_accounts())
                break
            elif selection == 2:
                add_input()
                break
            elif selection == 3:
                search()
                break
            else:
                print("Something went wrong!")
            # except ValueError as e:
            #     print("Enter valid number only "+e)
            # except Exception as e:
            #     print(e)


menu()