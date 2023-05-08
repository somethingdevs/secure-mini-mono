from utils.driver import dice_roll, moves_list
from models.player import Player
import database.Dao as databaseObj
import database.DaoConstants as DaoConst
from utils.loging import log

class monopoly_Instance:
    def __init__(self, roomID, player_list):
        self.db = databaseObj.Dao()
        self.daoConst = DaoConst.DaoConstants()
        self.player_list = player_list
        self.is_game_over = False
        self.tiles = self.db.select_all_query(self.daoConst.GET_PROPERTY_LIST, True)
        self.logger = log()

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
            message = 'Sent to jail. Skipping two rounds...'
            self.db.insertion_query(self.daoConst.INSERT_LOG, (message, player.room_id))

        elif tile == 'Income Tax':
            player.reduce_balance(200)
            self.logger.log_info('Income Tax of 200 has been deducted. Remove this print statement at the end')
            print('Income Tax of 200 has been deducted. Remove this print statement at the end')


    def game_winner(self):
        highest_balance = 0
        winner = None       #add proper logic to get the sume of all property values(money) owned plus money and evaluate for each

        for player in self.player_list:
            if player.balance > highest_balance:
                highest_balance = player.balance
                winner = player
        #Write a dao stuff for updating winner for the room
        # something like update table room set winner = (subquery of the guy that won idk)
        return winner


    def game_start(self):
        #global is_game_over
       # print('This is playerLIst',self.player_list)
        while not self.is_game_over:
            correct_move= True
            turn_ended = False
            for player in self.player_list:

                # Displays player details
                message= "%s's turn" % player.username
                self.logger.log_info(message)
                self.db.insertion_query(self.daoConst.INSERT_LOG, (message.replace("'","''"), player.room_id))

                message = 'Cash - %s \t Rounds played - %s \t Player position - %s' % (player.balance, player.game_round, player.position)
                self.db.insertion_query(self.daoConst.INSERT_LOG, (message, player.room_id))

                print(f'Cash - {player.balance}\t Rounds played - {player.game_round}\t Player position - {player.position}')
                print('----------------------------------------------------------------')

                moves_list()

                turn_ended = False
                has_rolled = False

                # Move validation
                while not turn_ended:
                    game_input = input('Enter your choice: ') # insert in log and display.

                    message = 'Enter your choice - %s' % game_input
                    self.db.insertion_query(self.daoConst.INSERT_LOG, (message, player.room_id))

                   # game_input = await request.body()
                    # Roll dice
                    if game_input.casefold() == 'r':
                        if not has_rolled:
                            has_rolled = True
                            player.player_moves(dice_roll(player))
                            current_tile=self.tiles[player.position]

                            print(f'{player.username} landed on {current_tile.tile_name} - {current_tile.description}')

                            message = '%s landed on %s - %s' % (player.username, current_tile.tile_name, current_tile.description)
                            self.db.insertion_query(self.daoConst.INSERT_LOG, (message, player.room_id))

                            asset_owned = False # assign this by

                            #Execute to get the tile_owner
                            tileInput=[current_tile.tile_id,player.room_id]
                            #tileOWNERInput
                            tileOWNERInput=self.db.select_query( self.daoConst.GET_PROPERTY_OWNER,tileInput)
                            # print('This is tile owner',tileOWNERInput)
                            tile_owner=None
                            if tileOWNERInput:
                                tile_owner = Player(room_id=tileOWNERInput[0][0], player_id=tileOWNERInput[0][1], username=tileOWNERInput[0][2], money=tileOWNERInput[0][3], position=tileOWNERInput[0][4], game_round=tileOWNERInput[0][5])

                            if current_tile.cost != None:
                                if  tile_owner is None:
                                    print('The current tile owner is None')
                                    # Nobody owns the tile, player can buy
                                    is_buy = input(f'Buy {current_tile.tile_name}? [Y/N]')

                                    message = 'Buy %s? [Y/N] - %s' % (current_tile.tile_name, is_buy)
                                    self.db.insertion_query(self.daoConst.INSERT_LOG, (message, player.room_id))

                                    if is_buy.casefold() == 'y':
                                        # Check for balance
                                        if player.check_balance(current_tile):
                                            player.buy_tile(current_tile)
                                            self.db.insertion_query(self.daoConst.BUY_PROPERTY,
                                                                    (player.room_id, player.player_id, current_tile.tile_id))
                                            # insert message that says tile bought
                                            # message = '%s bought for %s' % (current_tile.tile_name,current_tile.cost)
                                        else:
                                            print("Insufficient Funds!!")
                                            message = 'Insufficient Funds!!'
                                            self.db.insertion_query(self.daoConst.INSERT_LOG, (message, player.room_id))

                                elif tile_owner.player_id != player.player_id:
                                    # Deduct from current player
                                    rent = player.charge_rent(player.position)

                                    print(f'{tile_owner.username} charges you {rent} as rent')
                                    message = '%s charges you %s as rent' % (tile_owner.username, rent)
                                    self.db.insertion_query(self.daoConst.INSERT_LOG, (message, player.room_id))

                                    tile_owner.add_balance(rent) # insert updated money in DB
                                    asset_owned = True # create entry in player_property
                                    break

                                else:

                                   print('Player is on his own tile')
                                   message = 'Player is on his own tile'
                                   self.db.insertion_query(self.daoConst.INSERT_LOG, (message, player.room_id))
                                    #asset_owned = True
                                   break

                            else:
                                # print('SPECIAL CARD!!!' ,vars(current_tile))
                                # Insert non-buyable logic special card
                                self.special_cards(current_tile, player)

                        else:
                            print('You have already rolled the dice')# insert in log and display.
                            message = 'You have already rolled the dice'
                            self.db.insertion_query(self.daoConst.INSERT_LOG, (message, player.room_id))
                            continue



                    # The house and hotel are designed in such a way that only if you step on the tile, you can build them
                    # Build a house
                    elif game_input.casefold() == 'h':
                        # Insert house logic here
                        current_tile = self.tiles[player.position]
                        house_cost = current_tile.house_cost

                        if player.balance > house_cost:
                            player.build_house(current_tile)
                            message = 'House built!'
                            self.db.insertion_query(self.daoConst.INSERT_LOG, (message, player.room_id))

                        else:
                            print('Insufficient Funds!')
                            message = 'Insufficient Funds!'
                            self.db.insertion_query(self.daoConst.INSERT_LOG, (message, player.room_id))

                    # Build a hotel
                    elif game_input.casefold() == 'f':
                        # Insert hotel logic here
                        current_tile = self.tiles[player.position]
                        hotel_cost = current_tile.hotel_cost

                        if player.balance > hotel_cost:
                            player.build_house(current_tile)
                            message = 'Hotel built!'
                            self.db.insertion_query(self.daoConst.INSERT_LOG, (message, player.room_id))
                        else:
                            print('Insufficient Funds!')
                            message = 'Insufficient Funds!'
                            self.db.insertion_query(self.daoConst.INSERT_LOG, (message, player.room_id))

                    # View assets owned
                    elif game_input.casefold() == 'v':
                        if not bool(player.assets_owned):
                            print('No assets owned!')
                            message = 'No assets owned!'
                            self.db.insertion_query(self.daoConst.INSERT_LOG, (message, player.room_id))

                        else:
                            print('----------Assets Owned----------')
                            message = '----------Assets Owned----------'
                            self.db.insertion_query(self.daoConst.INSERT_LOG, (message, player.room_id))
                            for assets in player.assets_owned:
                                print(f'{assets}')
                                message = '%s' % assets
                                self.db.insertion_query(self.daoConst.INSERT_LOG, (message, player.room_id))
                        print(end='\n\n')

                    # Sell property
                    elif game_input.casefold() == 's':
                        # Insert sell property logic here
                        if player.assets_owned:
                            [print(i, end=', ') for i in player.assets_owned]
                            print(end='\n\n')
                            sell_input = int(input(f'Enter 0 - {len(player.assets_owned)}: ')) - 1
                            message = '%s' % player.assets_owned[sell_input]
                            selling_property_id = self.db.select_query(self.daoConst.GET_PROPERTY_FROM_LIST, (message, ))
                            current_tile = self.tiles[selling_property_id[0][0]]
                            sell_property = player.sell_tile(current_tile)
                            self.db.insertion_query(self.daoConst.SELL_PROPERTY, (player.room_id, player.player_id, sell_property))
                            print(end='\n\n')

                        else:
                            print('No assets owned!')
                            message = 'No assets owned!'
                            self.db.insertion_query(self.daoConst.INSERT_LOG, (message, player.room_id))

                    # End turn
                    elif game_input.casefold() == 'x':
                        if has_rolled:
                            turn_ended = True
                            print(f'{player.username}\'s turn ended!', end='\n\n')
                            message = '%s turn ended!' % player.username
                            self.db.insertion_query(self.daoConst.INSERT_LOG, (message, player.room_id))

                        else:
                            print("You need to first roll the dice!")
                            message = 'You need to first roll the dice!'
                            self.db.insertion_query(self.daoConst.INSERT_LOG, (message, player.room_id))

                    # Incorrect input
                    else:
                        print('Error! Incorrect Input')
                        message = 'Error! Incorrect Input'
                        self.db.insertion_query(self.daoConst.INSERT_LOG, (message, player.room_id))


                # Update player details in the table at the end of every round
                self.db.insertion_query(self.daoConst.UPDATE_EVERYTHING, (player.balance, player.position, player.game_round, player.room_id, player.player_id))

                message = 'Round end! Player details updated'
                self.db.insertion_query(self.daoConst.INSERT_LOG, (message, player.room_id))


            # Game over condition
            self.is_game_over = self.game_over(player)
            if(self.is_game_over):
                self.game_winner(self)
                break


    # Displays game stats at the end
    # Need to display what name of the player, number of wins, number of losses and
    def game_end_player_details(self):
        for player in self.player_list:
            pass

    # Display logs of the game?

    #Check if 15 rounds are reached
    def game_over(self, player):
        if player.game_round == 15 or player.balance <= 0:
            print('Game Over!')
            # Insert some logic and DB query that makes room inactive and updates the winner of the room
            return True
        else:
            return False

