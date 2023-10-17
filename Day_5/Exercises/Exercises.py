# Exercise 1. Average height.
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# total_height = 0
# count_height = 0
# for height in student_heights:
#     total_height += height
#     count_height += 1
# average_height = total_height / count_height
# print(f"Total height = {total_height}")
# print(f"number of students = {count_height}")
# print(f"average height = {round(average_height)}")

# Exercise 2. High score.
# student_scores = input("Enter scores: ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])

# high_score = 0
# for score in student_scores:
#     if score > high_score:
#         high_score = score

# print(f"The highest score in the class is: {high_score}")

# Exercise 3. Adding even numbers.
# target = int(input("Enter number: "))
# sum = 0
# for n in range(1, target + 1):
#     if n % 2 == 0:
#         sum += n
# print(sum)
for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
