from typing import List, Any
import board
import property

# Statically instantiating three players
player1 = property.Player('Ali', 0, 0, 1500, [], False, False)
player2 = property.Player('Poorvi', 0, 0, 1500, [], False, False)
player3 = property.Player('Deep', 0, 0, 1500, [], False, False)

player_list = [player1, player2, player3]

def player_moves(player, dice_value):
        player.position += dice_value
        if player.position > 31:
                player.position = player.position % 31
                player.game_round += 1
        # print(player.position)
        print(f'You are now at {board.BOARD_TILES[player.position]}')
        print(f'{ board.BOARD_TILES[player.position]} Details {board.BOARD_TILES_INFO[board.BOARD_TILES[player.position]]}', end='\n\n\n')
        #owned = board.BOARD_TILES_INFO[board.BOARD_TILES[player.position]][7]
        #if owned == "False" :
         #       price= board.BOARD_TILES_INFO[board.BOARD_TILES[player.position]][2]
          #      if player.balance >= price:
           #             player.balance -= price
            #            player.assets_owned.append(board.BOARD_TILES[player.position])
             #           board.BOARD_TILES_INFO['owned'] = True
              #          print(f"{player.username} bought {board.BOARD_TILES[player.position]} for {price} rupees.")
               # else:
                #        print(f"{player.username} has insufficient funds.")
        #else: 
         #       print(f"{board.BOARD_TILES[player.position]} is already owned")
        


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
