from menu_item import Food, Drink
import utils
import time
import platform


food1 = Food('Sate', 10000, 100)
food2 = Food('Soto', 15000, 500)
food3 = Food('Bakso', 13000, 600)
food4 = Food('Lawar', 20000, 375)
foods = ['', food1, food2, food3, food4]

drink1 = Drink('Es Teh', 3000, 250)
drink2 = Drink('Es Jeruk', 4000, 250)
drink3 = Drink('Soda Gembira', 10000, 370)
drink4 = Drink('STMJ', 2500, 300)
drinks = ['', drink1, drink2, drink3, drink4]


while True:
    print('-' * 20)
    print('| Our menu today:  |')
    print('-' * 20)
    print('FOOD')
    x = 1
    for food in foods:
        if food == '':
            continue
        print(str(x) + '.', food.name, 'Rp' + str(food.price), food.netto, 'Gram')
        x += 1
    print('')

    print('DRINK')
    x = 1
    for drink in drinks:
        if drink == '':
            continue
        print(str(x) + '.', drink.name, 'Rp' + str(drink.price), drink.volume, 'mL')
        x += 1

    print('')
    print('What do you want to order?')
    time.sleep(0.4)
    print('For FOOD')
    customer_food = int(input('Input number 1-4 (depend on menu number): '))

    print('For DRINK')
    customer_drink = int(input('Input number 1-4 (depend on menu number): '))

    if utils.validate(customer_food, customer_drink):
        print('You chose:', foods[customer_food].name, '&', drinks[customer_drink].name)
        print('')
        print('If you order more or equal to 3, for each item you get discount 80%')
        count_food = int(input('How many FOOD do you want to order? '))
        count_drink = int(input('How many DRINK do you want to order? '))
        customer_total_price = foods[customer_food].get_total_price(count_food) + \
                               drinks[customer_drink].get_total_price(count_drink)
        print('Your total price is', 'Rp' + str(round(customer_total_price)))
        time.sleep(5)

    else:
        print('Input valid number')
        x = 3
        while x >= 1:
            print('Restart program in', x, 'second')
            x -= 1
            time.sleep(1)

    if platform.system() == 'Windows':
        utils.clear_screen()
    elif platform.system() == 'Linux' or 'Darwin':
        utils.cls()
