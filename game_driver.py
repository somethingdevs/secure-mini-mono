import board
from utils.driver import game_over, dice_roll, moves_list
from models import player
import database.Dao

# Statically instantiating three players
# player1 = player.Player('Ali', 0, 0, 1500, ['Goa', 'Pondicherry', 'Rishikesh', 'Nainital', 'Gulmarg', 'Udaipur', 'Raipur', 'Darjeeling', 'Vijayawada', 'Waynad'], False, False)
# player2 = player.Player('Poorvi', 0, 0, 1500, [], False, False)
# player3 = player.Player('Deep', 0, 0, 1500, [], False, False)

# player_list = [player1, player2, player3]

get_players = database.db_connect
#
# board_query = 'select * from property_list'
# board = get_players.select_all_query(board_query)



players_query = 'select room_id, player_id from player where room_id = %s'
players_params = (1,)

usernames_query = 'SELECT u.username FROM user u JOIN player p ON u.user_id = p.player_id WHERE p.room_id = %s;'

player_list = []

usernames = get_players.select_query(usernames_query, players_params)
player_details = get_players.select_query(players_query, players_params)


# player_list is being populated,
for i in range(len(player_details)):
    player_list.append(player.Player(player_details[i][0], player_details[i][1], usernames[i][0]))


is_game_over = False
correct_move = True
turn_ended = False

def special_cards(tile, player):
    if tile == 'Start/GO':
        player.add_balance(200)
        print('Collected $200!')

    elif tile == 'Visiting Jail':
        pass

    elif tile == 'Free Parking':
        pass

    elif tile == 'GO TO JAIL':
        player.go_to_jail()

    elif tile == 'Income Tax':
        player.reduce_balance(200)
        print('Income Tax of 200 has been deducted. Remove this print statement at the end')


def game_winner(player_list):
    highest_balance = 0
    winner = None

    for player in player_list:
        if player.balance > highest_balance:
            highest_balance = player.balance
            winner = player

    return winner


def game_start():
    global is_game_over
    while not is_game_over:
        for player in player_list:

            # Displays player details
            print(f'{player.username}\'s turn ')
            print(f'Cash - {player.balance}\t Rounds played - {player.game_round}\t Player position - {player.position}')
            print('----------------------------------------------------------------')

            moves_list()

            turn_ended = False
            has_rolled = False

            # Move validation
            while not turn_ended:
                game_input = input('Enter your choice: ') # insert in log and display.

                # Roll dice
                if game_input.casefold() == 'r':
                    if has_rolled:
                        print('You have already rolled the dice')# insert in log and display.
                        continue
                    else:
                        has_rolled = True
                        player.player_moves(dice_roll(player)) #diceroll rolls 2 dices for a player and moves them

                        current_tile = board.BOARD_TILES[player.position]

                        # Checks if the item can be bought or not
                        non_buyable = True if (board.BOARD_TILES_INFO[current_tile][2] is None) else False

                        asset_owned = False
                        for tile_owner in player_list:

                            # The owner is the same player
                            if tile_owner == player:
                                asset_owned = True
                                break

                            # Add to owner
                            if current_tile in tile_owner.assets_owned:
                                # Deduct from current player
                                rent = player.charge_rent(player.position)
                                print(f'{tile_owner.username} charges you {rent} as rent')
                                tile_owner.add_balance(rent)
                                asset_owned = True

                        # Need to insert a special check for non-acquirable assets

                        print('IS asset owned:',asset_owned,'IS NON BUYABLE',non_buyable)
                        if  non_buyable == False:
                            if asset_owned == False:

                                is_buy = input(f'Buy {current_tile}? [Y/N]')

                                if is_buy.casefold() == 'y':
                                    # Check for balance
                                    if player.check_balance(current_tile):
                                        player.buy_tile(current_tile)

                        else :
                            # Insert non-buyable logic
                            special_cards(current_tile, player)

                # The house and hotel are designed in such a way that only if you step on the tile, you can build them
                # Build a house
                elif game_input.casefold() == 'h':
                    # Insert house logic here
                    current_tile = board.BOARD_TILES[player.position]
                    house_cost = board.BOARD_TILES_INFO[current_tile][4][1]

                    if player.balance > house_cost:
                        player.build_house(current_tile)
                    else:
                        print('Insufficient Funds!')

                # Build a hotel
                elif game_input.casefold() == 'f':
                    # Insert hotel logic here
                    current_tile = board.BOARD_TILES[player.position]
                    house_cost = board.BOARD_TILES_INFO[current_tile][4][1]

                    if player.balance > house_cost:
                        player.build_house(current_tile)
                    else:
                        print('Insufficient Funds!')

                # View assets owned
                elif game_input.casefold() == 'v':
                    if not bool(player.assets_owned):
                        print('No assets owned!')

                    else:
                        print('----------Assets Owned----------')
                        for assets in player.assets_owned:
                            print(f'{assets}')
                    print(end='\n\n')

                # Sell property
                elif game_input.casefold() == 's':
                    # Insert sell property logic here
                    if player.assets_owned:
                        [print(i, end=', ') for i in player.assets_owned]
                        print(end='\n\n')
                        sell_property = int(input(f'Enter 0 - {len(player.assets_owned)-1}: '))
                        player.sell_tile(player.assets_owned[sell_property])
                        print(end='\n\n')
                    else:
                        print('No assets owned!')
                # End turn
                elif game_input.casefold() == 'x':
                    if has_rolled:
                        turn_ended = True
                        print(f'{player.username}\'s turn ended!', end='\n\n')

                    else:
                        print("You need to first roll the dice!")

                # Incorrect input
                else:
                    print('Error! Incorrect Input')


            # Game over condition
            is_game_over = game_over(player)


game_start()

# Displays game stats at the end
for player in player_list:
    player.display_player_details()
    print('------------------------', end='\n')

# Insert winner logic


