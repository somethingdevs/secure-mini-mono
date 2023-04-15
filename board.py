import random


def dice_roll():
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)
    total_dice = first_dice + second_dice
    if first_dice == second_dice:
        print(f'x rolled doubles of {first_dice}!') # Change player name
    print(f'x rolled {total_dice}') # Change player name
    return total_dice


