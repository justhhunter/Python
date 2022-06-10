#Hunter Copening
#6/6/2022

#Lab Miles Per Gallon

# This program will take user input for miles driven and gallons used per trip. It will then calculate
# the MPG for each full tank of gas. After processing it will display the output which will be the
# sum of total MPG for all trips.



# main module
def main():



    # sentinel value
    sentinel = -1

    #initialize variables
    gallons = 0

    miles = 0
    totalgallons = 1
    totalmiles = 0
    total = 0
    
    # while loop using sentinel
    while gallons != sentinel:
        # prompt user input for gallons variable
        
        gallons = float(input('Enter the gallons used (-1 to end): '))
        # counter for total gallons
        totalgallons = totalgallons + gallons


        # if statement will stop rest of script from running if sentinel is input
        if not gallons == sentinel:
            # prompt user for miles variable
            miles = float(input('Enter the miles driven: '))
            # counter for total miles
            totalmiles = totalmiles + miles
            

            
            # MPG calculation and display
            MPG = miles / gallons
            print(MPG)
    # calculates total MPG for all trips        
    if gallons == sentinel:
        total = totalmiles / totalgallons
        print(total)



main()