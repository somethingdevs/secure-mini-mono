from service.wrapper import frontEndWrapperRoom
from service.room import room

newRoom = room()
frontEndWrapperRoom('start', newRoom)

game = newRoom.m

while game.is_game_over == False:
    frontEndWrapperRoom(input("Enter the input: "), newRoom)
