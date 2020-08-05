import os


def validate(number1, number2):
    if (number1 < 1 or number1 > 4) or (number2 < 1 or number2 > 4) == True:
        return False
    return True


def cls():
    clear = lambda: os.system('clear')
    clear()


def clear_screen():
    clear = lambda: os.system('cls')
    clear()