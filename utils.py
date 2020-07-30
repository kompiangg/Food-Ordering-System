import os


def validate(number):
    if number < 0 or number > 3:
        return False
    return True


def cls():
    clear = lambda: os.system('clear')
    clear()


def clear_screen():
    clear = lambda: os.system('cls')
    clear()