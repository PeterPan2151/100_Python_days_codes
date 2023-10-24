import math
# Exercise 1. Coverage of a wall.
# def paint_calc(height, width, cover):
#     number_cans = (height * width) / 5
#     print(f"You'll need {math.ceil(number_cans)} cans of paint.")


# test_h = int(input())  # Height of wall (m)
# test_w = int(input())  # Width of wall (m)
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# Exercise 2. CHeck if number is prime number.
def prime_checker(number):
    prime_number = True
    for n in range(2, number):
        if number % n == 0:
            prime_number = False

    if prime_number:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input())  # Check this number
prime_checker(number=n)
