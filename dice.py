
import random

def roll_dice():
    print("Welcome to the game")

    input("Press enter to roll the dice......(1st person)")
    p1 = random.randint(1, 6)
    print(f"1st person rolled : {p1}")

    input("Press enter to roll the dice......(2nd person)")
    p2 = random.randint(1, 6)
    print(f"2nd person rolled : {p2}")

    if p1 > p2:
        return "1st person wins"
    elif p2 > p1:
        return "2nd person wins"
    else:
        return "It is a tie"


# Game loop
while True:
    result = roll_dice()
    print(result)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break