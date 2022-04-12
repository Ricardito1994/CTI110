#CTI-110-0001
#P3HW2 - Pizza Order
#Ricardo Rivera
#4-11-22
##########################Pseudo-Code#################################
#Display 'Please enter number of students.'
#Input guest_num = int(input())
#Display 'Please enter number of students sharing a pizza'
#Input guest_pizza = float(input())
#Input if guest_pizza == 1.5:
#Set pizza_num = (guest_num / guest_pizza)
#Input elif guest_pizza == 2:
#Set pizza_num = (guest_num / guest_pizza)
#Input elif guest_pizza == 3:
#Set pizza_num = (guest_num / guest_pizza)
#Input else:
#Display 'INVALID ENTRY!!!!'
#Display 'Should have entered 1.5, 2 or 3'
#Display 'Run program again'
#Display exit()
#Set pizza_price = pizza_num * 5
#Set tax = pizza_price * .6
#Set price = pizza_price + tax
#Display '\n----Pizza Order--------'
#Display 'Number of Students:', (guest_num)
#Display 'Pizzas Needed:', format(pizza_num, '.0f')
#Display 'Price:', format(price, '.2f')
#Display '-------------------------'
######################################################################

print('Please enter number of students.')
guest_num = int(input())

print('Please enter number of students sharing a pizza')
guest_pizza = float(input())

if guest_pizza == 1.5:
    pizza_num = (guest_num / guest_pizza)
elif guest_pizza == 2:
    pizza_num = (guest_num / guest_pizza)
elif guest_pizza == 3:
    pizza_num = (guest_num / guest_pizza)
else:
    print('INVALID ENTRY!!!!')
    print('Should have entered 1.5, 2 or 3')
    print('Run program again')
    exit()

pizza_price = pizza_num * 5
tax = pizza_price * .6
price = pizza_price + tax
print('\n----Pizza Order--------')
print('Number of Students:',(guest_num))
print('Pizzas Needed:', format(pizza_num, '.0f'))
print('Price:', format(price, '.2f'))
print('-------------------------')
