class DaoConstants:
    # Always list the columns u wanna fetch do not use * in any case
    GET_PLAYERS_IN_ROOM = 'select room_id, player_id, player_balance, player_prop_id, player_position, player_round from player where room_id = %s; '
    ADD_PLAYER_IN_ROOM = 'INSERT INTO TABLE player (room_id, player_id, player_balance, player_position, player_round) VALUES (%s, %s, 1500, 0, 0)'  # This should have game_round = 0, position = 0, balance = 1500 and there is no need for assets in the player table. Write the query accordingly
    DISPLAY_WIN_LOSS = "SELECT u.username, CONCAT('W = ', COALESCE(wins, 0), ', L = ', COALESCE(losses, 0)) AS win_loss FROM user u " \
                       "LEFT JOIN (SELECT room_player, SUM(IF(room_winner = room_player, 1, 0)) AS wins, SUM(IF(room_winner != room_player, 1, 0)) AS losses FROM room " \
                       "GROUP BY room_player) wl ON u.user_id = wl.room_player ORDER BY u.username;)"  # should display number of wins and losses(total games - wins) of all playeres
    CREATE_ROOM = 'INSERT INTO TABLE user (room_player, room_status) VALUES (%s, %s)' # should pass room_player(player_id basically) and 'ACTIVE' in place of the params. room id is supposed to be auto_increment, if it throws an error it means that the table wasnt created properly
    JOIN_ROOM = 'INSERT INTO TABLE user (room_id, room_player, room_status) VALUES (%s, %s, %s)' # should pass room_player(player_id basically) and 'ACTIVE' in place of the params.
    CREATE_USER = 'INSERT INTO TABLE user (username, email, pass) VALUES(%s, %s, %s)'
    FETCH_USER = 'SELECT username from TABLE user where user_id = %s' # pretty sure this is wrong, but idk what is needed here
    # GET_PLAYER_DETAILS = 'select u.username, p.player_position'
    GET_PROPERTY_OWNED = 'SELECT property_id from player_property where room_id = %s and player_id = %s'

    # Always list the columns u wanna fetch do not use * in any case

    GET_PROPERTY_FROM_PLAYER_OWNED = 'SELECT pl.property_name FROM player_property pp JOIN property_list pl ON pp.property_id = pl.property_id WHERE pp.room_id = %s AND pp.player_id = %s;'
    BUY_PROPERTY = 'INSERT INTO player_property VALUES (%s, %s, %s);'  # room id player id in player table
    SELL_PROPERTY = 'DELETE FROM player_property WHERE room_id = %s AND player_id = %s AND property_id = %s'
    UPDATE_MONEY = 'UPDATE player set player_balance = %s where room_id = %s and player_id = %s'  # room id player id player table
    UPDATE_EVERYTHING = 'UPDATE player set player_balance = %s, player_position = %s, player_round = %s where room_id = %s and player_id = %s'
    UPDATE_WINNER_FOR_ROOM = 'UPDATE room set room_status = %s, room_winner = %s where room_id = %s'  # update winner with user id and set status to inactive in room table
    SELECT_LOGS_BY_ROOM_ID = 'select log_value where room_id= %s'
    # Might remove this
    GET_USERNAME_FROM_PLAYER = 'SELECT u.username FROM user u JOIN player p ON u.user_id = p.player_id WHERE p.room_id = %s;'
    GET_PROPERTY_LIST = 'select pl.property_id,pl.property_name,pl.property_description,pl.property_cost,pl.property_rent,pl.property_house_cost,pl.property_hotel_cost,pl.is_property_special from property_list pl;'
    GET_PROPERTY_OWNER = 'select p.room_id, p.player_id, u.username,p.player_balance, p.player_position, p.player_round from player p join user u on p.player_id=u.user_id where p.player_id= (select plpr.player_id from player_property plpr where plpr.property_id=%s and plpr.room_id=%s); '
    INSERT_LOG = "INSERT INTO logs (log_value, room_id) VALUES ('%s', %s);"
    # move them to a .env file and add it in gitignore
    HOST = '143.42.112.230'
    USER = 'gokulprathin'
    PASSWD = 'vIn9e:fW*ic^Y=_'
    DATABASE = 'default_db'

    def __init__(self) -> None:
        pass
