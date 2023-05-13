from typing import List, Any
import mysql.connector


class Player:
    def __init__(self, room_id, player_id, username, money, position, game_round):
        self.room_id = room_id
        self.player_id = player_id
        self.username = username
        self.position = position
        self.game_round = game_round
        self.balance = money
        self.assets_owned = []

    def player_moves(self, dice_value):
        self.position += dice_value
        print("You rolled: ", dice_value)
        if self.position > 31:
            self.position = self.position % 31
            print('Completed round!', end='\n\n')
            self.add_balance(200)
            self.game_round += 1
        # print(player.position)
        return self.position

    def display_player_details(self):
        print(f'Name - {self.username}')
        print(f'Pos - {self.position}')
        print(f'Balance - ${self.balance}')
        print(f'Assets owned - {self.assets_owned}')

    def buy_tile(self, tile):
        # Adding name of the tile to the list of assets owned
        self.assets_owned.append(tile.tile_name)
        price = tile.cost
        self.balance = self.balance - price
        print(f'{tile.tile_name} bought!')

    def sell_tile(self, tile):
        # Removing name of the tile from list of assets owned
        price = tile.cost / 2
        self.balance = self.balance + price
        print(f'Property Sold! New Balance - {self.balance}')
        self.assets_owned.remove(tile.tile_name)
        return tile.tile_id

    def build_house(self, tile):
        if tile in self.assets_owned:
            self.balance -= tile.house_cost
            print(f'House built on {tile.tile_name}')
        else:
            print('Asset is not owned!')
            return False
        pass

    def build_hotel(self, tile):
        if tile in self.assets_owned:
            self.balance -= tile.hotel_cost
            print(f'Hotel built on {tile.tile_name}')
        else:
            print('Asset is not owned!')
            return False
        pass

    def charge_rent(self, tile):
        rent = tile.rent
        # print(rent)
        self.balance -= rent
        return rent

    def add_balance(self, added_amount):
        self.balance += added_amount

    def reduce_balance(self, reduced_amount):
        self.balance -= reduced_amount

    def check_balance(self, tile):
        if self.balance > tile.cost:
            return True
        else:
            return False

    def go_to_jail(self):
        self.position = 8
        print('Sent to Jail!', end='\n\n')
        self.game_round += 2

    def print_player(self):
        print(vars(self))