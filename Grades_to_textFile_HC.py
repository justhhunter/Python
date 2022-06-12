# Hunter Copening

# 6/11/2022

# Figure 3.2 Class Averages 
# This program will take user input for any number of values then calculate an average

# This program has been modified from the original to store grades in text file



# opens the text file with grades for user to view
with open('Grades_HC.txt', 'r') as file:
    view = file.read()
    print('Class average is', view)
    file.close()
    pass



# fig03_02.py 
"""Class average program with sentinel-controlled iteration."""

# initialization phase
total = 0 # sum of grades
grade_counter = 0 # number of grades entered

# processing phase

grade = int(input('Enter grade, -1 to end: '))



while grade != -1:
    total += grade
    grade_counter += 1
    grade = int(input('Enter grade, -1 to end: '))



# termination phase
if grade_counter != 0:

    average = total / grade_counter
    
    text = print('Class average is ', format(average, '.2f'))

    # opens text file to rewrite with new grade average
    with open('Grades_HC.txt', 'w') as file:
        file.write(str(average))
        file.close()
        pass
            

else:
    print('No grades were entered')



