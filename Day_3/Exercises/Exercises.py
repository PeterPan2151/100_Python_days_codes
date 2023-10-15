# Exercise 1. Check if a number is odd or even
# number = int(input("Give me a number: "))
# if number % 2 == 0:
#     print("It is Even.")
# else:
#     print("It is Odd.")


# Exercise 2. BMI v2-0
# height = float(input("Enter your height in m: "))
# weight = int(input("Enter your weight in kg: "))
# bmi = weight / height ** 2

# if 0 < bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif 18.5 <= bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif 25 <= bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif 30 <= bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")


# Exercise 3.Check if a year is leap.
# year = int(input("Give me a year to check: "))
# if year % 4 == 0:
#     # Yes
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not leap Year")

#     else:
#         print("Leap year")
# else:
#     print("Not leap year")


# Exercise 4. Pizzeria
# print("Thank you for choosing Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L? ").lower()
# add_pepperoni = input("Do you want pepperoni? Y or N? ").lower()
# extra_cheese = input("Do you want extra cheese? Y or N? ").lower()
# bill = 0

# if size == 's':
#     bill += 15
# elif size == 'm':
#     bill += 20
# elif size == 'l':
#     bill += 25
# else:
#     print("Not a valid option.")

# if add_pepperoni == 'y':
#     if size == 's':
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == 'y':
#     bill += 1

# print(f"Your final bill is: ${bill}.")

# Exercise 5. Love Calculator
print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()

full_name = name1 + name2
t = full_name.count('t')
r = full_name.count('r')
u = full_name.count('u')
e = full_name.count('e')

l = full_name.count('l')
o = full_name.count('o')
v = full_name.count('v')

digit_one = t + r + u + e
digit_two = l + o + v + e

total = int(str(digit_one) + str(digit_two))

if 10 > total or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif 40 < total < 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
