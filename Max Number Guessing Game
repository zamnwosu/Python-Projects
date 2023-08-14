# Programmer: Zam Nwosu
# Input: 1) Amount of numbers 2) The number file name 3) Users guess of highest number
# Process: 1) The numbers as a list 2) Find the highest number in the list
# Output: 1) Tell user if their guess is wrong or right 2) Ask user if they want to try again
'''

input

1. find numbers

2.data file name

3.guess

output

1.max

2.answer

3.result

'''


def main():
    
    while True:
        
        numOfNumbers = int(input("Enter number of numbers: "))
        
        if numOfNumbers <= 100:
            
            break
        
        else:
            
            print("The number must be less than or equal to 100.")
    
    printlist(numOfNumbers)
    


def printlist(numOfNumbers):
    
    filename = input("Enter the name of your number file: ")
    
    file = open(filename, "r")
    
    

    print("\nNumbers")
    
    print("-------")
    
    

    nums = []
    
    

    num = file.readline()
    
    while len(nums) < numOfNumbers:
        
        num = num.strip("\n")
        
        num = int(num)
        
        nums.append(num)
        
        print(num)
        
        num = file.readline()
        
    
   
    guess(nums)



def guess(lst):
    
    while True:
        
        guess = int(input("Guess the highest number: "))
        
        if guess <= 100:
            
            test(guess, lst)
            
            break
        
        else:
            
            print("The number must be less than or equal to 100.")  



def test(number, lst):
    
    if number == max(lst):
        
        print("congratulations! You guessed correctly.")
    
    else:
        
        print("Try again.")
        
        guess(lst)

    

    cont = input("Enter 'continue' to continue or 'quit' to quit: ")
    
    if cont.lower() == "continue":
        
       print()
        
       main()
    
    else:
        
        None



main()
