#This code is meant to have a menu that allows the student to enter 1 so that they can add random numbers
#This code is also allows the student to subtract random numbers as long as they select the number 2
#5-9-22
#CTI-110 P2HW2-Math Quiz
#Ricardo Rivera
#
#####################Pseudo-Code#######################
#Function def main():
#Set choice = 0
#Loop while choice != 3:
#Set main_menu()
#Input choice = int(input('Please choose one of the menu options:'))
#Statement if choice == 1:
#Input add_rand_num()
#Statement elif choice == 2:
#Input sub_rand_num()
#Statement elif choice == 3:
#Display print('Thank you for playing...')
#Display print('Bye!!')
#Function def main_menu():
#Display print('Welcome to Math Quiz')
#Display print()
#Display print('MAIN MENU')
#Display print('--------------------')
#Display print('1. Adding Random Numbers')
#Display print('2. Subtracting Random Numbers')
#Display print('3. Exit')
#Function add_rand_num():
#Display print('Add the numbers.')
#Statement from random import randint
#Input num1 = randint(1, 100)
#Input num2 = randint(1, 100)
#Display("", num1)
#Display("+", num2)
#Set sum = num1 + num2
#Input guess = Int(input('Enter answer.')
#Set count = 1
#Loop While guess != sum:
#Set count += 1
#Statement if guess > sum:
#Display print('Sorry, guess is too high.')
#Statement elif guess < sum:
#Display print('Sorry, guess is too low.')
#Input guess = int(input('Try again:'))
#Statement else:
#Display print('Congradulations!!!! Your answer is correct..')
#Display print('Number of guessess:', count)
#Function def sub_rand_num():
#Display print('Subtract the numbers.')
#Statement from random import randint
#Input num1 = randint(1, 100)
#Input num2 = randint(1, 100)
#Display print("", num1)
#Display print("-". num2)
#Input difference = num1 - num2
#Input guess = int(input('Enter answer.'))
#Set count = 1
#Loop while guess != difference:
#Set count += 1
#Statement if guess > difference:
#Display print('Sorry, your guess was too high.')
#Statement elif guess < difference:
#Display print('Sorry, your guess was too low.')
#Input guess = int(input('Try again:'))
#Statement else:
#Display print('Congradulations!!!! Your answer is correct..')
#Display print('Number of guesses:', count)
#Set main()
#######################################################

def main():
    choice = 0
    while choice != 3:
        main_menu()
        choice = int(input('Please choose one of the menu options:'))
        if choice == 1:
            add_rand_num()
        elif choice == 2:
            sub_rand_num()
        elif choice == 3:
            print('Thank you for playing...')
            print('Bye!!')

    
def main_menu():
    print('Welcome to Math Quiz')
    print()
    print('MAIN MENU')
    print('--------------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')

       
def add_rand_num():
    print('Add the numbers.')
    from random import randint
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    print("", num1)
    print("+", num2)
    sum = num1 + num2
    guess = int(input('Enter answer.'))
    count = 1
    while guess != sum:
        count += 1
        if guess > sum:
            print('Sorry, guess is too high.')
        elif guess < sum:
            print('Sorry, guess is too low.')
        guess = int(input('Try again:'))

    else:
        print('Congradulations!!!! Your answer is correct..')
        print('Number of guesses:', count)
                
                     
def sub_rand_num():
    print('Subtract the numbers.')
    from random import randint
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    print("", num1)
    print("-", num2)
    difference = num1 - num2
    guess = int(input('Enter answer.'))
    count = 1

    while guess != difference:
        count += 1
        if guess > difference:
            print('Sorry, your guess is too high.')
        elif guess < difference:
            print('Sorry, your guess is too low.')
        guess = int(input('Try again:'))

    else:
        print('Congradulations!!!! Your answer is correct..')
        print('Number of guesses:', count)
        
main()
    
    


          
        
    



        
        
        
        
   
