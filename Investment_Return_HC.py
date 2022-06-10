# Hunter Copening
# 6/5/2022

# Investment Return Program

# This program will use a formula to determine the rate of return for an investment.
# It will use three different values for the period of years value, then display each output.


# main module

def main():

    # initialize variables
    p = 1000

    r = 0.07

    n = 10, 20, 30

    # This is the formulas for 10, 20, and 30 year investment periods
    invest10 = p*(1+r)**n[0]

    invest20 = p*(1+r)**n[1]

    invest30 = p*(1+r)**n[2]

    invest10rounded = round(invest10, 2)
    
    invest20rounded = round(invest20, 2)

    invest30rounded = round(invest30, 2)

    # displaying the outputs from the above equations

    print('This is your investment of $1000 after 10 years: $',invest10rounded,'profit')

    print('This is your investment of $1000 after 20 years: $',invest20rounded,'profit')

    print('This is your investment of $1000 after 30 years: $',invest30rounded,'profit')






# start main module
main()