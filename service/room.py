import service.monopoly_Instance as monopoly
import database.Dao as databaseObj
import database.DaoConstants as DaoConstRoom
from models import player
from utils.loging import log

import time


class Room:
    def __init__(self) -> None:
        self.dbRoom = databaseObj.Dao()
        self.daoConstRoom = DaoConstRoom.DaoConstants()
        self.m = None


    # Used to play the game

    def play(self, roomID):
        print('The room in play is -', roomID)
        usernames = self.dbRoom.select_query(self.daoConstRoom.GET_USERNAME_FROM_PLAYER, (roomID,))
        if usernames is None:
            return "Room does not exist"
        print(usernames)
        player_details = []

        while True:
            if len(player_details) >= 4:
                print("Players more than 4")
                break
            else:
                print('Waiting for players to join..........')
                time.sleep(5)
                player_details = self.dbRoom.select_query(self.daoConstRoom.GET_PLAYERS_IN_ROOM, (roomID,))

        print('Printing list:', player_details[0].printPlayer())
        player_list = []

        for i in range(len(player_details)):
            # Modify this insert to fetch position
            player_list.append(
                player.Player(room_id=player_details[i][0], player_id=player_details[i][1], username=usernames[i][0],
                              money=player_details[i][2], game_round=player_details[i][5],
                              position=player_details[i][4]))
        print('Printing list:', player_list[0].printPlayer())

        self.m = monopoly.monopoly_Instance(roomID=roomID, player_list=player_list)  # need to get roomid over here from web
        # m.game_start()

    # Joins a player to row in room table
    def join_row(self, room_id: int, user_id: int):
        print('Player joined')
        # user_id = user_id[0][0]
        if not room_id or not user_id:
            player_details = self.dbRoom.select_query(self.daoConstRoom.GET_PLAYERS_IN_ROOM, (room_id,))
            if len(player_details) >= 4:
                return False
            else:
                self.dbRoom.insertion_query(self.daoConstRoom.CREATE_PLAYER, (room_id, user_id,))
                username = self.dbRoom.select_query(self.daoConstRoom.GET_USERNAME_FROM_PLAYER, (room_id,))
                if not username:
                    return False  # Room is not created
                self.dbRoom.insertion_query(self.daoConstRoom.CREATE_ROOM, (user_id, 'ACTIVE', None))
                return True
        else:
            return False

    def createRoom(self, userId, room_id):
        try:
            print('userid is, ', userId)
            if userId is not None:
                print('In here')
                self.dbRoom.insertion_query(self.daoConstRoom.CREATE_ROOM, (room_id, userId, 'ACTIVE', 'NULL'))
                self.dbRoom.insertion_query(self.daoConstRoom.CREATE_PLAYER, (room_id, userId,))

            else:
                print('Cannot create user')
                return 'Error creating room'

        except Exception as e:
            print('in exceptions', e)
