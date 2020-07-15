# Ian Maze
# COP2002.0M1/0M2
# March, 23, 2020
# Real Estate (Even, Odd, Avg, median, min, max calculator)
# This program uses input from the user to calculate averages with real estate
# prices

#Display the calculator
def display():
    print()
    print("-------------------------------------------------------")
    print("              Real Estate Price Calculator             ")
    print("-------------------------------------------------------")
    print()
    print("This program will calculate the following:")
    print("Average\nMedian\nMinimum\nMaximum")
    print("from a list of given prices")
    print("-------------------------------------------------------")

#Calculate data to display
def do_the_math():
    choice = "Yes"
    count = 0
    data = []
    number = 0
    median_value = 0
    average_value = 0
    minimum_value = 0
    maximum_value = 0

    #Getting data from user
    while number != -99:
        number = int(input("Please enter the cost of one home, or -99 to quit: $"))
        data.append(number)
        count += 1
        choice = "Y"
    data.remove(-99)

    #Meadian Calculation
    length = len(data)
    if (length % 2 == 0):
        median_value = (data[(length)//2] + data[(length)//2-1]) / 2
    else:
        median_value = data[(length-1)//2]

    #Average Calculation
    average_value = sum(data) / len(data)

    #Minimum Calculation
    minimum_value = min(data)

    #Maximum Calculation
    maximum_value = max(data) 

    #Calling the display_end function
    display_end(data, median_value, average_value,
    maximum_value, minimum_value)
        
    
    
#Display Results
def display_end(a,b,c,d,e):
    choice = "y"
    print("-------------------------------------------------------")
    print("Prices of homes in your area:")
    print("-----------------------------")
    print(a)
    print("-------------------------------------------------------")
    print("The median sale price is $", b)
    print("The average sale price is $", c)
    print("The minimum sale price $", e)
    print("The maximum sale price $", d)
    print()
    choice = input("Would you like to continue? (y/n): ")
        
    if choice.lower() == 'n':
        print()
        print("-------------------------------------------------------")
        print("Goodbye")
        print("-------------------------------------------------------")

    else:
        main()
        
#Main function
def main():
    display()
    do_the_math()

if __name__ == "__main__":
	main()

