

from pprint import pprint
import pymysql as conn
import board
from database.DaoConstants import DaoConstants
from models.tile import Tile

class Dao:

    def __init__(self):
        self.db = conn.connect(host=DaoConstants.HOST,
                                    user=DaoConstants.USER,
                                    passwd=DaoConstants.PASSWD,
                                    database=DaoConstants.DATABASE,
                                   )

    # Display with condition FIX: make a single select_query with if else single or multiple to execute fetchOne or fetchAll
    def select_query(self,query, values):
       try:
            select_cursor = self.db.cursor()
            print(query)
            if len(values)>1:
                formatted_query = query % values
                print(formatted_query)
                #select_cursor.execute(query, (values[0],values[1]))
                select_cursor.execute(formatted_query)
            elif len(values)==1:
                formatted_query = query % values
                print(formatted_query)
                select_cursor.execute(formatted_query)
            
            rows = select_cursor.fetchall()
       except Exception as e:
            print("An exception occurred:", str(e))
        
       else:
            print(rows)
            return rows 
       finally:
             self.db.close()


    # Display all
    def select_all_query(self,query,istile):
        tiles = []

        try: 
            self.db = conn.connect(host=DaoConstants.HOST,
                                    user=DaoConstants.USER,
                                    passwd=DaoConstants.PASSWD,
                                    database=DaoConstants.DATABASE,
                                    auth_plugin='mysql_native_password')
            print(query)
            
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
                tiles=rows
                
        except Exception as e:
            print("An exception occurred in select_all_query :", str(e))
        finally:
             self.db.close()

        return tiles
     


    def insertion_query(self,query, values):
        try: 
            self.db = conn.connect(host=DaoConstants.HOST,
                                    user=DaoConstants.USER,
                                    passwd=DaoConstants.PASSWD,
                                    database=DaoConstants.DATABASE)
            print(query)
            insertion_cursor = self.db.cursor()
            if(len(values)>1):
                print('in here')
                formatted_query = query % values
                print(formatted_query)
                # Execute the query with all values
                insertion_cursor.execute(formatted_query)
            elif(len(values)==1):
                # Execute the query with the first value only
                formatted_query = query % values[0]
                print(formatted_query)
                insertion_cursor.execute(formatted_query)
            self.db.commit()
        except Exception as e:
            print("An exception occurred:", str(e))
        finally:
            self.db.close()

        # This part just replies with a successful or not, not really important tbh
        if insertion_cursor.rowcount == 1:
            return True

        else:
            return False