from typing import List, Any
import board
import player
#
# Statically instantiating three players
# player1 = player.Player('Ali', 0, 0, 1500, [], False, False)
# player2 = player.Player('Poorvi', 0, 0, 1500, [], False, False)
# player3 = player.Player('Deep', 0, 0, 1500, [], False, False)
#
# player_list = [player1, player2, player3]


# player_moves(player1, board.dice_roll())
# player_moves(player2, board.dice_roll())
# player_moves(player3, board.dice_roll())

##def buy(player):
      #if player.assets_owned is None:
        #price= board.BOARD_TILES_INFO[board.BOARD_TILES[player.position]][2]
        #
        #1print(price)
        #if player.balance >= : 
                #player.money -= self.price
                #self.owner = player
                #print(f"{player.username} bought {self.name} for {self.price} dollars.")
        #else:
#               print(f"{player.name} does not have enough money to buy {self.name}.")
#else: 
#print(f"{self.name} is already owned by {self.owner.name}.")

# # Input validation
# def move_validation(move):
#     has_rolled = False
#
#     # Roll dice
#     if move.casefold() == 'r':
#         if has_rolled:
#             print('You have already rolled the dice')
#             return False
#         else:
#             has_rolled = True
#             return True
#         pass
#
#     # Build a house
#     elif move.casefold() == 'h':
#         # Insert house logic here
#         pass
#
#     # Build a hotel
#     elif move.casefold() == 'f':
#         # Insert hotel logic here
#         pass
#
#     # View assets owned
#     elif move.casefold() == 'v':
#         # Insert view assets logic here
#         pass
#
#     # Sell property
#     elif move.casefold() == 's':
#         # Insert sell property logic here
#         pass
#
#     # End turn
#     elif move.casefold() == 'x':
#         if has_rolled:
#             return True
#
#         else:
#             print("You need to first roll the dice!")
#             return False

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
