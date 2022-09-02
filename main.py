import random

# Rock, Paper and scissors game
# rock ✊🏽 papaer 🤚🏽 scissors ✌🏽
game = ['rock', 'paper', 'scissors']
emojis = ['✊', '✋', '✌️']

computer_choice = random.randint(0, len(game) - 1)


user_choice = int(
    input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n'))

if user_choice > 2 or user_choice < 0:
    print(f'Please choose 0, 1 or 2 . try again!')

elif computer_choice == user_choice:
    print(
        f'You choose {emojis[user_choice]} and computer choose {emojis[computer_choice]}. It\'s a draw')

elif (computer_choice == 0 and user_choice == 2) or (computer_choice == 2 and user_choice == 1) or (computer_choice == 1 and user_choice == 0):
    print(
        f'You choose {emojis[user_choice]} and computer choose {emojis[computer_choice]}. Computer wins')
else:
    print(
        f'You choose {emojis[user_choice]} and computer choose {emojis[computer_choice]}. You win')
