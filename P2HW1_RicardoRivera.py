#In this project I am building a code that calculates the total purchase of the 5 items.
#3/16/2022
#CTI-110 P2HW1-Total Purchases
#Ricardo Rivera
#
###########################Pseudo-Code#########################
#Display "Enter the price of item #1: "
#Input item_1
#Display "Enter the price of item #2: "
#Input item_2
#Display "Enter the price of item #3: "
#Input item_3
#Display "Enter the price of item #4: "
#Input item_4
#Display "Enter the price of item #5: "
#Input item_5
#Set Subtotal = item_1 + item_2 + item_3 + item_4 + item_5
#Set Sales_Tax = Subtotal * 0.07
#Set Overall_Total = Subtotal + Sales_Tax
#Display "\n-------Results-------"
#Display "Subtotal: ", format(Subtotal, '.2f'))
#Display "Sales Tax: ", format(Sales_Tax, '.2f'))
#Display "Total: ", format(Overall_Total, '.2f'))
##############################################################

#Enter 5 input statements for the 5 items.
item_1 = float(input('Enter the price of item #1: '))
item_2 = float(input('Enter the price of item #2: '))
item_3 = float(input('Enter the price of item #3: '))
item_4 = float(input('Enter the price of item #4: '))
item_5 = float(input('Enter the price of item #5: '))

#Calculation of Subtotal for the 5 items.
Subtotal = item_1 + item_2 + item_3 + item_4 + item_5

#Calculation for the Sales Tax of the item prices entered.
Sales_Tax = Subtotal * 0.07

#Calculation for the overall total price.
Overall_Total = Subtotal + Sales_Tax

#Display Results
print('\n-------Results-------')
print('Subtotal: ', format(Subtotal, '.2f'))
print('Sales Tax: ', format(Sales_Tax, '.2f'))
print('Total: ', format(Overall_Total, '.2f'))
