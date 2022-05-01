#This program I will use a loop to display scores and letter grades.
#CTI-110
#P4HW1 - Score List
#Ricardo Rivera
#4-30-22
#
##############################Psuedo-Code###########################
#Input num_scores=int(input("How many scores do you want to enter?(Enter at least 2):'))
#List scores=[]
#Loop for num in range(1, num_scores + 1):
#Input score=float(input('Enter score #'+str(num)+':'))
#Loop while score < 0 or score > 100:
#Display print('INVALID Score entered!!!!\nScore should be between 0 and 100:')
#Input score=float(input('Enter score #'+str(num)+' again:'))
#Set scores.append(score)
#Set final_scores=scores
#Set lowest_score=min(final_scores)
#Set final_scores.remove(lowest_score)
#Set score_average=sum(final_scores)/len(final_scores)
#Input if score_average >= 90:
#Set grade='A'
#Input elif score_average >= 80:
#Set grade='B'
#Input elif score_average >= 70:
#Set grade='C'
#Input elif score_average >= 65:
#Set grade='D'
#Input else:
#Set grade='F'
#Display print('--------Results----------')
#Display print('Lowest Scores:', lowest_score)
#Display print('Modified List:', final_Scores)
#Display print('Score Average:', score_average)
#Display print('Grade:',grade)
#Display print('-------------------------')
####################################################################

num_scores=int(input('How many scores do you want to enter?(Enter at least 2):'))
scores=[]
print()
for num in range(1, num_scores + 1):
    score=float(input('Enter score #'+str(num)+':'))
    while score < 0 or score > 100:
        print()
        print('INVALID Score entered!!!!\nScore should be between 0 and 100')
        score=float(input('Enter score #'+str(num)+' again:'))
    scores.append(score)

final_scores=scores
lowest_score=min(final_scores)
final_scores.remove(lowest_score)
score_average=sum(final_scores)/len(final_scores)

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
print()
print()
print('------------Results------------')
print('Lowest Scores:', lowest_score)
print('Modified List:', final_scores)
print('Score Average:',format(score_average, '.2f'))
print('Grade:', grade)
print('-------------------------------')
