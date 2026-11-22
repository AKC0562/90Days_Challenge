import sys


bill = float(input("Enter the amount of the bill:"))

if bill <= 100:
    print("Please enter an relastic amount of bill.")
    sys.exit()
tip = float(input("Enter the percentage of tip:"))

if tip <= 1:
    print("Please enter an relastic amount of tip`s percentage.")
    sys.exit()
people = int(input("Enter the no. of people the bill to be split:"))

if bill <= 1:
    print("Please enter an relastic amount of people the bill is ging to split.")
    sys.exit()

Original_Bil = bill
bill_with_tip =  bill + (bill * tip / 100)
amount_per_people = bill_with_tip/people

print("Original bill amount: $", Original_Bil)
print("Bill amount with tip: $", bill_with_tip)
print("Amount to be paid per person: $", amount_per_people)