from decouple import config


class DaoConstants:

    ROOM_EXIST="SELECT EXISTS (SELECT 1 FROM rooms WHERE roomID = %s);"

    GET_PLAYERS_IN_ROOM = 'select room_id, player_id, player_balance, player_prop_id, player_position, player_round from player where room_id = %s;'
    CREATE_USER = "insert into user ( username, email, pass) VALUES ('%s','%s','%s');"
    GET_USER = "select username,pass from user where email='%s';"
    GET_EXISTING_USER = "SELECT EXISTS (SELECT 1 FROM user WHERE username = '%s' AND email = '%s');"
    DISPLAY_WIN_LOSS = "SELECT u.username, CONCAT('W = ', COALESCE(wins, 0), ', L = ', COALESCE(losses, 0)) AS win_loss " \
                       "FROM user u LEFT JOIN (   SELECT room_player,  SUM(IF(room_winner = room_player, 1, 0)) AS wins, SUM(IF(room_winner != room_player, 1, 0)) AS losses " \
                       "FROM room GROUP BY room_player) wl ON u.user_id = wl.room_player WHERE u.username = '%s';  "

    CREATE_ROOM = "insert into room (room_id,room_player, room_status, room_winner) VALUES(%s,%s, '%s', %s)"
    GET_MAX_ROOM = 'select max(room_id) from room;'
    GET_PROPERTY_FROM_LIST = 'select property_id from  property_list where property_name = %s'
    BUY_PROPERTY = 'INSERT INTO player_property VALUES (%s, %s, %s);'  # room id player id in player table
    SELL_PROPERTY = 'DELETE FROM player_property WHERE room_id = %s AND player_id = %s AND property_id = %s'
    UPDATE_EVERYTHING = 'UPDATE player set player_balance = %s, player_position = %s, player_round = %s where room_id = %s and player_id = %s'
    UPDATE_WINNER_FOR_ROOM = ''
    SELECT_LOGS_BY_ROOM_ID = 'select log_value from logs where room_id= %s order by log_id LIMIT 100'
    GET_USER_LOGS = "SELECT logs.log_id, logs.log_timestamp, logs.log_value, logs.room_id FROM logs" \
                    " JOIN room ON logs.room_id = room.room_id" \
                    " JOIN user ON room.room_player = user.user_id" \
                    " WHERE user.username = '%s';"
    GET_USER_ID = 'select user_id from user where username="%s"'
    GET_USERNAME_FROM_PLAYER = 'SELECT u.username FROM user u JOIN player p ON u.user_id = p.player_id WHERE p.room_id = %s;'
    GET_PROPERTY_LIST = 'select pl.property_id,pl.property_name,pl.property_description,pl.property_cost,pl.property_rent,pl.property_house_cost,pl.property_hotel_cost,pl.is_property_special from property_list pl;'
    GET_PROPERTY_OWNER = 'select p.room_id, p.player_id, u.username,p.player_balance, p.player_position, p.player_round from player p join user u on p.player_id=u.user_id where p.player_id= (select plpr.player_id from player_property plpr where plpr.property_id=%s and plpr.room_id=%s); '
    INSERT_LOG = "INSERT INTO logs (log_value, room_id) VALUES ('%s', %s);"

    # Database .env
    HOST = config('HOST')
    USER = config('USER')
    PASSWD = config('PASSWD')
    DATABASE = config('DATABASE')

    def __init__(self) -> None:
        pass
