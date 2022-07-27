from get import *
from basic_functions import *

def search():
    keyword = str(input("Enter name: "))
    accounts = get_accounts()
    list_of_searched_users = dict()
    for item in accounts.get('users'):
        ctr = item.get('name').lower().find(keyword.lower())
        if ctr >= 0:
            temp = {
                accounts.get('users').index(item) : item
            }
            list_of_searched_users.update(temp)        
    display_searched_users(list_of_searched_users)

def display_searched_users(users_list):
    accounts=get_accounts()
    clear_screen()
    if len(users_list) > 0:
        for key in users_list.keys():
            print("[{}]. {}".format(key,users_list.get(key)['name']))
        # ask user to input something
        print("Enter index of user to be selected.")
        while True:
            # try:
            selection = int(input("Enter user index: "))
            if selection > len(accounts.get('users')):
                print('Index is out of bounds. Please try again')
            else:
                display_user(selection)
                break
            # except ValueError as e:
            #     print("Enter valid index! Please try again. "  + e)
            # except Exception as e:
            #     print(e)
    else:
        print("No results found.")