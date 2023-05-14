from typing import List, Any
import mysql.connector

# Add an insert query at the end of all of these functions before something is being returned


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


#
# db = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='secureminimono',
#     database='secure_mini_mono'
# )
#
# cursor = db.cursor()
#
# cursor.execute('select * from player where player_id = 1')
#
# player_list = []
#
# for i in cursor:
#     player_list.append(Player(i[0], i[1], 'Ali'))
#
# print(player_list[0].display_player_details())


# Creating and accessing players details, need to change this to connected players later
# player1 = Player('Ali', 0, 0, 1500, [], False, False)
# player2 = Player('Poorvi', 0, 0, 1500, [], False, False)
# player3 = Player('Deep', 0, 0, 1500, [], False, False)

# player_list = [player1, player2, player3]

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
