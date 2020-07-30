from menu_item import MenuItem
import platform
import utils


food1 = MenuItem('Sate', 10000)
food2 = MenuItem('Soto', 15000)
food3 = MenuItem('Bakso', 13000)
food4 = MenuItem('Lawar', 20000)
foods = [food1, food2, food3, food4]

while True:
    print('-' * 20)
    print('| Our menu today:  |')
    print('-' * 20)

    x = 0
    for food in foods:
        print(str(x) + '.', food.name, food.price)
        x += 1

    print('What do you want to order?')
    customer_food = int(input('Input number 0-3 (depend on menu number): '))

    if utils.validate(customer_food):
        print('You chose:', foods[customer_food].name)
        print('')
        print('If you order more or equal to 3 you get discount 80%')
        count = int(input('How many do you want to order? '))
        customer_total_price = foods[customer_food].get_total_price(count)
        print('Your total price is', round(customer_total_price))

    else:
        print('Input valid number')
        if platform.system() == 'Windows':
            utils.clear_screen()
        elif platform.system() == 'Linux' or 'Darwin':
            utils.cls()
