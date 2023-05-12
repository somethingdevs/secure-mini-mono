import service.monopoly_Instance as monopoly
import database.Dao as databaseObj
import database.DaoConstants as DaoConstRoom
from models import player
import time


class room:
    def __init__(self) -> None:
        self.dbRoom = databaseObj.Dao()
        self.daoConstRoom = DaoConstRoom.DaoConstants()
        self.roomID = 1   # need to make this from website input
        self.m = None
    # insert logic to wait for players joining this
    # as a player joins insert in player table
    '''
                as a player joins insert into room and player table with all values;

                AS 4 players join execute the below functions
               
        '''

    def play(self):
        usernames = self.dbRoom.select_query(
            self.daoConstRoom.GET_USERNAME_FROM_PLAYER, (self.roomID,))
        print(usernames)
        player_details = []

        while True:
            if (len(player_details) >= 4):
                print("Players more than 4")
                break
            else:
                print('Waiting for players to join..........')
                time.sleep(5)
                player_details = self.dbRoom.select_query(
                    self.daoConstRoom.GET_PLAYERS_IN_ROOM, (self.roomID,))

        #print('Printing list:',player_details[0].printPlayer())
        player_list = []

        for i in range(len(player_details)):
            # Modify this insert to fetch position
            player_list.append(player.Player(room_id=player_details[i][0], player_id=player_details[i][1], username=usernames[i][0],
                                             money=player_details[i][2], game_round=player_details[i][5], position=player_details[i][4]))
        print('Printing list:', player_list[0].print_player())

        # need to get roomid over here from web
        self.m = monopoly.monopoly_Instance(roomID=1, player_list=player_list)

        # m.game_start()

        # m.game_end_player_details()
