import board
import player
from player import player1, player2, player3

player_list = [player1, player2, player3]

is_game_over = False
messages = []

def display_moves(player):
    messages = []

    messages.append(f'{player.username}\'s turn ')
    messages.append(f'Cash - {player.balance}\t Rounds played - {player.game_round}\t Player position - {player.position}')
    messages.append('----------------------------------------------------------------')

    for key, value in board.moves.items():
        messages.append("{:<30}{}".format(key, value))
    messages.append('\n')
    return '\n'.join(messages)


def process_move(move: str) -> str:
    global is_game_over
    global messages

    while not is_game_over:
        for current_player in player_list:
            messages = []
            has_rolled = False

            if move.casefold() == 'r':
                if has_rolled:
                    messages.append('You have already rolled the dice')
                else:
                    has_rolled = True
                    messages.append(f"{current_player.username} chooses {move}!")

                    # Roll dice
                    roll_value = board.dice_roll(current_player)
                    current_player.player_moves(roll_value)
                    # messages.append(f'{player1.username} rolled {roll_value}')

                    current_tile = board.BOARD_TILES[current_player.position]

                    messages.append(f'{current_player.username} rolled {roll_value} and lands on {current_tile}')

            elif move.casefold() == 'h':

                current_tile = board.BOARD_TILES[player1.position]
                house_cost = board.BOARD_TILES_INFO[current_tile][4][1]

                if current_player.balance > house_cost:
                    current_player.build_house(current_tile)
                else:
                    messages.append('Insufficient Funds!')


            # Build a hotel
            elif move.casefold() == 'f':
                # Insert hotel logic here
                current_tile = board.BOARD_TILES[current_player.position]
                house_cost = board.BOARD_TILES_INFO[current_tile][4][1]

                if current_player.balance > house_cost:
                    current_player.build_house(current_tile)
                else:
                    messages.append('Insufficient Funds!\n\n')


            # View assets owned
            elif move.casefold() == 'v':
                if not bool(current_player.assets_owned):
                    messages.append('No assets owned!')

                else:
                    messages.append('----------Assets Owned----------')
                    for assets in current_player.assets_owned:
                        messages.append(f'{assets}')
                messages.append('\n\n')


            # Sell property
            elif move.casefold() == 's':
                # Insert sell property logic here
                if current_player.assets_owned:
                    [messages.append(i) for i in current_player.assets_owned]
                    messages.append('\n\n')
                    sell_property = int(input(f'Enter 0 - {len(player1.assets_owned) - 1}: '))
                    current_player.sell_tile(current_player.assets_owned[sell_property])
                    messages.append('\n\n')
                else:
                    messages.append('No assets owned!\n')

            # End turn
            elif move.casefold() == 'x':
                if has_rolled:
                    turn_ended = True
                    messages.append(f'{current_player.username}\'s turn ended!\n\n')

                else:
                    messages.append("You need to first roll the dice!\n\n")

            else:
                messages.append("You need to first roll the dice!\n\n")

        is_game_over = board.game_over(current_player)
    # Append the move chosen by the player
    return '\n'.join(messages)