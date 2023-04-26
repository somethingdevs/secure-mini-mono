from board import display_moves, game_over, dice_roll
import moves
import property


# Statically instantiating three players
player1 = property.Player('Ali', 0, 0, 1500, [], False, False)
player2 = property.Player('Poorvi', 0, 0, 1500, [], False, False)
player3 = property.Player('Deep', 0, 0, 1500, [], False, False)

player_list = [player1, player2, player3]

is_game_over = False
incorrect_move = True

# display moves
# accept input
# depending upon input do something - for now roll the dice
# move forward
# go until rounds are 15. and then stop

display_moves()
while not is_game_over:
    for player in player_list:
            print(f'{player.username}\'s turn ')
            print(f'Cash - {player.balance}\t Rounds played - {player.game_round}\t Player position - {player.position}')
            print('----------------------------------------------------------------')
            while incorrect_move:
                game_input = input('Enter your choice : ')
                print(end='\n\n')
                if game_input.casefold() == 'r':
                    moves.player_moves(player, dice_roll(player))
                    incorrect_move = False
                else:
                    print('Error! Incorrect Input', end='\n\n')
                    incorrect_move = True
            is_game_over = game_over(player)