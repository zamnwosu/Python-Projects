# Programmer: Zam Nwosu
# Input: 1) Amount of numbers 2) The number file name 3) Users guess of highest number
# Process: 1) Important random numbers 2) Sort the numbers as a list 3) Find the highest number in the list
# Output: 1) Tell user if their guess is wrong or right 2) Ask user if they want to try again

def main():
    import random

    n = int(input("Total numbers: "))
    while (n <1 or n >100):
        print("numbers need to be between 0 and 100")
        n = int(input("Total numbers: "))
    p = open("numbers.txt", "w")
    randomlist = random.sample(range(1, 200), n)
    p.write(str(randomlist))
    p.close()
    file = open("numbers.txt", "r")
    content = file.read()
    print("The numbers listed are the following...: ")
    print(content)

    largest = (max(randomlist))

    def GetGuess():
        guess = int(input("Guess the highest number: "))
        i = 0
        while i<100:
            if guess == largest:
                print("You guessed right")
                print("done")
                break
            if guess not in randomlist:
                print("The guess is wrong")
                i+=1
                guess = int(input("Guess the highest number: "))
            if guess in randomlist and guess != largest and guess != "00":
                print("This is not the correct number! Try again")
                i+=1
                guess = int(input("Guess the highest number: "))
            if guess == 00:
                print("Done")
                break

    GetGuess()
main()
