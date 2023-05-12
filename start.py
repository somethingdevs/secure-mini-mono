import service.room as startRoom
from service.userHandle import UserHandle
from models.user import User 

#Get from UI
userrr=User( user_id=None,username="hi",email="hi@gmu", password="hi")
u=UserHandle()
u.createUser(userrr)
u.loginUser(userrr)
#room=startRoom.room()#
#room.play()
