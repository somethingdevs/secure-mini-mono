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


# player_moves(player1, board.dice_roll())
# player_moves(player2, board.dice_roll())
# player_moves(player3, board.dice_roll())

