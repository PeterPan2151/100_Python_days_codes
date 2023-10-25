# Exercise 1. Grading Program.
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }

# student_grades = {}
# for student in student_scores:
#     score = student_scores[student]
#     if 91 <= score <= 100:
#         student_grades[student] = "Outstanding"
#     elif 81 <= score <= 90:
#         student_grades[student] = "Exceeds Expectations"
#     elif 71 <= score <= 80:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"

# print(student_grades)


# Exercise 2. Travel Log.


travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country, visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities
    travel_log.append(new_country)


country = input()  # Add country name
visits = int(input())  # Number of visits
list_of_cities = eval(input())  # create list from formatted string
add_new_country(country, visits, list_of_cities)
print(
    f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
