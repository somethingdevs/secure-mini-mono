from utils.driver import dice_roll, moves_list
from models.player import Player
import database.Dao as databaseObj
import database.DaoConstants as DaoConst
from utils.loging import log


class monopoly_Instance:
    def __init__(self, roomID, player_list):
        self.counterPlayer = 0
        self.prevCounterPlayer = -1
        self.db = databaseObj.Dao()
        self.daoConst = DaoConst.DaoConstants()
        self.player_list = player_list
        self.is_game_over = False
        self.isRolled = False
        self.tiles = self.db.select_all_query(
            self.daoConst.GET_PROPERTY_LIST, True)
        self.logger = log()
        self.buy_options = None

    def special_cards(self, tile, player):
        if tile == 'Start/GO':
            player.add_balance(200)
            print('Collected $200!')

        elif tile == 'Visiting Jail':
            pass

        elif tile == 'Free Parking':
            pass

        elif tile == 'GO TO JAIL':
            player.go_to_jail()
            message = 'Sent to jail. Skipping two rounds...\n'
            self.db.insertion_query(
                self.daoConst.INSERT_LOG, (message, player.room_id))

        elif tile == 'Income Tax':
            player.reduce_balance(200)
            self.logger.log_info(
                'Income Tax of 200 has been deducted\n')
            print(
                'Income Tax of 200 has been deducted. Remove this print statement at the end')

    def game_winner(self):
        highest_balance = 0
        # add proper logic to get the sume of all property values(money) owned plus money and evaluate for each
        winner = None

        for player in self.player_list:
            if player.balance > highest_balance:
                highest_balance = player.balance
                winner = player
        # Write a dao stuff for updating winner for the room
        # something like update table room set winner = (subquery of the guy that won idk)
        return winner

    def player_buy_option(self):
        if self.buy_options is None:
            return
        [current_tile, player] = self.buy_options
        message = '\n'
        # message = 'Buy %s? [Y/N] - \n' % (
        #             current_tile.tile_name)
        self.db.insertion_query(
            self.daoConst.INSERT_LOG, (message, player.room_id))

        print("Name of the current tile is: ", current_tile.tile_name)
        message = "Name of the current tile is: %s\n" % current_tile.tile_name
        self.db.insertion_query(
            self.daoConst.INSERT_LOG, (message, player.room_id))

        if player.check_balance(current_tile):
            player.buy_tile(current_tile)
            self.db.insertion_query(self.daoConst.BUY_PROPERTY,
                                    (player.room_id, player.player_id, current_tile.tile_id))

            # insert message that says tile bought
            message = '%s bought for %s\n' % (current_tile.tile_name, current_tile.cost)
            self.db.insertion_query(
                self.daoConst.INSERT_LOG, (message, player.room_id))
        else:
            print("Insufficient Funds!!")
            message = 'Insufficient Funds!!\n'
            self.db.insertion_query(
                self.daoConst.INSERT_LOG, (message, player.room_id))

    def player_roll_dice(self, player):
        if self.isRolled:
            print('You have already rolled the dice')
            message = 'You have already rolled the dice\n'
            self.db.insertion_query(
                self.daoConst.INSERT_LOG, (message, player.room_id))
            return
        # if not rolled then, roll the dice
        dice_value = dice_roll(player)

        message = f'Rolled a {dice_value}'
        self.db.insertion_query(
            self.daoConst.INSERT_LOG, (message, player.room_id))

        player.player_moves(dice_value)
        current_tile = self.tiles[player.position]

        self.isRolled = True

        print(
            f'{player.username} landed on {current_tile.tile_name} - {current_tile.description}')

        message = '%s landed on %s - %s\n' % (
            player.username, current_tile.tile_name, current_tile.description)
        self.db.insertion_query(
            self.daoConst.INSERT_LOG, (message, player.room_id))
        message = '\n'
        self.db.insertion_query(
            self.daoConst.INSERT_LOG, (message, player.room_id))

        asset_owned = False  # assign this by

        # Execute to get the tile_owner
        tileInput = [current_tile.tile_id, player.room_id]
        # tileOWNERInput
        tileOWNERInput = self.db.select_query(
            self.daoConst.GET_PROPERTY_OWNER, tileInput)
        # print('This is tile owner',tileOWNERInput)
        tile_owner = None
        if tileOWNERInput:
            tile_owner = Player(room_id=tileOWNERInput[0][0], player_id=tileOWNERInput[0][1], username=tileOWNERInput[
                0][2], money=tileOWNERInput[0][3], position=tileOWNERInput[0][4], game_round=tileOWNERInput[0][5])

        if current_tile.cost != None:
            if tile_owner is None:
                print('The current tile owner is None')

                print(f"Buy {current_tile.tile_name}? [Y/N]")

                message = 'The current tile owner is None'
                self.db.insertion_query(self.daoConst.INSERT_LOG, (message, player.room_id))

                message = f"Buy {current_tile.tile_name}? [Y/N]"
                self.db.insertion_query(self.daoConst.INSERT_LOG, (message, player.room_id))

                # is_buy = input(
                #     f'Buy {current_tile.tile_name}? [Y/N]')
                # if is_buy.lower() == 'y':
                self.buy_options = [current_tile, player]
                # Nobody owns the tile, player can buy

            elif tile_owner.player_id != player.player_id:
                # Deduct from current player
                rent = player.charge_rent(current_tile)

                print(
                    f'{tile_owner.username} charges you {rent} as rent')
                message = '%s charges you %s as rent\n' % (
                    tile_owner.username, rent)
                self.db.insertion_query(
                    self.daoConst.INSERT_LOG, (message, player.room_id))

                # insert updated money in DB
                tile_owner.add_balance(rent)
                asset_owned = True  # create entry in player_property

            else:

                print('Player is on his own tile')
                message = 'Player is on his own tile\n'
                self.db.insertion_query(
                    self.daoConst.INSERT_LOG, (message, player.room_id))
                # asset_owned = True

        else:
            # print('SPECIAL CARD!!!' ,vars(current_tile))
            # Insert non-buyable logic special card
            self.special_cards(current_tile, player)

    def current_player_turn(self, game_input):
        if self.prevCounterPlayer != self.counterPlayer:
            return
        player = self.player_list[self.counterPlayer % len(self.player_list)]
        message = f'Enter your choice -'
        self.db.insertion_query(
            self.daoConst.INSERT_LOG, (message, player.room_id))
        message = f'{game_input}\n'
        print(game_input, type(game_input))
        self.db.insertion_query(
            self.daoConst.INSERT_LOG, (message, player.room_id))
        # Roll dice
        if game_input.casefold() == 'r':
            self.player_roll_dice(player)

        elif game_input.casefold() == 'h':
            # Insert house logic here
            current_tile = self.tiles[player.position]
            house_cost = current_tile.house_cost

            if player.balance > house_cost:
                player.build_house(current_tile)
                message = 'House built!\n'
                self.db.insertion_query(
                    self.daoConst.INSERT_LOG, (message, player.room_id))

            else:
                print('Insufficient Funds!')
                message = 'Insufficient Funds!\n'
                self.db.insertion_query(
                    self.daoConst.INSERT_LOG, (message, player.room_id))

        elif game_input.casefold() == 'f':
            # Insert hotel logic here
            current_tile = self.tiles[player.position]
            hotel_cost = current_tile.hotel_cost

            if player.balance > hotel_cost:
                player.build_hotel(current_tile)
                message = 'Hotel built!\n'
                self.db.insertion_query(
                    self.daoConst.INSERT_LOG, (message, player.room_id))
            else:
                print('Insufficient Funds!')
                message = 'Insufficient Funds!\n'
                self.db.insertion_query(
                    self.daoConst.INSERT_LOG, (message, player.room_id))

        elif game_input.casefold() == 'v':
            if not bool(player.assets_owned):
                print('No assets owned!')
                message = 'No assets owned!\n'
                self.db.insertion_query(
                    self.daoConst.INSERT_LOG, (message, player.room_id))

            else:
                print('----------Assets Owned----------')
                message = '----------Assets Owned----------\n'
                self.db.insertion_query(
                    self.daoConst.INSERT_LOG, (message, player.room_id))
                for assets in player.assets_owned:
                    print(f'{assets}')
                    message = '%s' % assets
                    self.db.insertion_query(
                        self.daoConst.INSERT_LOG, (message, player.room_id))
                message = '\n'
                self.db.insertion_query(
                    self.daoConst.INSERT_LOG, (message, player.room_id))
            print(end='\n\n')

        elif game_input.casefold() == 's':
            # Insert sell property logic here
            if player.assets_owned:
                [print(i, end=', ') for i in player.assets_owned]
                print(end='\n\n')
                sell_input = int(
                    input(f'Enter 0 - {len(player.assets_owned)}: ')) - 1
                message = f'{player.assets_owned[sell_input]}'
                selling_property_id = self.db.select_query(
                    self.daoConst.GET_PROPERTY_FROM_LIST, (message,))
                current_tile = self.tiles[selling_property_id[0][0]]
                sell_property = player.sell_tile(current_tile)
                self.db.insertion_query(
                    self.daoConst.SELL_PROPERTY, (player.room_id, player.player_id, sell_property))
                print(end='\n\n')

            else:
                print('No assets owned!')
                message = 'No assets owned!\n'
                self.db.insertion_query(
                    self.daoConst.INSERT_LOG, (message, player.room_id))

        elif game_input.casefold() == 'x':
            if self.isRolled:
                self.isRolled = False
                self.counterPlayer += 1
                self.buy_options = None
                print(f'{player.username}\'s turn ended!',
                      end='\n\n')
                message = '%s turn ended!\n' % player.username
                self.db.insertion_query(
                    self.daoConst.INSERT_LOG, (message, player.room_id))

            else:
                print("You need to first roll the dice!")
                message = 'You need to first roll the dice!\n'
                self.db.insertion_query(
                    self.daoConst.INSERT_LOG, (message, player.room_id))

        else:
            print('Error! Incorrect Input')
            message = 'Error! Incorrect Input\n'
            self.db.insertion_query(
                self.daoConst.INSERT_LOG, (message, player.room_id))

    def player_turn_start(self):
        self.prevCounterPlayer = self.counterPlayer
        player = self.player_list[self.counterPlayer % len(self.player_list)]
        # Displays player details
        message = f"{player.username}'s turn\n"
        self.logger.log_info(message)
        self.db.insertion_query(
            self.daoConst.INSERT_LOG, (message.replace("'", "''"), player.room_id))

        message = 'Cash - %s \t Rounds played - %s \t Player position - %s\n' % (
            player.balance, player.game_round, player.position)
        self.db.insertion_query(
            self.daoConst.INSERT_LOG, (message, player.room_id))
        message = '----------------------------------------------------------------'
        self.db.insertion_query(
            self.daoConst.INSERT_LOG, (message, player.room_id))

        print(
            f'Cash - {player.balance}\t Rounds played - {player.game_round}\t Player position - {player.position}')
        print('----------------------------------------------------------------')

        moves_list()
        print("Enter your choice: ")
        message = f'Enter your choice - \n'
        self.db.insertion_query(
            self.daoConst.INSERT_LOG, (message, player.room_id))
        # game_input = input('Enter your choice: ')

    # Displays game stats at the end
    # Need to display what name of the player, number of wins, number of losses and

    def game_end_player_details(self):
        for player in self.player_list:
            pass

    # Display logs of the game?

    # Check if 15 rounds are reached
    def game_over(self, player):
        if player.game_round == 15 or player.balance <= 0:
            print('Game Over!')
            # Insert some logic and DB query that makes room inactive and updates the winner of the room
            return True
        else:
            return False
