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





# # for i in range(1,11):
# #     print(5*i)

# '''import os

# # Get list of files/directories in the current working directory
# files = os.listdir()
# print(files)   '''



# a = int(input("Enter first number to be added: "))
# b = int(input("Enter the second number to be added: "))

# print(a+b)

# num = int(input("Enter the number to be divided by 2: "))


# print(int(num/2))
# print(num%2)

# num_1 = int(input("Enter nuber 1: "))
# num_2 = int(input("Enter nuber 2: "))

# result = (num_1 + num_2)/2

# print(result)


# import math

# num = int(input("Enter a number: "))

# square = math.pow(num, 2)

# print(square)

# name = "pappe"

# print(name[0:4:2])

# from datetime import date

# name = input("Enter your name")


# # print("Good Afternoon",name)

# print(f"Dear {name}, \n\nYou are Selected !! \n\n {date.today()}")

# s = input("Enter a string: ")
# count = s.count(" ")
# print(f"Number of spaces: {count}")   



# fruits = []
# for n in range(1,8):
#     fruits.append(input(f"Enter fruit {n}: "))


# print(fruits)

# marks = []

# for m in range(1,7):
#         marks.append(input(f"Enter marks of {m} subject: "))

# marks.sort()


# print(marks)

# tuple_1 = (1,2,3,4,5)

# tuple_1 = (3,4)

# # print(tuple_1)

# nums = []

# n = int(input("Enter the number of numbers to be added: "))

# for i in range(n):
#     nums.append(int(input(f"Enter the {i+1} number to be added: ")))

# total = sum(nums)

# print(total)

# a = (7,0,8,0,0,9)

# print(a.count(0))

# dict = {
#     "name" : "Pappe",
#     "age" : "12",
#     "channel":"not your type",
#     "state":"punjabi",
# }

# dict.update({"now doing":"controvercy"})

# print(dict)

# num = set()

# for i in range(1,9):
#     num.add(int(input("Enter a number: ")))


# print(num)


