import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
print("Let'splay some Rock Paper Scissors")
player_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer_choice = random.randint(0, 2)


if player_choice > 2 or player_choice < 0:
    print("Invalid option, please try again.")
else:
    moves = [rock, paper, scissors]
    print(f"Player choose: \n {moves[player_choice]}")
    print("VS")
    print(f"{moves[computer_choice]}")
    if player_choice == computer_choice:
        print("It's a Tie!")
    elif player_choice == 0 and computer_choice == 2:
        print("You win!")
    elif player_choice == 2 and computer_choice == 0:
        print("You loose!")
    elif player_choice > computer_choice:
        print("You win!")
    elif player_choice < computer_choice:
        print("You loose!")
