# Programmer: Zam Nwosu
# Input: Three numbers for the number of seat tickets for each class that were sold 
# Process: 1) Calculate the income for each of the three classes 2) Calculate the total income of the three classes combined
# Output: 1) Income for each class 2) Total income

Aseat = 0
Bseat = 0
Cseat = 0
a_income = 0
b_income = 0
c_income = 0
total = 0

def ask_seat_numbers():
    global Aseat
    Aseat = int(input("Enter count of A seats: "))
    while Aseat < 0:
        Aseat = int(input("Invalid input! Please enter a positive integer for Class A: "))
    global Bseat
    Bseat = int(input("Enter count of B seats: "))
    while Bseat < 0:
        Bseat = int(input("Invalid input! Please enter a positive integer for Class B: "))
    global Cseat
    Cseat = int(input("Enter count of C seats: "))
    while Cseat < 0:
        Cseat = int(input("Invalid input! Please enter a positive integer for Class C: "))
    calculate_income()
    total_income()
    
def calculate_income():
    global a_income
    a_income = (Aseat*20)
    global b_income
    b_income = (Bseat*15)
    global c_income
    c_income = (Cseat*10)
    print("Income from Class A seats: $", format(a_income, ',.2f'), sep='')
    print("Income from Class B seats: $", format(b_income, ',.2f'), sep='')
    print("Income from Class C seats: $", format(c_income, ',.2f'), sep='')
    
def total_income():
    total = (a_income + b_income + c_income)
    print("Total income: $", format(total, ',.2f'), sep='')
    
ask_seat_numbers()