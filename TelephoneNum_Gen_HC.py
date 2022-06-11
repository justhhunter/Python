# Hunter Copening
# 6/7/2022

# Telephone Number Word Generator Lab

# This program will accept a user input as a phone number 
# It will then generate all the possible word combinations for that phone number using
# the corresponding letters and numbers on a standard telephone.

# (avoid phone number with 0s or 1s because they do not correspond to any letters)





# importing product function

from itertools import product


# stores keys assigned to letters
phone_dictionary = {
    '2':['A','B','C'], 
    '3':['D','E','F'], 
    '4':['G','H','I'], 
    '5':['J','K','L'], 
    '6':['M','N','O'], 
    '7':['P','R','S'], 
    '8':['T','U','V'], 
    '9':['W','X','Y'],
    }



# takes user input
user_phone = input("""
Enter the 7 digit phone number you would 
like to get word combinations for:  """)


# iterator stored as list
# basically nested for loop
sequence = list(product(
phone_dictionary[user_phone[0]],
phone_dictionary[user_phone[1]],
phone_dictionary[user_phone[2]],
phone_dictionary[user_phone[3]],
phone_dictionary[user_phone[4]],
phone_dictionary[user_phone[5]],
phone_dictionary[user_phone[6]]))


#  makes list easier to read for regular user
combinations = ["".join(i) for i in sequence]

# displays result
print(combinations)




