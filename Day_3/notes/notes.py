print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if 45 <= age <= 55:
        print("Have a free ride.")
        bill += 0
    elif age > 18:
        bill += 12
        print("Adult tickets are $12")
    elif 12 <= age <= 18:
        bill += 7
        print("Youth tickets are $7")
    else:
        bill += 5
        print("Children tickets are $5")

    photo = input("Dou you want a photo taken? Yes or no? ").lower()
    if photo == 'yes':
        bill += 3
    print(f"The total bill is ${bill}")
else:
    print("Sorry, you can't ride.")
