#CTI-110-0001
#P3HW2 - Pizza Order
#Ricardo Rivera
#4-11-22
##########################Pseudo-Code#################################
#Input go_again = 'y'
#Loop while go_again =='y' or go_again == 'Y'
#Input guest_num = int(input('How many students do you want to order pizza for?'))
#Input guest_pizza = float(input('Enter number of people per pizza (1.5, 2, 3):'))
#Loop while guest_pizza not in (1.5, 2, 3):
#Display ('INVALID ENTRY!!!!')
#Display ('Should have entered 1.5, 2, or 3')
#Display ()
#Input guest_pizza = float(input('Enter number of people per pizza again. (1.5, 2 , 3):'))
#Input if guest_pizza == 1.5:
#Set pizza_num = (guest_num / guest_pizza)
#Input elif guest_pizza == 2:
#Set pizza _num = (guest_num / guest_pizza)
#Input elif guest_pizza == 3:
#Set pizza_num = (guest_num / guest_pizza)
#Set pizza_price = pizza_num * 5
#Set tax = pizza_price * .6
#Set price = pizza_price + tax
#Display print('\n----Pizza Order--------')
#Display print('Number of Students:', (guest_num))
#Display print('Pizzas Needed:', format(pizza_num, '.0f'))
#Display print('Price:', format(price, '.2f'))
#Display print('--------------------------')
#Input go_agian = input('Would you like to run progran again (y for yes):')
#Input if not go_again == 'y' or go_again == 'Y':
#Display print('Goodbye!')
######################################################################
go_again = 'y'
while go_again == 'y' or go_again == 'Y':

    guest_num = int(input('How many students do you want to order pizza for?'))

    guest_pizza = float(input('Enter number of  people per pizza(1.5, 2, 3):'))

    while guest_pizza not in (1.5, 2, 3):
        print('INVALID ENTRY!!!!')
        print('Should have entered 1.5, 2 or 3')
        print()
        guest_pizza = float(input('Enter number of  people per pizza again. (1.5, 2, 3):'))
        
    if guest_pizza == 1.5:
        pizza_num = (guest_num / guest_pizza)
    elif guest_pizza == 2:
        pizza_num = (guest_num / guest_pizza)
    elif guest_pizza == 3:
        pizza_num = (guest_num / guest_pizza)

    pizza_price = pizza_num * 5
    tax = pizza_price * .6
    price = pizza_price + tax

    print('\n----Pizza Order--------')
    print('Number of Students:',(guest_num))
    print('Pizzas Needed:', format(pizza_num, '.0f'))
    print('Price:', format(price, '.2f'))
    print('-------------------------')

    go_again = input('would you like to run program again (y for yes):')

if not go_again == 'y' or go_again == 'Y':
     print('Goodbye!')
