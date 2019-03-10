#!/usr/bin/env python

__author__ = 'Aditya Verma'
__rollno__ = 2017009

import random
random.seed(0)
tile1, tile2, tile3, tile4, tile5 = 0, 0, 0, 0, 0
tile6, tile7, tile8, tile9 = 0, 0, 0, 0
turn = True  # True for player1's move and False for player2's move


def validBoard():
    '''
        Return True if board state is valid.
        A board state is valid if number of ticks by player1 is always either equal to or one more than the ticks by player2.
    '''
    one, two = 0, 0
    if tile1 == 1:
        one += 1
    elif tile1 == 2:
        two += 1
    if tile2 == 1:
        one += 1
    elif tile2 == 2:
        two += 1
    if tile3 == 1:
        one += 1
    elif tile3 == 2:
        two += 1
    if tile4 == 1:
        one += 1
    elif tile4 == 2:
        two += 1
    if tile5 == 1:
        one += 1
    elif tile5 == 2:
        two += 1
    if tile6 == 1:
        one += 1
    elif tile6 == 2:
        two += 1
    if tile7 == 1:
        one += 1
    elif tile7 == 2:
        two += 1
    if tile8 == 1:
        one += 1
    elif tile8 == 2:
        two += 1
    if tile9 == 1:
        one += 1
    elif tile9 == 2:
        two += 1

    if one >= two:
        return True
    else:
        return False


def validmove(move):
    '''
        Checks whether a move played by a player is valid or invalid.
        Return True if move is valid.
        A move is valid if the corresponding tile for the move is not ticked.
    '''

    if move == 1 and tile1 == 0:
        return True
    if move == 2 and tile2 == 0:
        return True
    if move == 3 and tile3 == 0:
        return True
    if move == 4 and tile4 == 0:
        return True
    if move == 5 and tile5 == 0:
        return True
    if move == 6 and tile6 == 0:
        return True
    if move == 7 and tile7 == 0:
        return True
    if move == 8 and tile8 == 0:
        return True
    if move == 9 and tile9 == 0:
        return True
    return False


def takeNaiveMove():
    '''
        Returns a tile number randomly from the set of unchecked tiles
        with uniform probability distribution.
    '''

    while True:
        move = random.randint(1, 9)
        if validmove(move):
            return move


def takeStrategicMove():
    '''
        Returns a tile number from the set of unchecked tiles
        using some rules.
    '''

    if turn:
        # priority 1: If there is an empty tile mark it.

        if tile1 == 1 and tile2 == 1 and tile3 == 0:
            return 3
        elif tile1 == 1 and tile2 == 0 and tile3 == 1:
            return 2
        elif tile1 == 0 and tile2 == 1 and tile3 == 1:
            return 1
        elif tile4 == 1 and tile5 == 1 and tile6 == 0:
            return 6
        elif tile4 == 1 and tile5 == 0 and tile6 == 1:
            return 5
        elif tile4 == 0 and tile5 == 1 and tile6 == 1:
            return 4
        elif tile7 == 1 and tile8 == 1 and tile9 == 0:
            return 9
        elif tile7 == 1 and tile8 == 0 and tile9 == 1:
            return 8
        elif tile7 == 0 and tile8 == 1 and tile9 == 1:
            return 7
        elif tile1 == 1 and tile4 == 1 and tile7 == 0:
            return 7
        elif tile1 == 1 and tile4 == 0 and tile7 == 1:
            return 4
        elif tile1 == 0 and tile4 == 1 and tile7 == 1:
            return 1
        elif tile2 == 1 and tile5 == 1 and tile8 == 0:
            return 8
        elif tile2 == 1 and tile5 == 0 and tile8 == 1:
            return 5
        elif tile2 == 0 and tile5 == 1 and tile8 == 1:
            return 2
        elif tile3 == 1 and tile6 == 1 and tile9 == 0:
            return 9
        elif tile3 == 1 and tile6 == 0 and tile9 == 1:
            return 6
        elif tile3 == 0 and tile6 == 1 and tile9 == 1:
            return 3
        elif tile1 == 1 and tile5 == 1 and tile9 == 0:
            return 9
        elif tile1 == 1 and tile5 == 0 and tile9 == 1:
            return 5
        elif tile1 == 0 and tile5 == 1 and tile9 == 1:
            return 1
        elif tile3 == 1 and tile5 == 1 and tile7 == 0:
            return 7
        elif tile3 == 1 and tile5 == 0 and tile7 == 1:
            return 5
        elif tile3 == 0 and tile5 == 1 and tile7 == 1:
            return 3

        # priority 2: If opponent is going to win, block it.

        if tile1 == 2 and tile2 == 2 and tile3 == 0:
            return 3
        elif tile1 == 2 and tile2 == 0 and tile3 == 2:
            return 2
        elif tile1 == 0 and tile2 == 2 and tile3 == 2:
            return 1
        elif tile4 == 2 and tile5 == 2 and tile6 == 0:
            return 6
        elif tile4 == 2 and tile5 == 0 and tile6 == 2:
            return 5
        elif tile4 == 0 and tile5 == 2 and tile6 == 2:
            return 4
        elif tile7 == 2 and tile8 == 2 and tile9 == 0:
            return 9
        elif tile7 == 2 and tile8 == 0 and tile9 == 2:
            return 8
        elif tile7 == 0 and tile8 == 2 and tile9 == 2:
            return 7
        elif tile1 == 2 and tile4 == 2 and tile7 == 0:
            return 7
        elif tile1 == 2 and tile4 == 0 and tile7 == 2:
            return 4
        elif tile1 == 0 and tile4 == 2 and tile7 == 2:
            return 1
        elif tile2 == 2 and tile5 == 2 and tile8 == 0:
            return 8
        elif tile2 == 2 and tile5 == 0 and tile8 == 2:
            return 5
        elif tile2 == 0 and tile5 == 2 and tile8 == 2:
            return 2
        elif tile3 == 2 and tile6 == 2 and tile9 == 0:
            return 9
        elif tile3 == 2 and tile6 == 0 and tile9 == 2:
            return 6
        elif tile3 == 0 and tile6 == 2 and tile9 == 2:
            return 3
        elif tile1 == 2 and tile5 == 2 and tile9 == 0:
            return 9
        elif tile1 == 2 and tile5 == 0 and tile9 == 2:
            return 5
        elif tile1 == 0 and tile5 == 2 and tile9 == 2:
            return 1
        elif tile3 == 2 and tile5 == 2 and tile7 == 0:
            return 7
        elif tile3 == 2 and tile5 == 0 and tile7 == 2:
            return 5
        elif tile3 == 0 and tile5 == 2 and tile7 == 2:
            return 3

        # If you get first chance, take a corner.

        if tile1 == tile2 == tile3 == tile4 == tile5 == tile6 == tile7 == tile8 == tile9 == 0:
            return 1

        # priority 3: Take the center if it is free
        if tile5 == 0:
            return 5

        # FORK: If opponent gets a corner and middle is empty then block him taking the middle to create a fork

        if (tile1 == 2 or tile3 == 2 or tile7 == 2 or tile9 == 2) and tile5 == 0:
            return 5

        # FORK: Block opponent's fork (diagonal fork)

        if ( (tile1 == 2 and tile9 == 2) or (tile3 == 2 and tile7 == 2) ) and tile5 == 1:
            if tile2 == 0:
                return 2
            elif tile4 == 0:
                return 4
            elif tile6 == 0:
                return 6
            elif tile8 == 0:
                return 8

        # FORK: Block the intersecting corners

        if (tile2 == 2 or tile3 == 2) and (tile4 == 2 or tile7 == 2) and tile1 == 0:
            return 1
        elif (tile1 == 2 or tile2 == 2) and (tile6 == 2 or tile9 == 2) and tile3 == 0:
            return 3
        elif (tile3 == 2 or tile6 == 2) and (tile7 == 2 or tile8 == 2) and tile9 == 0:
            return 9
        elif (tile1 == 2 or tile4 == 2) and (tile8 == 2 or tile9 == 2) and tile7 == 0:
            return 7

        # priority 4: Take a corner if it is free

        if tile1 == 0:
            return 1
        elif tile3 == 0:
            return 3
        elif tile7 == 0:
            return 7
        elif tile9 == 0:
            return 9

        # priority 5: Do anything else randomly

        else:
            return takeNaiveMove()
    else:
        # priority 1: If there is an empty tile mark it.
        if tile1 == 2 and tile2 == 2 and tile3 == 0:
            return 3
        elif tile1 == 2 and tile2 == 0 and tile3 == 2:
            return 2
        elif tile1 == 0 and tile2 == 2 and tile3 == 2:
            return 1
        elif tile4 == 2 and tile5 == 2 and tile6 == 0:
            return 6
        elif tile4 == 2 and tile5 == 0 and tile6 == 2:
            return 5
        elif tile4 == 0 and tile5 == 2 and tile6 == 2:
            return 4
        elif tile7 == 2 and tile8 == 2 and tile9 == 0:
            return 9
        elif tile7 == 2 and tile8 == 0 and tile9 == 2:
            return 8
        elif tile7 == 0 and tile8 == 2 and tile9 == 2:
            return 7
        elif tile1 == 2 and tile4 == 2 and tile7 == 0:
            return 7
        elif tile1 == 2 and tile4 == 0 and tile7 == 2:
            return 4
        elif tile1 == 0 and tile4 == 2 and tile7 == 2:
            return 1
        elif tile2 == 2 and tile5 == 2 and tile8 == 0:
            return 8
        elif tile2 == 2 and tile5 == 0 and tile8 == 2:
            return 5
        elif tile2 == 0 and tile5 == 2 and tile8 == 2:
            return 2
        elif tile3 == 2 and tile6 == 2 and tile9 == 0:
            return 9
        elif tile3 == 2 and tile6 == 0 and tile9 == 2:
            return 6
        elif tile3 == 0 and tile6 == 2 and tile9 == 2:
            return 3
        elif tile1 == 2 and tile5 == 2 and tile9 == 0:
            return 9
        elif tile1 == 2 and tile5 == 0 and tile9 == 2:
            return 5
        elif tile1 == 0 and tile5 == 2 and tile9 == 2:
            return 1
        elif tile3 == 2 and tile5 == 2 and tile7 == 0:
            return 7
        elif tile3 == 2 and tile5 == 0 and tile7 == 2:
            return 5
        elif tile3 == 0 and tile5 == 2 and tile7 == 2:
            return 3

        # priority 2: If opponent is going to win, block it.

        if tile1 == 1 and tile2 == 1 and tile3 == 0:
            return 3
        elif tile1 == 1 and tile2 == 0 and tile3 == 1:
            return 2
        elif tile1 == 0 and tile2 == 1 and tile3 == 1:
            return 1
        elif tile4 == 1 and tile5 == 1 and tile6 == 0:
            return 6
        elif tile4 == 1 and tile5 == 0 and tile6 == 1:
            return 5
        elif tile4 == 0 and tile5 == 1 and tile6 == 1:
            return 4
        elif tile7 == 1 and tile8 == 1 and tile9 == 0:
            return 9
        elif tile7 == 1 and tile8 == 0 and tile9 == 1:
            return 8
        elif tile7 == 0 and tile8 == 1 and tile9 == 1:
            return 7
        elif tile1 == 1 and tile4 == 1 and tile7 == 0:
            return 7
        elif tile1 == 1 and tile4 == 0 and tile7 == 1:
            return 4
        elif tile1 == 0 and tile4 == 1 and tile7 == 1:
            return 1
        elif tile2 == 1 and tile5 == 1 and tile8 == 0:
            return 8
        elif tile2 == 1 and tile5 == 0 and tile8 == 1:
            return 5
        elif tile2 == 0 and tile5 == 1 and tile8 == 1:
            return 2
        elif tile3 == 1 and tile6 == 1 and tile9 == 0:
            return 9
        elif tile3 == 1 and tile6 == 0 and tile9 == 1:
            return 6
        elif tile3 == 0 and tile6 == 1 and tile9 == 1:
            return 3
        elif tile1 == 1 and tile5 == 1 and tile9 == 0:
            return 9
        elif tile1 == 1 and tile5 == 0 and tile9 == 1:
            return 5
        elif tile1 == 0 and tile5 == 1 and tile9 == 1:
            return 1
        elif tile3 == 1 and tile5 == 1 and tile7 == 0:
            return 7
        elif tile3 == 1 and tile5 == 0 and tile7 == 1:
            return 5
        elif tile3 == 0 and tile5 == 1 and tile7 == 1:
            return 3

        # If you get first chance, take a corner.

        if tile1 == tile2 == tile3 == tile4 == tile5 == tile6 == tile7 == tile8 == tile9 == 0:
            return 1

        # priority 3: Take the center if it is free
        if tile5 == 0:
            return 5

        # priority 4.1 FORK: If opponent gets a corner and middle is empty then block him taking to create a fork by taking the middle

        if (tile1 == 1 or tile3 == 1 or tile7 == 1 or tile9 == 1) and tile5 == 0:
            return 5

        # priority 4.2 FORK: Block opponent's fork (diagonal fork)

        if ( (tile1 == 1 and tile9 == 1) or (tile3 == 1 and tile7 == 1) ) and tile5 == 2:
            if tile2 == 0:
                return 2
            elif tile4 == 0:
                return 4
            elif tile6 == 0:
                return 6
            elif tile8 == 0:
                return 8

        # priority 4.3 FORK: Block the intersecting corners

        if (tile2 == 1 or tile3 == 1) and (tile4 == 1 or tile7 == 1) and tile1 == 0:
            return 1
        elif (tile1 == 1 or tile2 == 1) and (tile6 == 1 or tile9 == 1) and tile3 == 0:
            return 3
        elif (tile3 == 1 or tile6 == 1) and (tile7 == 1 or tile8 == 1) and tile9 == 0:
            return 9
        elif (tile1 == 1 or tile4 == 1) and (tile8 == 1 or tile9 == 1) and tile7 == 0:
            return 7

        # priority 4.4: Take a corner if it is free

        if tile1 == 0:
            return 1
        elif tile3 == 0:
            return 3
        elif tile7 == 0:
            return 7
        elif tile9 == 0:
            return 9

        # priority 5: Do anything

        else:
            return takeNaiveMove()


def win():
    '''
        Returns True if the board state specifies a winning state
        for some player.

        A player wins if ticks made by the player are present either
        i) in a row
        ii) in a cloumn
        iii) in a diagonal
    '''

    c1 = tile1 == tile2 == tile3 == 1 or tile4 == tile5 == tile6 == 1
    c2 = tile7 == tile8 == tile9 == 1 or tile1 == tile4 == tile7 == 1
    c3 = tile2 == tile5 == tile8 == 1 or tile3 == tile6 == tile9 == 1
    c4 = tile1 == tile5 == tile9 == 1 or tile3 == tile5 == tile7 == 1
    c5 = tile1 == tile2 == tile3 == 2 or tile4 == tile5 == tile6 == 2
    c6 = tile7 == tile8 == tile9 == 2 or tile1 == tile4 == tile7 == 2
    c7 = tile2 == tile5 == tile8 == 2 or tile3 == tile6 == tile9 == 2
    c8 = tile1 == tile5 == tile9 == 2 or tile3 == tile5 == tile7 == 2

    if c1 or c2 or c3 or c4 or c5 or c6 or c7 or c8:
        return True
    else:
        return False


def showGame():
    '''
        Shows the current game status in a matrix form.
    '''

    print('''
    |{}|{}|{}|
    |{}|{}|{}|
    |{}|{}|{}|
    '''.format(tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9))


def game(gametype=1):
    '''
        Returns 1 if player1 wins and 2 if player2 wins
        and 0 if it is a draw.

        gametype defines three types of games discussed above.
        i.e., game1, game2, game3
    '''

    status = 0
    c1 = tile1 == tile2 == tile3 == 1 or tile4 == tile5 == tile6 == 1
    c2 = tile7 == tile8 == tile9 == 1 or tile1 == tile4 == tile7 == 1
    c3 = tile2 == tile5 == tile8 == 1 or tile3 == tile6 == tile9 == 1
    c4 = tile1 == tile5 == tile9 == 1 or tile3 == tile5 == tile7 == 1
    c5 = tile1 == tile2 == tile3 == 2 or tile4 == tile5 == tile6 == 2
    c6 = tile7 == tile8 == tile9 == 2 or tile1 == tile4 == tile7 == 2
    c7 = tile2 == tile5 == tile8 == 2 or tile3 == tile6 == tile9 == 2
    c8 = tile1 == tile5 == tile9 == 2 or tile3 == tile5 == tile7 == 2
    c9 = tile1 != 0 and tile2 != 0 and tile3 != 0 and tile4 != 0 and tile5 != 0
    c10 = tile6 != 0 and tile7 != 0 and tile8 != 0 and tile9 != 0

    if c1 or c2 or c3 or c4:
        status = 1
    elif c5 or c6 or c7 or c8:
        status = 2
    elif c9 and c10:
        status = 0

    return status


def game1(n):
    '''
        Returns the winning probability for player1.

        n games are played between two naive players.
        Estimate probability of winning for player1.
        Assume player1 starts the game.
    '''

    global turn, tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9
    wins, draw, wins2 = 0, 0, 0
    for i in range(n):
        turn = True
        tile1, tile2, tile3, tile4, tile5 = 0, 0, 0, 0, 0
        tile6, tile7, tile8, tile9 = 0, 0, 0, 0
        prewin = wins
        for j in range(9):
            tempturn = takeNaiveMove()
            if turn:
                if tempturn == 1:
                    tile1 = 1
                if tempturn == 2:
                    tile2 = 1
                if tempturn == 3:
                    tile3 = 1
                if tempturn == 4:
                    tile4 = 1
                if tempturn == 5:
                    tile5 = 1
                if tempturn == 6:
                    tile6 = 1
                if tempturn == 7:
                    tile7 = 1
                if tempturn == 8:
                    tile8 = 1
                if tempturn == 9:
                    tile9 = 1
            elif not turn:
                if tempturn == 1:
                    tile1 = 2
                if tempturn == 2:
                    tile2 = 2
                if tempturn == 3:
                    tile3 = 2
                if tempturn == 4:
                    tile4 = 2
                if tempturn == 5:
                    tile5 = 2
                if tempturn == 6:
                    tile6 = 2
                if tempturn == 7:
                    tile7 = 2
                if tempturn == 8:
                    tile8 = 2
                if tempturn == 9:
                    tile9 = 2
            turn = not turn  # Switch turns
            # showGame()  # Shows the game in matrix form after each turn
            if win():
                if game(1) == 1:
                    wins += 1
                elif game(1) == 2:
                    wins2 += 1
                break
        if prewin == wins and game(1) == 0:
            draw += 1
    # print('Draw = {}, Wins1 = {}, Wins2 = {}'.format(draw, wins, wins2))
    return wins / n


def game2(n):
    '''
        Returns the winning probability for player1.
        n games are played between a naive and intelligent player.
        Estimate probability of winning for player1.
        Assume player1 is naive and starts the game.
    '''

    global turn, tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9
    wins, draw, wins2 = 0, 0, 0
    for i in range(n):
        turn = True
        tile1, tile2, tile3, tile4, tile5 = 0, 0, 0, 0, 0
        tile6, tile7, tile8, tile9 = 0, 0, 0, 0
        prewin = wins
        for j in range(9):
            if turn:
                tempturn = takeNaiveMove()
                if tempturn == 1:
                    tile1 = 1
                if tempturn == 2:
                    tile2 = 1
                if tempturn == 3:
                    tile3 = 1
                if tempturn == 4:
                    tile4 = 1
                if tempturn == 5:
                    tile5 = 1
                if tempturn == 6:
                    tile6 = 1
                if tempturn == 7:
                    tile7 = 1
                if tempturn == 8:
                    tile8 = 1
                if tempturn == 9:
                    tile9 = 1
            elif not turn:
                tempturn = takeStrategicMove()
                if tempturn == 1:
                    tile1 = 2
                if tempturn == 2:
                    tile2 = 2
                if tempturn == 3:
                    tile3 = 2
                if tempturn == 4:
                    tile4 = 2
                if tempturn == 5:
                    tile5 = 2
                if tempturn == 6:
                    tile6 = 2
                if tempturn == 7:
                    tile7 = 2
                if tempturn == 8:
                    tile8 = 2
                if tempturn == 9:
                    tile9 = 2
            turn = not turn  # Switch turns
            if win():
                if game(2) == 1:
                    wins += 1
                elif game(2) == 2:
                    wins2 += 1
                    # showGame() # Shows the game in matrix form after each turn
                break
        if prewin == wins and game(2) == 0:
            draw += 1
    # print('Draw = {}, Wins1 = {}, Wins2 = {}'.format(draw, wins, wins2))
    return wins / n


def game3(n):
    '''
        Returns the winning probability for player1.
        n games are played between two intelligent players.
        Estimate probability of winning for player1.
        Assume player1 starts the game.
    '''

    global turn, tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9
    wins, draw, wins2 = 0, 0, 0
    for i in range(n):
        turn = True
        tile1, tile2, tile3, tile4, tile5 = 0, 0, 0, 0, 0
        tile6, tile7, tile8, tile9 = 0, 0, 0, 0
        prewin = wins
        for j in range(9):
            tempturn = takeStrategicMove()
            if turn:
                if tempturn == 1:
                    tile1 = 1
                if tempturn == 2:
                    tile2 = 1
                if tempturn == 3:
                    tile3 = 1
                if tempturn == 4:
                    tile4 = 1
                if tempturn == 5:
                    tile5 = 1
                if tempturn == 6:
                    tile6 = 1
                if tempturn == 7:
                    tile7 = 1
                if tempturn == 8:
                    tile8 = 1
                if tempturn == 9:
                    tile9 = 1
            elif not turn:
                if tempturn == 1:
                    tile1 = 2
                if tempturn == 2:
                    tile2 = 2
                if tempturn == 3:
                    tile3 = 2
                if tempturn == 4:
                    tile4 = 2
                if tempturn == 5:
                    tile5 = 2
                if tempturn == 6:
                    tile6 = 2
                if tempturn == 7:
                    tile7 = 2
                if tempturn == 8:
                    tile8 = 2
                if tempturn == 9:
                    tile9 = 2
            turn = not turn  # Switch turns
            # showGame()  # Shows the game in matrix form after each turn
            if win():
                if game(3) == 1:
                    wins += 1
                elif game(3) == 2:
                    wins2 += 1
                break
        if prewin == wins and game(3) == 0:
            draw += 1
    # print('Draw = {}, Wins1 = {}, Wins2 = {}'.format(draw, wins, wins2))
    return wins / n


if __name__ == '__main__':
    print(game1(1000))
    print(game2(10000))
    print(game3(10000))
