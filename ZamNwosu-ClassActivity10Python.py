#Purpose: review basic concepts - data file, exception, functions, loops
#Programmer: Zam Nwosu

#input:
#1. total numbers to find max number (many)
#2. data file name
#3. guess
#output:
#1. max
#2. answer
#3. result/report
#process:
#1. get many
#2. get numbers 
#3. get data file name
#4. list numbers
#5. get guess
#6. find answer
#7. show result

#from random import seed
from random import random 
from random import randint

def main():
    #start your code here with the # but indent the function body
    
    #1. get many
    many = int(input("How many numbers to find max:"))
    while (many <1 or many >6):
        print("the number needs to be greater than 0 but less than 6")
        many = int(input("How many numbers to find max:"))
    
    #2. get numbers
    
    #play with the list
    numbers = [6,2,3,8,5]
    print(numbers)
    #print(numbers[0])
    
    print("Original list: ")
    index = 0
    while index < 5:
        print("item with index number:", index,"is", numbers[index])
        index+=1 
    
    #add many to the list
    numbers.append(many)
    print("New list: ")
    print(numbers)
    
    #one algorithm to find max from a list of numbers 
    largest = numbers[0]
    index = 1 
    while index < 5:
        if (numbers[index] > largest):
            largest = numbers[index]
        index +=1 
    print("The max is", largest)
    
    #alternative way
    print(max(numbers))
    
    #3. get data file name
    #dataFileName = input("Enter the file name for a data file:")
    
    #4. list numbers
    
    
    #5. get guess
    #------- task 2: create a function to get the user guess, validate the is within range--- 
    #getGuess()
    
    #6. find answer
    
    
    #7. show result
    
def getGuess():
    #get user's guess
    guess = int(input("Enter your guess of the largest number:"))
    while (guess <1 or guess >6):
        print("!!!The number needs to be greater than 0 but less than 6!!!")
        guess = int(input("Enter your guess:"))
        
#get random generator to generate a number
def GetRandInt():
    #seed(1)
    
    outFile = open("numbers.txt", 'w')
    for i in range(5):
        number = random()
        value = randint(0,100)
        ## save numbers to the data file ## 
        outFile.write(str(value))
        outFile.write('\n')
        print(number,' ',value)
    outFile.close()

#main()
GetRandInt()
