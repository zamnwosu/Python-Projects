# Name: Zam Nwosu
# Input: Number of years and rainfall each month entered by the user
# Output: Number of months, total number of rainfall, average monthly rainfall
# Process: 1) Get number of years from the user 2) Get rainfall from each month from user 3) Print their average rainfall and total rainfall

years = int(input("How many years do you want to track?: "))

months = 12

CompleteTotal = 0.0 

for years_rain in range(years):

    total= 0.0

    print("For year", years_rain + 1, ":")
    for month in range(months):
        rain = float(input("Enter rainfall amount for the month: "))
        total += rain

    CompleteTotal += total

number_months = years * months
average = CompleteTotal / number_months

print("For", number_months, "months:")
print("The total rainfall: ", format(CompleteTotal, ".2f"), "inches")
print("The average monthly rainfall: ", format(average, ".2f"), "inches")