from typing import List, Any

import board


class Player:

    def __init__(self, username, position: int, game_round: int, balance: int, assets_owned: List[Any], is_jail: bool,
                 is_bankrupt: bool):
        self.username = username
        self.position = position
        self.game_round = game_round
        self.balance = balance
        self.assets_owned = assets_owned  # can have something like [number of assets owned, name of assets, price]
        self.is_jail = is_jail
        self.is_bankrupt = is_bankrupt

    def player_moves(self, dice_value):
        self.position += dice_value
        if self.position > 31:
            self.position = self.position % 31
            print('Completed round!', end='\n\n')
            self.add_balance(200)
            self.game_round += 1
        # print(player.position)
        print(f'You are now at {board.BOARD_TILES[self.position]}')
        print(
            f'Description - {board.BOARD_TILES_INFO[board.BOARD_TILES[self.position]][0]}',
            end='\n\n\n')

    def display_player_details(self):
        print(f'Name - {self.username}')
        print(f'Pos - {self.position}')
        print(f'Balance - ${self.balance}')
        print(f'Assets owned - {self.assets_owned}')

    def buy_tile(self, tile):
        self.assets_owned.append(tile)
        price = board.BOARD_TILES_INFO[tile][2]
        self.balance = self.balance - price

    def sell_tile(self, tile):
        self.assets_owned.remove(tile)
        price = board.BOARD_TILES_INFO[tile][2]
        self.balance = self.balance + price

    def build_house(self, asset):
        pass

    def build_hotel(self, asset):
        pass

    def charge_rent(self, tile):
        rent = board.BOARD_TILES_INFO[board.BOARD_TILES[tile]][4][0]
        print(rent)
        self.balance -= rent
        return rent

    def add_balance(self, added_amount):
        self.balance += added_amount

    def reduce_balance(self, reduced_amount):
        self.balance -= reduced_amount

    def check_balance(self, tile):
        if self.balance > board.BOARD_TILES_INFO[board.BOARD_TILES[tile]][2]:
            return True
        else:
            return False

    def go_to_jail(self):
        self.position = 8
        print('Sent to Jail!', end='\n\n')
        # self.game_round += 2



# Creating and accessing players details, need to change this to connected players later
player1 = Player('Ali', 0, 0, 1500, [], False, False)
player2 = Player('Poorvi', 0, 0, 1500, [], False, False)
player3 = Player('Deep', 0, 0, 1500, [], False, False)

player_list = [player1, player2, player3]

# print(player1.position)
# player1.position += board.dice_roll(player1.username)
# print(player1.position)
# print(f'You are now at {board.BOARD_TILES[player1.position]}')
# print(f'{board.BOARD_TILES[player1.position]} Details {board.BOARD_TILES_INFO[board.BOARD_TILES[player1.position]]}')

# print(player2.position)
# player2.position += board.dice_roll(player2.username)
# print(player2.position)
# print(f'You are now at {board.BOARD_TILES[player2.position]}')
# print(f'{board.BOARD_TILES[player2.position]} Details {board.BOARD_TILES_INFO[board.BOARD_TILES[player2.position]]}')

# print(player3.position)
# player3.position += board.dice_roll(player3.username)
# print(player3.position)
# print(f'You are now at {board.BOARD_TILES[player3.position]}')
# print(f'{board.BOARD_TILES[player3.position]} Details {board.BOARD_TILES_INFO[board.BOARD_TILES[player3.position]]}')


# Printing details, use this as reference on how to access Class Player
# player1.display_player_details()
# print()
# player2.display_player_details()
# print()
# player3.display_player_details()

# print(player1.username)
