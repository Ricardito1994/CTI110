#This program I will use loop and functions to display scores and letter grades.
#CTI-110
#P5HW1 - Score List
#Ricardo Rivera
#5-2-22
#
##############################Psuedo-Code###########################
#Function def main():
#Set scores =[]
#Set option = 0
#Loop while option != 3:
#Set menu()
#Input option = int(input('Enter your option'))
#Statement if option == 1:
#Set scores = type_scores(scores)
#Statement elif option == 2:
#Statement if len(scores) == 0:
#Display print('You need to create list first.')
#Statement else:
#List lowest_score, final_score, score_average, grade = calc_avg_score(scores)
#Display print()
#Display print()
#Display print('--------------Results--------------')
#Display print('Lowest Scores:', lowest_score)
#Display print('modified List:', final_score)
#Display print('Score Average:', format(score_average, '.2f'))
#Display print('Grade:', grade)
#Display print('-----------------------------------')
#Display print()
#Statement elif option == 3:
#Display print('Exit Code')
#Statement else:
#Display print('You have entered an invalid option!')
#Display print()
#Function def menu():
#Display print('[1] Create Score List')
#Display print('[2] Display Results')
#Display print('[3] Exit')
#Function def type_scores(scores):
#Input num_scores = int(input('How many scores do you want to enter?(Enter at least 2):'))
#Loop for num in range(1, num_scores + 1):
#Input score = float(input('Enter score #' + str(num) + ':'))
#Loop while score < 0 or score > 100:
#Display print('INVALID Score entered!!!!\nScore should be between 0 and 100')
#Input score = float(input('Enter score #' + str(num) + 'again:'))
#Set scores.append(score)
#Function Return scores
#Function def calc_avg_score(scores):
#Set final_score = scores
#Set lowest_score = min(scores)
#Set final_score.remove(lowest_score)
#Set score_average = sum(final_score) / len(final_score)
#Statement if score_average >= 90:
#Input grade = 'A'
#Statement elif score_average >= 80:
#Input grade = 'B'
#Statement elif score_average >= 70:
#Input grade = 'C'
#Statement elif score_average >= 65:
#Input grade = 'D'
#Statement else:
#Input grade = 'F'
#Function Return final_score, lowest_score, score_average, grade
#Statement if__name__ == "__main__":
#Set main()
####################################################################


    
def main():
    scores=[]
    option=0
    while option != 3:
        menu()
        option = int(input('Enter your option'))
        if option == 1:
            scores = type_scores(scores)
        elif option == 2:
            if len(scores) == 0:
                print('You need to create list first.')
            else:
                lowest_score, final_score, score_average, grade = calc_avg_score(scores)
                print()
                print()
                print('------------Results------------')
                print('Lowest Scores:', lowest_score)
                print('Modified List:', final_score)
                print('Score Average:',format(score_average, '.2f'))
                print('Grade:', grade)
                print('-------------------------------')
                print()
        elif option == 3:
            print('Exit Code')
        else:
            print('You have entered an invalid option!')
            print()

def menu():
    print('[1] Create Score List')
    print('[2] Display Results')
    print('[3] Exit')

def type_scores(scores):
    num_scores=int(input('How many scores do you want to enter?(Enter at least 2):'))
    for num in range(1, num_scores + 1):
        score=float(input('Enter score #'+str(num)+':'))
        while score < 0 or score > 100:
            print('INVALID Score entered!!!!\nScore should be between 0 and 100')
            score=float(input('Enter score #'+str(num)+' again:'))
        scores.append(score)
    return scores
        
def calc_avg_score(scores):
    final_score = scores
    lowest_score = min(scores)
    final_score.remove(lowest_score)
    score_average = sum(final_score)/len(final_score)

    if score_average >= 90:
        grade='A'
    elif score_average >= 80:
        grade='B'
    elif score_average >= 70:
        grade='C'
    elif score_average >= 65:
        grade='D'
    else:
        grade='F'
    return final_score, lowest_score, score_average, grade


if __name__ == "__main__":
    main()
