# Program to demonstrate use of functions, data files and try..except
# Programmer: Zam Nwosu
# Input: Username, menu choice, 2 numbers 
# Output: Result of operations
# Process: Operations - Addition, Subtraction, Multiplication, Division

#1. show greeting
#2. get user name
#3. show menu
#4. get user menu choice
#5. perform operation based on user menu choice
#6. display result


def getTwoNumbers():
    num1=float(input("Enter a number: "))
    while (num1==0):
        print("No zero please!")
        num1=float(input("Enter a number: "))
        
    num2=float(input("Enter a number: "))
    return num1,num2

def showMenu(userName):
    print (userName, ", what would you like to try?")
    print ("1. Addition")
    print ("2. Subtraction")
    print ("3. Multiplication")
    print ("4. Division")
    print ("0. EXIT")
  
def main():
    result=0
    num1=0
    num2=0
    choice=-1
    
    #1 show greeting
    print ("Good day! Let's have some fun together...")
    
    #2 get user name
    userName = input("What is your name: ")
    
    while (choice !=0):
        #3 show menu
        showMenu(userName)
        
        #4 get user menu choice
        choice = int(input("Your choice (1, 2, 3, 4 or 0): "))
        
        #5 perform operation based on user choice
        
        try:
            if (choice == 1):
                num1 = float(input("Enter a number: "))
                num2 = float (input("Enter another number: "))
                result = num1+num2
                
            elif (choice == 2):
                num1 = float(input("Enter a number: "))
                num2 = float (input("Enter another number: "))
                result = num1-num2
            elif (choice == 3):
                num1 = float(input("Enter a number: "))
                num2 = float (input("Enter another number: "))
                result = num1*num2
            elif (choice == 4):
                num1 = float(input("Enter a number: "))
                num2 = float (input("Enter another number: "))
                result = num1/num2
            else:
                print("Bye!")
        
        except ValueError:
            print("Value Error in process.")
        except:
            print("Error encountered when processing...")
        
        #6. display result
        if (choice !=0):
            print ("The Result is ", result)
            outFile=open("result.txt", 'w')
            outFile.write("The Result is ")
            outFile.write(str(result))
            
main()