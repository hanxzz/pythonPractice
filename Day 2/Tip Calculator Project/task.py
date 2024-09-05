from typing import final

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tipAmount = tip/100*bill
totalBill = tipAmount+bill
finalBill= totalBill/people
finalAmount = round(finalBill,2)
print(finalAmount)


