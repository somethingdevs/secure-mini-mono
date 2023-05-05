import board
from board import display_moves, dice_roll
#from utils.driver import game_over
from models.player import Player 
import database.Dao as databaseObj
import database.DaoConstants as DaoConst


class monopoly_Instance:
    def __init__(self,roomID,player_list):
        self.db=databaseObj.Dao()
        self.daoConst=DaoConst.DaoConstants()
        self.player_list=player_list
        print( self.player_list[0].printPlayer())
        self.is_game_over= False
        self.tiles= self.db.select_all_query( self.daoConst.GET_PROPERTY_LIST,True)

    def special_cards(self,tile, player):
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


    def game_winner(self):
        highest_balance = 0
        winner = None       #add proper logic to get the sume of all property values(money) owned plus money and evaluate for each

        for player in self.player_list:
            if player.balance > highest_balance:
                highest_balance = player.balance
                winner = player
        #Write a dao stuff for updating winner for the room
        return winner


    def game_start(self):
        #global is_game_over
       # print('This is playerLIst',self.player_list)
        while not self.is_game_over:
            correct_move= True
            turn_ended = False
            for player in self.player_list:

                # Displays player details
                print(f'{player.username}\'s turn ')
                print(f'Cash - {player.balance}\t Rounds played - {player.game_round}\t Player position - {player.position}')
                print('----------------------------------------------------------------')

                display_moves()

                turn_ended = False
                has_rolled = False

                # Move validation
                while not turn_ended:
                    game_input = input('Enter your choice: ') # insert in log and display.

                    # Roll dice
                    if game_input.casefold() == 'r':
                        if not has_rolled:
                            has_rolled = True
                            player.player_moves(dice_roll(player)) #diceroll rolls 2 dices for a player and moves them

                            current_tile=self.tiles[player.position]
                    
                            asset_owned = False # assign this by

                            #Execute to get the tile_owner
                            tileInput=[current_tile.tile_id,player.room_id]
                            #tileInput
                            tileOWNERInput=self.db.select_query( self.daoConst.GET_PROPERTY_OWNER,tileInput)
                            print(tileOWNERInput)
                            tile_owner=Player(room_id=tileOWNERInput[0], player_id= tileOWNERInput[1],username= tileOWNERInput[2], money=tileOWNERInput[3],position =tileOWNERInput[4],game_round= tileOWNERInput[5])
                             
                            
                            #The owner is the same player, write query to get owner of current tile
                            print('PLAYER_TILE OWNER' , type(tile_owner))
                            print('Player type is:',type(player))


                            if  current_tile.cost != None :
                                if  tile_owner is None:
                                    print('The current tile owner is None')
                                    #BUYs LOGIC
                                    is_buy = input(f'Buy {current_tile}? [Y/N]')

                                    if is_buy.casefold() == 'y':
                                        # Check for balance
                                        if player.check_balance(current_tile):
                                            player.buy_tile(current_tile)
                                        else:
                                            print("insufficient Funds !!")

                                elif tile_owner.player_id != player.player_id:
                                    print('The current tile cost is: ',tile_owner.player_id )
                                    # Deduct from current player
                                    rent = player.charge_rent(player.position) 
                                    print(f'{tile_owner.username} charges you {rent} as rent')
                                    tile_owner.add_balance(rent)# insert updated money in DB
                                    asset_owned = True # create entry in player_property
                                    break     

                                else:
                                   
                                   print('Player is on his own tile')
                                    #asset_owned = True
                                   break  
                            else :
                                print('SPECIAL CARD!!!' ,vars(current_tile))
                                # Insert non-buyable logic special card
                                self.special_cards(current_tile, player)

                        else:
                            print('You have already rolled the dice')# insert in log and display.
                            continue

                        

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
            self.is_game_over = self.game_over(player)
            if(self.is_game_over):
                self.game_winner(self)
                break


    # Displays game stats at the end
    def getGameStats(self): 
        for player in self.player_list:
            player.display_player_details()
            print('------------------------', end='\n')

    #Check if 15 rounds are reached
    def game_over(self,player):
        if player.game_round == 15 or player.balance <= 0:
            print('Game Over!')
            return True

        else:
            return False
