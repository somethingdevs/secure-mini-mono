from typing import List, Any
import board

import board


def property_cards():
    pass


class Player:
    def __init__(self, username, position: int, balance: int, assets_owned: List[Any], is_jail: bool, is_bankrupt: bool):
        self.username = username
        self.position = position
        self.balance = balance
        self.assets_owned = assets_owned # can have something like [number of assets owned, name of assets, price]
        self.is_jail = is_jail
        self.is_bankrupt = is_bankrupt

    def display_player_details(self):
        print(f'Name - {self.username}')
        print(f'Pos - {self.position}')
        print(f'Balance - ${self.balance}')
        print(f'Assets owned - {self.assets_owned}')


# Creating and accessing players details, need to change this to connected players later
player1 = Player('Ali', 0, 1500, [], False, False)
player2 = Player('Poorv', 0, 1500, [], False, False)
player3 = Player('Deep', 0, 1500, [], False, False)

player_list = [player1, player2, player3]

print(player1.position)


player1.position += board.dice_roll(player1.username)

print(player1.position)
print(f'You are now at {board.BOARD_TILES[player1.position]}')
print(f'{board.BOARD_TILES[player1.position]} Details {board.BOARD_TILES_INFO[board.BOARD_TILES[player1.position]]}')





# Printing details, use this as reference on how to access Class Player
# player1.display_player_details()
# print()
# player2.display_player_details()
# print()
# player3.display_player_details()

# print(player1.username)

