from typing import List, Any

import board


def property_cards():
    pass


class Player:
    def __init__(self, username, position, balance: int, assets_owned: List[Any], is_jail: bool, is_bankrupt: bool):
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



# Creating and accessing players details
player1 = Player('Ali', '32', 2500, ['dsfsa'], True, True)
player1.display_player_details()
print(player1.username)

