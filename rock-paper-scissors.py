import random
import sys

game = True
wins = 0
losses = 0
draw = 0
matches = 0
wrong_letter = 0

while game == True:

    moves = ['r', 'p', 's']
    player_move = input('Choose your move: ')
    computer_move = random.choice(moves)

    if wrong_letter == 5:
        print('Are you stupid? Play with your own. I`m done')
        sys.exit()

    if player_move.lower() == computer_move:
        print('Draw')
        draw += 1
    elif player_move == 'exit':
        print(f'Total Matches {matches}')
        print(f'Wins {wins}')
        print(f'Losses {losses}')
        print(f'Draw {draw}')
        sys.exit()
    elif player_move not in moves:
        wrong_letter += 1
        print('Your moves: ')
        print('r - rock')
        print('p - paper')
        print('s - scissors')
        print(wrong_letter)

    if player_move.lower() == 'p' and computer_move == 's':
        print('You lose')
        losses += 1
    elif player_move.lower() == 'p' and computer_move == 'r':
        print('You win')
        wins += 1

    elif player_move.lower() == 's' and computer_move == 'r':
        print('You lose')
        losses += 1
    elif player_move.lower() == 's' and computer_move == 'p':
        print('You win')
        wins += 1

    elif player_move.lower() == 'r' and computer_move == 'p':
        print('You lose')
        losses += 1
    elif player_move.lower() == 'r' and computer_move == 's':
        print('You win')
        wins += 1

    matches += 1
