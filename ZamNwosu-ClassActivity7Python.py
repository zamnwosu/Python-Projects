# Programmer: Zam Nwosu
# Purpose: Demonstrate functions
# Input: 1) User choice of menu 2) User choice less than 1 or greater than 10 (for valid function)
# Output: Output from number exercise

# Declare variables
floatNum1 = 23.567
floatNum2 = 0.0
floatNum3 = 2.56789
intN1 = 1
intN2 = 2
intN3 = 0

# Perform calculation and display result 
floatNum2 = floatNum1 / floatNum3
print (format (floatNum2, '20.2f'))
floatNum2 = floatNum3/floatNum1
print (format (floatNum2, '20.2f'))
floatNum3 = intN1 // intN2
print ("", "\t", floatNum3)

# Ask user to input a number less than 1 or greater than 10 inclusively

userNum = float(input("Enter a number less than 1 or greater than 10 inclusively: "))
while (userNum<10 and userNum>1):
    print("!!!!! invalid range !!!!!")
    userNum = float(input("Enter a number less than 1 or greater than 10 inclusively: "))
........... 
    
def main():
    choice = menu("Good morning")
    if choice == 1:
        numExer()
    if choice ==2:
        validate()
    choice = menu("Good afternoon")
    
def main(greeting):
    print(greeting)
    print("Enter 1 for number exercise ")
    print("Enter 2 for valid number ")
    print("Enter 0 for quit ")
    choice = int(input("Your selection: "))
    while(choice<0 or choice>2):
        choice = int(input("Your selection: "))
    return choice
