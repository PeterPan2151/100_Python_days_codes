print("Welcome to the treasure island. \nYour mission is to find the treasure.")
print('You\'re at a cross road. ', end='')
choice = input('Where do you want to go? "left" or "right"').lower()

if choice == 'right':
    print("You fell of a cliff, game over!.")
elif choice == 'left':
    print("Yeah")
    print("You come to a lake. There is an island in the middle of the lake. ", end='')
    swim_or_wait = input(
        'Type "wait" to wait for a boat or type "swim" to swim across. ')
    if swim_or_wait == 'wait':
        print("You arrive ata the island unharmed. There is a house with 3 doors. On red, one yellow and one blue. ", end='')
        door = input("Which one do you choose? ").lower()
        if door == 'blue':
            print("Congratulations!! You found the treasure.")
        elif door == 'red':
            print("You entered a room full of fire, game over!")
        elif door == 'yellow':
            print("Behind this door was a hungry Lion, game over!")
        else:
            print("Invalid option.")
    elif swim_or_wait == 'swim':
        print("You were eaten by a shark, you should have waited, game over!")
    else:
        print("Invalid option.")
else:
    print("Invalid option.")
