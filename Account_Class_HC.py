# Hunter Copening

# 6/11/2022


# Figure 10.2.2 Account Class

# account.py
#Account class definition



from decimal import Decimal


#account class for maintaining bank account
class Account:
    
    # initialize an account object
    def __init__(self, name, balance):
        print("""Initialize an Account object""")
        # if balance less than 0.00 raise an exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00')

        self.__name = name
        self.__balance = balance
        
        
        
        
    def deposit(self, amount):
        print("""Deposit money to the account.""")

        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')

        self.__balance += amount
        


# access the class and print these variables
# currently I have added 2 underscores to the objects
# this makes them private and only accessible inside of the class
# if you remove them then you will be able to execute the following code without error 

account1 = Account('John Green', Decimal('50.00'))
print(account1.__name)
print(account1.__balance)



