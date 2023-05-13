import pymysql

from models.tile import Tile


class Database:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
        )

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def execute_query(self, query):
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result

    def select_query(self, query, values):
        try:
            select_cursor = self.connection.cursor()
            # print(query)
            if (len(values) > 1):
                select_cursor.execute(query, (values[0], values[1]))

            else:
                select_cursor.execute(query, values)

            rows = select_cursor.fetchall()
        except Exception as e:
            print("An exception occurred:", str(e))

        else:
            # print(rows)
            return rows


    def select_all_query(self, query, istile):
        tiles = []

        try:
            # print(query)
            select_all_cursor = self.db.cursor()
            select_all_cursor.execute(query)
            rows = select_all_cursor.fetchall()
            if istile:
                for row in rows:
                    #tile_id, tile_name, description, cost, rent, house_cost, hotel_cost, is_special = row
                    tileObj = Tile(tile_id=row[0], tile_name=row[1], description=row[2], cost=row[3], rent=row[4],
                                   house_cost=row[5], hotel_cost=row[6], is_special=row[7])
                    tiles.append(tileObj)
            else:
                tiles = rows

        except Exception as e:
            print("An exception occurred in select_all_query :", str(e))

        return tiles

    def insertion_query(self, query, values):
        try:
            # print(query)
            insertion_cursor = self.db.cursor()
            if (len(values) > 1):
                print(values[0], values[1])
                formatted_query = query % values
                print(formatted_query)
                insertion_cursor.execute(formatted_query)
            else:
                insertion_cursor.execute(query, values)
            self.db.commit()
        except Exception as e:
            print("An exception occurred:", str(e))


        # This part just replies with a successful or not, not really important tbh
        if insertion_cursor.rowcount == 1:
            return True
        else:
            return False
