import os

def clear_screen():
    os.system("cls")

def additional_space(difference):
    if difference == None:
        return
    return " " * difference

def show_title(title, total_length: int):
    title_length = len(title)
    each_side = int(((78 + total_length) - title_length) / 2)
    return ("=" * each_side) + title + ("=" * each_side)