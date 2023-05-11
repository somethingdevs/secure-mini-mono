import random
from models import player
import database.Dao

# players_query = 'select room_id, player_id from player where room_id = %s'
# players_params = (1,)
#
# usernames_query = 'SELECT u.username FROM user u JOIN player p ON u.user_id = p.player_id WHERE p.room_id = %s;'
#
# player_list = []
# get_players = database.db_connect
# usernames = get_players.select_query(usernames_query, players_params)
# value = get_players.select_query(players_query, players_params)
#
#
# # player_list is being populated,
# for i in range(len(value)):
#     player_list.append(player.Player(value[i][0], value[i][1], usernames[i][0]))


# In case wanna know if the players are working or not, go ahead and uncomment this
# for j in player_list:
#     j.display_player_details()
#     print('Room id - ', j.room_id)
#     print('Player id - ', j.player_id, end='\n\n')

is_game_over = False
# messages = []


# def display_moves(current_player):
#     # messages = []
#
#     print(f'{current_player.username}\'s turn ')
#     print(f'Cash - {current_player.balance}\t Rounds played - {current_player.game_round}\t Player position - {current_player.position}')
#     print('----------------------------------------------------------------')
#
#     for key, value in board.moves.items():
#         print("{:<30}{}".format(key, value))
#     print('\n')
#     return '\n'.join(messages)


# def process_move(move: str) -> str:
#     global is_game_over
#     global messages
#
#     while not is_game_over:
#         for current_player in player_list:
#             messages = []
#             has_rolled = False
#
#             if move.casefold() == 'r':
#                 if has_rolled:
#                     print('You have already rolled the dice')
#                 else:
#                     has_rolled = True
#                     print(f"{current_player.username} chooses {move}!")
#
#                     # Roll dice
#                     roll_value = dice_roll(current_player)
#                     current_player.player_moves(roll_value)
#                     # print(f'{player1.username} rolled {roll_value}')
#
#                     current_tile = board.BOARD_TILES[current_player.position]
#
#                     print(f'{current_player.username} rolled {roll_value} and lands on {current_tile}')
#
#             elif move.casefold() == 'h':
#
#                 current_tile = board.BOARD_TILES[player1.position]
#                 house_cost = board.BOARD_TILES_INFO[current_tile][4][1]
#
#                 if current_player.balance > house_cost:
#                     current_player.build_house(current_tile)
#                 else:
#                     print('Insufficient Funds!')
#
#
#             # Build a hotel
#             elif move.casefold() == 'f':
#                 # Insert hotel logic here
#                 current_tile = board.BOARD_TILES[current_player.position]
#                 house_cost = board.BOARD_TILES_INFO[current_tile][4][1]
#
#                 if current_player.balance > house_cost:
#                     current_player.build_house(current_tile)
#                 else:
#                     print('Insufficient Funds!\n\n')
#
#
#             # View assets owned
#             elif move.casefold() == 'v':
#                 if not bool(current_player.assets_owned):
#                     print('No assets owned!')
#
#                 else:
#                     print('----------Assets Owned----------')
#                     for assets in current_player.assets_owned:
#                         print(f'{assets}')
#                 print('\n\n')
#
#
#             # Sell property
#             elif move.casefold() == 's':
#                 # Insert sell property logic here
#                 if current_player.assets_owned:
#                     [print(i) for i in current_player.assets_owned]
#                     print('\n\n')
#                     sell_property = int(input(f'Enter 0 - {len(player1.assets_owned) - 1}: '))
#                     current_player.sell_tile(current_player.assets_owned[sell_property])
#                     print('\n\n')
#                 else:
#                     print('No assets owned!\n')
#
#             # End turn
#             elif move.casefold() == 'x':
#                 if has_rolled:
#                     turn_ended = True
#                     print(f'{current_player.username}\'s turn ended!\n\n')
#
#                 else:
#                     print("You need to first roll the dice!\n\n")
#
#             else:
#                 print("You need to first roll the dice!\n\n")
#
#         is_game_over = board.game_over(current_player)
#     # Append the move chosen by the player
#     return '\n'.join(messages)


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
    # if first_dice == second_dice:
        # print(f'{player.username} rolled doubles of {first_dice}!')  # Change player name
    # print(f'{player.username} rolled {total_dice}', end='\n\n')  # Change player name
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

def get_moves():
    pass
