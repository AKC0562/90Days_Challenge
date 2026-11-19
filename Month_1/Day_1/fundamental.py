#This is the code with error
# x = "global_x"

# def make_workers():
#     workers = []
#     for i in range(3):
#         def worker():
#             return (x, i)
#         workers.append(worker)
#     return workers

# def broken_reader():
#     print(x)
#     if False:
#         x = "local_x"

# w0, w1, w2 = make_workers()
# print(w0(), w1(), w2())
# broken_reader()




# This is with correction

# x = "global_x"  # Module-level variable.

# def make_workers():
#     workers = []  # Store the worker functions.
#     for i in range(3):
#         def worker(i=i):  # Capture a separate i value for every worker.
#             return (x, i)  # Return the global x and the captured i.
#         workers.append(worker)  # Add the function to the list.
#     return workers  # Return the three worker functions.

# def broken_reader():
#     print(x)  # With no local assignment, this correctly reads global x.

# w0, w1, w2 = make_workers()
# print(w0(), w1(), w2())  # Output: ('global_x', 0) ('global_x', 1) ('global_x', 2)
# broken_reader()  # Output: global_x


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