class Tile:
    def __init__(self, tile_id, tile_name, description, cost, rent, house_cost, hotel_cost, is_special):
        self.tile_id = tile_id
        self.tile_name = tile_name
        self.description = description
        self.cost = cost
        self.rent = rent
        self.house_cost = house_cost
        self.hotel_cost = hotel_cost
        self.is_special = is_special

    def printTile(self):
        print(vars(self))
