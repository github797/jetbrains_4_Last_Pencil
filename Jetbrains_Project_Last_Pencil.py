# Players take turns taking X pencils until none of them remain.
# Players (the bot and the user) can remove not more than 3 pencils at a time.
# The player who takes the last pencil loses the game.
# A bot follows a winning strategy.
# If the bot's position isn't the winning one, it takes any number of pencils (1, 2, or 3) at random.

import random


def start_pencils():
    print('How many pencils would you like to use: ')
    while True:
        pencils = input()

        if pencils.isdigit() is False or int(pencils) < 0:
            print('The number of pencils should be numeric')
            continue
        pencils = int(pencils)

        if pencils == 0:
            print('The number of pencils should be positive')
            continue
        break
    return pencils


def start_player():
    turn = input(f'Who will be the first ({", ".join(players)}):\n').capitalize()
    while turn not in players:
        print(f'Choose between {players[0]} and {players[1]}')
        turn = input().capitalize()
    return turn


def bot(pencils, turn):  # Jack is the bot
    print(f"{turn}'s turn:")
    if pencils % 4 == 0:
        pencils_taken = 3
    elif pencils % 4 == 3:
        pencils_taken = 2
    elif pencils % 4 == 2 or pencils == 1:
        pencils_taken = 1
    else:
        pencils_taken = random.randint(1, 3)
    print(pencils_taken)
    pencils -= pencils_taken
    return pencils


def user(pencils, turn):  # John is the user
    print(f"{turn}'s turn!")
    while True:
        pencils_taken = input()
        if pencils_taken not in ['1', '2', '3']:
            print("Possible values: '1', '2' or '3")
            continue
        pencils_taken = int(pencils_taken)
        if pencils_taken > pencils:
            print('Too many pencils were taken')
            continue
        break
    pencils -= pencils_taken
    return pencils


def game(pencils, turn):
    while pencils > 0:
        print('|' * pencils)
        if turn == players[1]:  # Jack is the bot
            pencils = bot(pencils, turn)
        else:
            pencils = user(pencils, turn)

        turn = players[1] if turn == players[0] else players[0]

        if pencils == 0:
            print(f'{turn} won!')
            break


if __name__ == '__main__':
    players = ['John', 'Jack']
    game(start_pencils(), start_player())
