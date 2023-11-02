import os
from logo import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number? "))
    calc_on = True
    while calc_on:
        for op in operations:
            print(op)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number? "))
        function_choose = operations[operation_symbol]
        answer = function_choose(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_choice = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation\nor type 'exit' to exit the program: ")

        if continue_choice == 'y':
            num1 = answer
            os.system('cls')
        elif continue_choice == 'n':
            calc_on = False
            calculator()
        elif continue_choice == 'exit':
            break


calculator()
print("Thank you.")
