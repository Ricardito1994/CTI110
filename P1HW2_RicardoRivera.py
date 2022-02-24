#Finding out the Number of Pizzas I need to order for my group of Students.
#February 23, 2022
#CTI-110 P1HW2-Pizza Order
#Ricardo Rivera
#
##########################Pseudo-Code################################
#Create a variable for students
#create an integer input/ int(input()) with quotation that allows the user to enter the number of students.
#In the quotation type Enter number of students to order pizza for.
#Create a variable for slices
#Create a variable for pizzas
#Create an equation that finds the amount of slices needed.
#slices = students * 3/ to find the number of slices needed.
#Create an equation that finds the amount of Pizzas needed.
#pizzas = students / 2/ to find the number of pizzas needed.
#Print statement, with quotation "\n----Pizza Order--------"
#Print statement, with quotation "Number of Students: ", with the variable of students inside ()
#Print statement, with quotation "Pizza Slices needed: ", with the variable of slices inside ()
#Print statement, with quotation "Pizzas needed: ", with the variable of pizzas iinside ()
#Print statement, with quotation "----------------------"
#####################################################################

#Enter Number of Students.
students = int(input("Enter number of students to order pizza for."))

#Calculate Number of Pizzas and Slices.
slices = students *3
pizzas = students / 2

#Display Results
print("\n----Pizza Order--------")
print("Number of Students: ", students)
print("Pizza Slices needed: ", slices)
print("Pizzas needed: ", pizzas)
print("-----------------------")
