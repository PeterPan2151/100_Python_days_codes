import logo
import os
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    message = ""
    if direction == 'decode':
        shift *= -1
    for letter in text:
        if letter not in alphabet:
            message += letter
        else:

            letter_index = alphabet.index(letter)
            position = letter_index + shift
            message += alphabet[position]
    print(f"The {direction}d text is {message}")


print(logo.logo)
# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
game_on = True
while game_on:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26

    caesar(text, shift, direction)
    choice = input(
        "Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    if choice == 'no':
        print("Goodbye.")
        game_on = False
    else:
        os.system('cls')
