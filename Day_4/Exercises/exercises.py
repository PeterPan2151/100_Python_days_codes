import random

# Exercise 1. Heads or Tails.
# number = random.randint(1, 2)
# if number == 1:
#     print("Heads")
# else:
#     print("Tails")

# Exercise 2. Bank Roulette.

# names_string = input("Enter name: ")
# names = names_string.split(", ")

# number = random.randint(0, len(names) - 1)
# print(f"{names[number]} is going to buy the meal today!")


# Exercise 3. Treasure Map.
line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Enter column first, then row, together: ")
letter = position[0].lower()
abc = ['a', 'b', 'c']
column = abc.index(letter)
row = int(position[1])
map[row - 1][column] = "X"

print(f"{line1}\n{line2}\n{line3}")
