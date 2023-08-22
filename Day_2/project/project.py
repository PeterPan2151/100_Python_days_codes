print("Welcome to the tip calculator.")
total_bill = float(input("What was the total of the bill? "))
percentage = int(input("What percentage are you leaving? 10 12 or 15? "))
people = int(input("How many people are splitting the bill? "))

increase = total_bill * (percentage / 100)
total = total_bill + increase
pay_per_person = total / people

pay_per_person = "{:.2f}".format(pay_per_person)
print(f"Each person will pay {pay_per_person}")
