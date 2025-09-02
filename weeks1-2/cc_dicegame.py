
import random

high_score = 0


def dice_game():

    global high_score

    while True:
        print("Current High Score: " + str(high_score))
        print("1) Roll Dice")
        print("2) Leave Game")
        start = input ("Enter your choice: ")
        print()
        if start == "2":
            print("Goodbye!")
            break
        elif start == "1":
            first_dice = random.randint(1, 6)
            second_dice = random.randint(1, 6)
            total = first_dice + second_dice
            if total > high_score:
                high_score = total
            print()
            print("You roll a...", str(first_dice), "\nYou roll a...", str(second_dice))
            print()
            print("You have rolled a total of", str(total))
            print()
        if total == high_score:
                print("New high score!")
print()
dice_game()