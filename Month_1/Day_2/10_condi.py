
# 1.Age group categorization.

age = int(input("Enter your age: "))
if age>=60:
    print("Hello senior saab!")
elif 13<=age<=19:
    print("Yoo! bro you are at your teenage.")
elif 20<= age <=59:
    print("Hello Sir/Ma`am how is your aduldhood going?")
else:
    print("Hey kido how is your day going?")


#2. Movie ticket pricing.
# for normal sinle at a time 
def ticket_price(age):
    if age<18:
        return 8
    else:
        return 12
# for multiple at a time
def total_ticket_fair(no_tickets):
    total = 0
    for ticket in range(1,no_tickets+1):
        age =  int(input((f"Enter age of {ticket} member: ")))
        if age<18:
            total += 8
        else:
            total += 12
    return total

def dis(t_p,day,no_person):
    if day.strip().lower() =="wednesday":
        return t_p -(no_person*2)
    else:
        return t_p


def main():
    day = input("Enter todays day(monday, tuesday, ....): ")
    no_of_tickets = int(input("Enter number of tickets you want to buy? "))

    print("The amount you have to pay is : $",(dis(total_ticket_fair(no_of_tickets),day,no_of_tickets)))

main()


#3. Grade calculator

marks = int(input("Enter your marks: "))


if marks<60:
    print("F")
elif 60<=marks<=69:
    print("D")
elif 70<=marks<=79:
    print("C")
elif 80 <= marks<=89 :
    print("B")
else:
    print("A")

#4. Fruit Ripeness checker. 

fruit_color = input("Enter the color of your fruit: ")

if fruit_color.lower() == "green":
    print("Unrip")
elif fruit_color.lower() == "yellow":
    print("Ripe")
else:
    print("Overripen")



#5. Weather Activity Suggestion.

weather = input("Enter your current weather state: ")

if weather.lower() == "summer":
    print("Go to a beach!")
elif weather.lower() == "rainy":
    print("Chai aur pakore")
elif weather.lower() == "autumn":
    print("Walk on the street")
elif weather.lower() == "winter":
    print("Go to a hill station")
elif weather.lower() == "spring":
    print("Time to grow plants.")
else:
    print("Enter a correct season.")

# 6. Transportation Mode Selection.

dist = int(input("Enter your distace to be covered: "))

if dist<3:
    print("Mode of transport: Walk")
elif dist >= 3:
    print("Mode of transport Bike(2 wheeler)")
elif dist> 15:
    print("Mode of transport is Car (4 wheeler)")
else:
  pass

#7. Coffee Customization. 

order = input("Enter your six=ze of coffee")

if order.lower()=="medium":
    print("You will get 1 extra short of espresso ")
elif order.lower()=="large":
    print("You will get 2 extra short of espresso ")
else:
    print("No extra espresso shorts")

#8. Password Strength Checker.

# Problem: Check if a password is "Weak", 
# "Medium", or "Strong". Criteria: < 6 chars (Weak),
#  6-10 chars (Medium), >10 chars (Strong).

#9. Leap Year Checker. 

#Problem: Determine if a year is a leap year. 
# (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

#10.Pet Food Recommendation. 

#Problem: Recommend a type of pet food based on the pet's species and age. 
# (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).