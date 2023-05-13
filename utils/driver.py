import random
from models import player


def game_over(player):
    if player.game_round == 15 or player.balance <= 0:
        print('Game Over!')
        return True

    else:
        return False


def dice_roll(player):
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)
    total_dice = first_dice + second_dice
    return total_dice


def moves_list():
    # Display player stats(name, cash in hand, rounds played, position)
    print('-------------Moves-------------')

    print("{:<30}{}".format('Roll dice', 'r'))
    print("{:<30}{}".format('Build a house', 'h'))
    print("{:<30}{}".format('Build a hotel', 'f'))
    print("{:<30}{}".format('View assets owned', 'v'))
    print("{:<30}{}".format('Sell property', 's'))
    print("{:<30}{}".format('End turn', 'x'), end='\n\n\n')
