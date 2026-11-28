# 1. Counting positive numbers

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positve_no_count = 0

for num in numbers:
    if num>0:
        positve_no_count+= 1
print("Number of positve number in given list are:",positve_no_count)

#2. Sum of Even Numbers

n = int(input("Enter the value of n: "))

sum_of_n_even = 0

for i in range(1,n+1):
    if i%2 == 0:
        sum_of_n_even+= i
print("Sum of n even number is: ",sum_of_n_even)

#3. Multiplication Table printer

num = int(input("Enter the number for multipication tsble: "))

for i in range(1,11):
    if i==5:
        continue
    print(f"{num}x{i}={num*i}")
    
#4. Revise a string

string= input("Enter a word: ")
reversed_string = ""

for char in string:
    reversed_string = char + reversed_string

print(reversed_string)

#5. FInd the first non-repeating char

input_str = input("Enter a word: ")

for char in input_str:
    if input_str.count(char) ==1:
        print("Answer:",char)
        break

#6 Factorial calculator 

num = int(input("Enter a number for factorial: "))
factorial= 1

while num > 0:
    factorial = factorial *num
    num-=1
print(f"Factorial of given number is: {factorial}")

#7. Validate number

while True:
    number = int(input("Enter value b/w 1 and 10: "))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Invalid number, try again")

#8. Prime number checker

num = int(input("Enter a number: "))

isprime = True

if num > 1:
    for i in range(2, num):
        if (num%i)==0:
            print("Enter  number is not prime.")
            break
        print("Enter number is prime")

#9. List Uniqueness checker

items = ["Iron Man", "Captain America", "Hulk","Thor","Black Widow","Hawkeye","Iron Man", "Captain America"]
unique_tem = set()

for item in items:
    if item in unique_tem:
        print("Duplicate: ",item)
        break
    unique_tem.add(item)

#10. Exponenrial Backoff

import time

wait_time = 1
max_retries= 5
attempt=0

while attempt<max_retries:
    print(f"Attemt{attempt+1}-wait time {wait_time}")
    time.sleep(wait_time)
    wait_time*=2
    attempt+=1