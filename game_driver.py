import board
from board import display_moves, game_over, dice_roll
import player
import moves

# Statically instantiating three players
player1 = player.Player('Ali', 0, 0, 1500, ['Goa', 'Pondicherry', 'Rishikesh', 'Nainital', 'Gulmarg', 'Udaipur', 'Raipur', 'Darjeeling', 'Vijayawada', 'Waynad'], False, False)
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


while not is_game_over:
    for player in player_list:

        # Displays player details
        print(f'{player.username}\'s turn ')
        print(f'Cash - {player.balance}\t Rounds played - {player.game_round}\t Player position - {player.position}')
        print('----------------------------------------------------------------')

        display_moves()

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

                    if asset_owned == False and non_buyable == False:

                        is_buy = input(f'Buy {current_tile}? [Y/N]')

                        if is_buy.casefold() == 'y':
                            # Check for balance
                            if player.check_balance(current_tile):
                                player.buy_tile(current_tile)

                    if non_buyable == True:
                        # Insert non-buyable logic
                        moves.special_cards(current_tile, player)

            # Build a house
            elif game_input.casefold() == 'h':
                # Insert house logic here
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
                    print('----------Assets Owned----------')
                    for assets in player.assets_owned:
                        print(f'{assets}')
                print(end='\n\n')

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

            # Incorrect input
            else:
                print('Error! Incorrect Input')


        # Game over condition
        is_game_over = game_over(player)


# Displays game stats at the end
for player in player_list:
    player.display_player_details()
    print('------------------------')

# Insert winner logic

