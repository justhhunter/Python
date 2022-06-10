# Hunter Copening
# 6/5/2022

# Heart Rate Extra Credit Program

# This program will take user input for age, then will determine maximum heart rate.
# It will also display a range for the users target heart rate based on the maximum heart rate.



# main module




def main():

    # initialize variables
    # collects data from user
    age = int(input('Please enter your age: '))

    # determines max heart rate
    maximum = 220 - age

    # determines range of target heart rate
    min_heart_rate = maximum * 0.5

    max_heart_rate = maximum * 0.85

    # turns float values into integers for user display purposes
    min_heart_rate = int(min_heart_rate)

    max_heart_rate = int(max_heart_rate)

    # displays output
    print('Your maximum heart rate is',maximum,'beats per minute')

    print('Your target heart rate is between',min_heart_rate,'and',max_heart_rate,'beats per minute')

    # disclaimer
    print("""
    These formulas are estimates provided by the AHA; 
    maximum and target heart rates may vary based on the 
    health, fitness, and gender of the individual. 
    Always consult a physician or qualified 
    healthcare professional before beginning or 
    modifying an exercise program.""")




# running main
main()