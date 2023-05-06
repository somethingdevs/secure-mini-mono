class DaoConstants:
   #Always list the columns u wanna fetch do not use * in any case
   GET_PLAYERS_IN_ROOM = 'select room_id, player_id, player_balance, player_prop_id, player_position, player_round from player where room_id = %s; '
   ADD_PLAYER_IN_ROOM=''
   CREATE_ROOM=''
   #Always list the columns u wanna fetch do not use * in any case
   BUY_PROPERTY=''#room id player id in player table
   UPDATE_MONEY=''#room id player id player table
   UPDATE_WINNER_FOR_ROOM=''#update winner with user id in room table
   SELECT_LOGS_BY_ROOM_ID='select log_value where room_id= %s'
   # Might remove this
   GET_USERNAME_FROM_PLAYER = 'SELECT u.username FROM user u JOIN player p ON u.user_id = p.player_id WHERE p.room_id = %s;'
   GET_PROPERTY_LIST='select pl.property_id,pl.property_name,pl.property_description,pl.property_cost,pl.property_rent,pl.property_house_cost,pl.property_hotel_cost,pl.is_property_special from property_list pl;'
   GET_PROPERTY_OWNER='select p.room_id, p.player_id, u.username,p.player_balance, p.player_position, p.player_round from player p join user u on p.player_id=u.user_id where p.player_id= (select plpr.player_id from player_property plpr where plpr.property_id=%s and plpr.room_id=%s); '
   INSERT_LOG="INSERT INTO logs (log_value, room_id) VALUES ('%s', %s);"
   #move them to a .env file and add it in gitignore
   HOST='143.42.112.230'
   USER='gokulprathin'
   PASSWD='vIn9e:fW*ic^Y=_'
   DATABASE='default_db'

   def __init__(self) -> None:
      pass
   