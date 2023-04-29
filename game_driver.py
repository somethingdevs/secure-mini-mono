import board
from board import display_moves, game_over, dice_roll
import moves
import player

# Statically instantiating three players
player1 = player.Player('Ali', 0, 0, 1500, ['Goa'], False, False)
player2 = player.Player('Poorvi', 0, 0, 1500, [], False, False)
player3 = player.Player('Deep', 0, 0, 1500, [], False, False)

player_list = [player1, player2, player3]

is_game_over = False
correct_move = True
turn_ended = False

# display moves
# accept input
# depending upon input do something - for now roll the dice
# move forward
# go until rounds are 15. and then stop

# Input validation
def move_validation(move):
    has_rolled = False

    # Roll dice
    if move.casefold() == 'r':
        if has_rolled:
            print('You have already rolled the dice')
            return False
        else:
            has_rolled = True
            return True
        pass

    # Build a house
    elif move.casefold() == 'h':
        # Insert house logic here
        pass

    # Build a hotel
    elif move.casefold() == 'f':
        # Insert hotel logic here
        pass

    # View assets owned
    elif move.casefold() == 'v':
        # Insert view assets logic here
        pass

    # Sell property
    elif move.casefold() == 's':
        # Insert sell property logic here
        pass

    # End turn
    elif move.casefold() == 'x':
        if has_rolled:
            return True

        else:
            print("You need to first roll the dice!")
            return False


display_moves()
while not is_game_over:
    for player in player_list:

        # Displays player details
        print(f'{player.username}\'s turn ')
        print(f'Cash - {player.balance}\t Rounds played - {player.game_round}\t Player position - {player.position}')
        print('----------------------------------------------------------------')

        turn_ended = False
        has_rolled = False

        # Move validation
        while not turn_ended:
            game_input = input('Enter your choice: ')

            # Roll dice
            if game_input.casefold() == 'r':
                if has_rolled:
                    print('You have already rolled the dice')
                    continue
                else:
                    has_rolled = True
                    player.player_moves(dice_roll(player))

            # Build a house
            elif game_input.casefold() == 'h':
                # Insert house logic here
                player.balance = player.balance - board.BOARD_TILES_INFO[board.BOARD_TILES[player.position]]
                pass

            # Build a hotel
            elif game_input.casefold() == 'f':
                # Insert hotel logic here
                pass

            # View assets owned
            elif game_input.casefold() == 'v':

                if not bool(player.assets_owned):
                    print('No assets owned!')

                else:
                    for assets in player.assets_owned:
                        print('----------Assets Owned----------')
                        print(f'{assets}')

            # Sell property
            elif game_input.casefold() == 's':
                # Insert sell property logic here
                pass

            # End turn
            elif game_input.casefold() == 'x':
                if has_rolled:
                    turn_ended = True
                    print(f'{player.username}\'s turn ended!', end='\n\n')

                else:
                    print("You need to first roll the dice!")

            else:
                print('Error! Incorrect Input')

        # Game over condition
        is_game_over = game_over(player)


for player in player_list:
    player.display_player_details()



