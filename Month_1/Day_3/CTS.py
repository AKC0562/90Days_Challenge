import re

text = input("Enter your camelCase text: ")

output = ""

for char in text:
    if char.isupper():
        output += "_"+char.lower()
    else:
        output+= char

print("Snake Case: ",output)