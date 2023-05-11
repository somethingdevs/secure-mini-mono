import service.room as startRoom
from database.Dao import Dao, DaoConstants

# new_room = Dao.insertion_query(DaoConstants.CREATE_ROOM, (1, 'ACTIVE'))
# room = startRoom.room(new_room)
room=startRoom.room()
room.play()
