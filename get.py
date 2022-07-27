import json
from basic_functions import *
import copy
global accounts
accounts = None
import time


def get_accounts():
    global accounts
    if accounts == None:
        with open("address.json","r") as f:
            accounts = json.loads(f.read())
    return accounts

def display_accounts(account_list):
    print("Loading....")
    time.sleep(1)
    clear_screen()
    max_name_length = 0
    max_address_length = 0
    max_email_length = 0
    max_contact_length = 0

    for user in account_list.get('users'):
        if len(user.get('name')) > max_name_length:
            max_name_length = len(user.get('name'))
        if len(user.get('address')) > max_address_length:
            max_address_length = len(user.get('address'))
        if len(user.get('email')) > max_email_length:
            max_email_length = len(user.get('email'))
        if len(user.get('contact')) > max_contact_length:
            max_contact_length = len(user.get('contact'))

    difference_in_length_name = 0
    difference_in_length_address = 0
    difference_in_length_contact = 0
    difference_in_length_email = 0
    difference_in_index = 0
    temp = copy.deepcopy(account_list)
    print(show_title("Displaying All Contacts", (max_address_length+max_contact_length+max_email_length+max_name_length)))

    print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(
    "Name" + additional_space(max_name_length-len("Name")),
    "| Email" + additional_space(max_email_length - len("Email")),
    "| Contact" + additional_space(max_contact_length-len("Contact")),
    "| Address" + additional_space(max_address_length-len("Address"))))


    for user in temp.get("users"):

        if len(user.get('name')) < max_name_length:
            difference_in_length_name = max_name_length - len(user.get('name'))
        if len(user.get('address')) < max_address_length:
            difference_in_length_address = max_address_length - len(user.get('address'))
        if len(user.get('email')) < max_email_length:
            difference_in_length_email = max_email_length - len(user.get('email'))
        if len(user.get('contact')) < max_contact_length:
            difference_in_length_contact = max_contact_length - len(user.get('contact'))
        
        print("{}\t\t\t| {}\t\t\t| {}\t\t\t| {}".format(
            user.get('name') + additional_space(difference_in_length_name),
            user.get('email') + additional_space(difference_in_length_email),
            user.get('contact') + additional_space(difference_in_length_contact),
            user.get('address')  + additional_space(difference_in_length_address)))

def display_user(index: int):
    clear_screen()
    accounts = get_accounts()
    print("==============CONTACT PAGE=============")
    print("Name: {}".format(accounts.get('users')[index].get('name')))
    print("Email: {}".format(accounts.get('users')[index].get('email')))
    print("Contact: {}".format(accounts.get('users')[index].get('contact')))
    print("Address: {}".format(accounts.get('users')[index].get('address')))
    print("=======================================")

