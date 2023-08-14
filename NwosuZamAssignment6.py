# Name: Zam Nwosu
# Input: The amount of integers and which number is the largest one
# Output: Whether that number is the highest or not
# Process: 1) Get the max numbers from user 2) Figure out the max value 3) Get which they think is the largest number 4) Print that it is correct or not 

def main():
    import random
    
    n = int(input("How many numbers to find max: "))
    while (n <1 or n >100):
        print("the number needs to be greater than 0 but less than 101")
        n = int(input("How many numbers to find max:"))
    f = open("numbers.txt", "w")
    randomlist = random.sample(range(1, 200), n)
    f.write(str(randomlist))
    f.close()
    file = open("numbers.txt", "r")
    content = file.read()
    print("Here's the list of numbers: ")
    print(content)
    
    largest = (max(randomlist))
    
    def GetGuess():
        guess = int(input("Guess the highest number from the list (or input 00 to quit): "))
        i = 0
        while i<100:
            if guess == largest:
                print("Congratulations! That's correct!")
                print("END")
                break
            if guess not in randomlist:
                if guess != 00:
                    print("This number is not from the list! Try again")
                    i+=1
                    guess = int(input("Guess the highest number from the list (or input 00 to quit): "))
            if guess in randomlist and guess != largest:
                if guess != 00:
                    print("This is not the correct number! Try again")
                    i+=1
                    guess = int(input("Guess the highest number from the list (or input 00 to quit): "))
            if guess == 00:
                print("END")
                break
                    
    GetGuess()
main()            