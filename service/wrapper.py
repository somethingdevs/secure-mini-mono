from service.monopoly_Instance import monopoly_Instance
from service.room import room
from utils.driver import moves_list


def frontEndWrapperRoom(data, room: room):
    # Check if the input is from the correct user
    if room.m is None:
        room.play()
    frontEndWrapperGame(data, room.m)


def frontEndWrapperGame(data, game: monopoly_Instance):
    player = game.player_list[game.prevCounterPlayer % len(game.player_list)]
    # If this is the new Round
    if game.prevCounterPlayer != game.counterPlayer:
        game.player_turn_start()
        return

    # If the payer is on buy option of the property or the player is at the first input screen
    if game.buy_options is not None and data.lower() == 'y':
        game.player_buy_option()
        game.buy_options = None
        message = 'Cash - %s \t Rounds played - %s \t Player position - %s' % (
            player.balance, player.game_round, player.position)
        game.db.insertion_query(
            game.daoConst.INSERT_LOG, (message, player.room_id))
        print(
            f'Cash - {player.balance}\t Rounds played - {player.game_round}\t Player position - {player.position}')
        print('----------------------------------------------------------------')
        moves_list()
    else:
        game.current_player_turn(data)

    player = game.player_list[game.prevCounterPlayer % len(game.player_list)]
    # It means the player round has ended and the new round must start. Few things to take care of
    if game.prevCounterPlayer != game.counterPlayer:
        game.db.insertion_query(game.daoConst.UPDATE_EVERYTHING, (
            player.balance, player.position, player.game_round, player.room_id, player.player_id))

        message = 'Round end! Player details updated'
        game.db.insertion_query(
            game.daoConst.INSERT_LOG, (message, player.room_id))
        game.player_turn_start()

    # If GAME OVER!
    game.is_game_over = game.game_over(player)
    if (game.is_game_over):
        game.game_winner(game)
