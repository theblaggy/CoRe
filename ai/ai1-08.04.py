# -*- coding: utf-8 -*-
"""Artificial Intelligence #1"""

import random

turn_cunt = 0
ret_list = []

my_board = [["#" for x in range(8)] for y in range(8)]

corners = [(0, 0), (7, 0), (0, 7), (7, 7)]
corner_left = [(1, 0), (7, 1), (0, 6), (6, 7)]
corner_right = [(0, 1), (6, 0), (1, 7), (7, 6)]
corner_diag = [(1, 1), (6, 1), (1, 6), (6, 6)]
corner_diag_pair = {(0, 0): (1, 1),
                    (7, 0): (6, 1),
                    (0, 7): (1, 6),
                    (7, 7): (6, 6),

                    (1, 1): (0, 0),
                    (6, 1): (7, 0),
                    (1, 6): (0, 7),
                    (6, 6): (7, 7)}
corner_sides = [(1, 0), (7, 1), (0, 6), (6, 7), (0, 1), (6, 0), (1, 7), (7, 6)]
corner_sides_reverse = {(1, 0): (6, 7),
                        (7, 1): (0, 6),
                        (0, 6): (7, 1),
                        (6, 7): (1, 0),

                        (0, 1): (7, 6),
                        (6, 0): (1, 7),
                        (1, 7): (6, 0),
                        (7, 6): (0, 1)}

side_top = [(x, 0) for x in range(8)]
side_bottom = [(x, 7) for x in range(8)]
side_left = [(0, y) for y in range(8)]
side_right = [(7, y) for y in range(8)]
sides = [side_top, side_bottom, side_left, side_right]


def corner_kill(board, symbol):
    for x in range(8):
        for y in range(8):
            if getboard(board, x, y) != '#' and getboard(board, x, y) != symbol:
                if x == 0 and y == 0 and getboard(board, 1, 1) == '#': return 1, 1
                if x == 0 and y == 7 and getboard(board, 1, 6) == '#': return 1, 6
                if x == 7 and y == 0 and getboard(board, 6, 1) == '#': return 6, 1
                if x == 7 and y == 7 and getboard(board, 1, 1) == '#': return 6, 6


def rndm(board):
    while True:
        x = random.choice(range(8))
        y = random.choice(range(8))
        if getboard(board, x, y) == '#': return x, y


def corner_side(board):
    choice = random.choice(corner_sides)
    x = choice[0]
    y = choice[1]
    if getboard(board, x, y) == '#': return x, y


def corner(new, board):
    for field in corner_diag:
        if field == new:
            if getboard(board, corner_diag_pair[field][0], corner_diag_pair[field][1]) == "#": return corner_diag_pair[field]


def side(new, board):
    if new in side_top and (ret_list[-1] not in side_top or ret_list[-1] in corners):
        if new in ((2, 0), (3, 0), (6, 0)):
            if getboard(board, 1, 0) == "#": return 1, 0
            elif getboard(board, 6, 0) == "#": return 6, 0

        elif new in ((1, 0), (4, 0), (5, 0)):
            if getboard(board, 6, 0) == "#": return 6, 0
            elif getboard(board, 1, 0) == "#": return 1, 0

    elif new in side_bottom and (ret_list[-1] not in side_bottom or ret_list[-1] in corners):
        if new in ((2, 7), (3, 7), (6, 7)):
            if getboard(board, 1, 7) == "#": return 1, 7
            elif getboard(board, 6, 7) == "#": return 6, 7

        elif new in ((1, 7), (4, 7), (5, 7)):
            if getboard(board, 6, 7) == "#": return 6, 7
            elif getboard(board, 1, 7) == "#": return 1, 7

    elif new in side_left and (ret_list[-1] not in side_left or ret_list[-1] in corners):
        if new in ((0, 2), (0, 3), (0, 6)):
            if getboard(board, 0, 1) == "#": return 0, 1
            elif getboard(board, 0, 6) == "#": return 0, 6

        elif new in ((0, 1), (0, 4), (0, 5)):
            if getboard(board, 0, 6) == "#": return 0, 6
            elif getboard(board, 0, 1) == "#": return 0, 1

    elif new in side_right and (ret_list[-1] not in side_right or ret_list[-1] in corners):
        if new in ((7, 2), (7, 3), (7, 6)):
            if getboard(board, 7, 1) == "#": return 7, 1
            elif getboard(board, 7, 6) == "#": return 7, 6

        elif new in ((7, 1), (7, 4), (7, 5)):
            if getboard(board, 7, 6) == "#":
                if getboard(board, 7, 6) == "#": return 7, 6
                elif getboard(board, 7, 1) == "#": return 7, 1


def last_edge(board):
    if ret_list[-1] in (corners or corner_diag):
        if ret_list[-1] == (0, 0):
            if getboard(board, 6, 7) == "#" and getboard(board, 7, 6) != "#": return 6, 7
            elif getboard(board, 7, 6) == "#" and getboard(board, 6, 7) != "#": return 7, 6
            elif getboard(board, 6, 7) == "#" and getboard(board, 7, 6) == "#": return random.choice([(6, 7), (7, 6)])

        elif ret_list[-1] == (7, 0):
            if getboard(board, 0, 6) == "#" and getboard(board, 1, 7) != "#": return 0, 6
            elif getboard(board, 1, 7) == "#" and getboard(board, 0, 6) != "#": return 1, 7
            elif getboard(board, 0, 6) == "#" and getboard(board, 1, 7) == "#": return random.choice([(0, 6), (1, 7)])

        elif ret_list[-1] == (0, 7):
            if getboard(board, 7, 1) == "#" and getboard(board, 6, 0) != "#": return 7, 1
            elif getboard(board, 6, 0) == "#" and getboard(board, 7, 1) != "#": return 6, 0
            elif getboard(board, 7, 1) == "#" and getboard(board, 6, 0) == "#": return random.choice([(7, 1), (6, 0)])

        elif ret_list[-1] == (7, 7):
            if getboard(board, 1, 0) == "#" and getboard(board, 0, 1) != "#": return 1, 0
            elif getboard(board, 0, 1) == "#" and getboard(board, 1, 0) != "#": return 0, 1
            elif getboard(board, 1, 0) == "#" and getboard(board, 0, 1) == "#": return random.choice([(1, 0), (0, 1)])


def remaining_sides(board, my_sides):
    if len(my_sides) != 4:
        for side1 in sides:
            if side1 not in my_sides:
                for corner_side1 in corner_sides:
                    if corner_side1 in side1:
                        if getboard(board, corner_side1[0], corner_side1[1]) == "#": return corner_side1


def fill_sides(board):
    remaining_side_fields = []
    for side1 in sides:
        for field in side1:
            if getboard(board, field[0], field[1]) == "#" and field not in corners:
                remaining_side_fields.append(field)
    if len(remaining_side_fields) != 0:
        return random.choice(remaining_side_fields)


def first_turn(new, board, symbol):
    # Line 0
    if new == (0, 0): return corner_kill(board, symbol)
    elif new == (1, 0): return 6, 0
    elif new == (2, 0): return 1, 0
    elif new == (3, 0): return 1, 0
    elif new == (4, 0): return 6, 0
    elif new == (5, 0): return 6, 0
    elif new == (6, 0): return 1, 0
    elif new == (7, 0): return corner_kill(board, symbol)

    # Line 1
    elif new == (0, 1): return 0, 6
    elif new == (1, 1): return 0, 0
    elif new == (2, 1): return 0, 1
    elif new == (3, 1): return 0, 1
    elif new == (4, 1): return 7, 1
    elif new == (5, 1): return 7, 1
    elif new == (6, 1): return 7, 0
    elif new == (7, 1): return 7, 6

    # Line 2
    elif new == (0, 2): return 0, 1
    elif new == (1, 2): return 1, 0
    elif new == (2, 2): return corner_side(board)
    elif new == (3, 2): return corner_side(board)
    elif new == (4, 2): return corner_side(board)
    elif new == (5, 2): return corner_side(board)
    elif new == (6, 2): return 6, 0
    elif new == (7, 2): return 7, 1

    # Line 3
    elif new == (0, 3): return 0, 1
    elif new == (1, 3): return 1, 0
    elif new == (2, 3): return corner_side(board)
    elif new == (3, 3): return corner_side(board)
    elif new == (4, 3): return corner_side(board)
    elif new == (5, 3): return corner_side(board)
    elif new == (6, 3): return 6, 0
    elif new == (7, 3): return 7, 1

    # Line 4
    elif new == (0, 4): return 0, 6
    elif new == (1, 4): return 1, 7
    elif new == (2, 4): return corner_side(board)
    elif new == (3, 4): return corner_side(board)
    elif new == (4, 4): return corner_side(board)
    elif new == (5, 4): return corner_side(board)
    elif new == (6, 4): return 6, 7
    elif new == (7, 4): return 7, 6

    # Line 5
    elif new == (0, 5): return 0, 6
    elif new == (1, 5): return 1, 7
    elif new == (2, 5): return corner_side(board)
    elif new == (3, 5): return corner_side(board)
    elif new == (4, 5): return corner_side(board)
    elif new == (5, 5): return corner_side(board)
    elif new == (6, 5): return 6, 7
    elif new == (7, 5): return 7, 6

    # Line 6
    elif new == (0, 6): return 0, 1
    elif new == (1, 6): return 0, 7
    elif new == (2, 6): return 0, 6
    elif new == (3, 6): return 0, 6
    elif new == (4, 6): return 7, 6
    elif new == (5, 6): return 7, 6
    elif new == (6, 6): return 7, 7
    elif new == (7, 6): return 7, 1

    # Line 7
    elif new == (0, 7): return corner_kill(board, symbol)
    elif new == (1, 7): return 6, 7
    elif new == (2, 7): return 1, 7
    elif new == (3, 7): return 1, 7
    elif new == (4, 7): return 6, 7
    elif new == (5, 7): return 6, 7
    elif new == (6, 7): return 1, 7
    elif new == (7, 7): return corner_kill(board, symbol)


def second_turn(new, board, symbol):
    # If Enemy In Corner, Then Corner Kill
    ret = corner_kill(board, symbol)
    if ret is not None: return ret

    # If Enemy Corner Diag, Then Corner
    ret = corner(new, board)
    if ret is not None: return ret

    # If Enemy At Side, Then Corner Side At Same Side
    ret = side(new, board)
    if ret is not None: return ret

    # If Last Turn Corner Side, Then Reverse Corner Side
    if ret_list[-1] in corner_sides: return corner_sides_reverse[ret_list[-1]]

    # If Last Turn Edge, Then Reverse Corner Side
    if ret_list[-1] in (corners or corner_diag):
        if ret_list[-1] == (0, 0): return random.choice([(6, 7), (7, 6)])
        elif ret_list[-1] == (7, 0): return random.choice([(0, 6), (1, 7)])
        elif ret_list[-1] == (0, 7): return random.choice([(7, 1), (6, 0)])
        elif ret_list[-1] == (7, 7): return random.choice([(1, 0), (0, 1)])

    # Else Random
    return rndm(board)


def random_turn(new, board, symbol, my_sides):
    # If Enemy In Corner, Then Corner Kill
    ret = corner_kill(board, symbol)
    if ret is not None: return ret

    # If Enemy Corner Diag, Then Corner
    ret = corner(new, board)
    if ret is not None: return ret

    # If Enemy At Side, Then Corner Side At Same Side
    ret = side(new, board)
    if ret is not None: return ret

    # If Last Turn Edge, Then Reverse Corner Side
    ret = last_edge(board)
    if ret is not None: return ret

    # Try To Get 3rd and 4th Side
    ret = remaining_sides(board, my_sides)
    if ret is not None: return ret

    # Try To Fill Sides
    ret = fill_sides(board)
    if ret is not None: return ret

    # Else Random
    ret = rndm(board)
    if ret is not None: return ret


def turn(board, symbol):
    global turn_cunt, my_board

    enemy = ("X" if symbol == "O" else "O")
    turn_cunt += 1
    
    old_board = my_board

    # Board
    my_board = []
    for y in range(8):
        row = []
        for x in range(8):
            if getboard(board, x, y) == "#": field = "#"
            elif getboard(board, x, y) == symbol: field = symbol
            elif getboard(board, x, y) == enemy: field = enemy
            row.append(field)
        my_board.append(row)

    # New
    new = None
    for y in range(8):
        for x in range(8):
            if my_board[y][x] != old_board[y][x] and my_board[y][x] != symbol and old_board[y][x] != symbol:
                new = (x, y)
                break

    # My Sides
    my_sides = []
    for side1 in sides:
        for field in side1:
            if getboard(board, field[0], field[1]) == symbol:
                if side1 not in my_sides:
                    my_sides.append(side1)

    if turn_cunt == 1:
        ret = first_turn(new, board, symbol)
        if symbol == "X": ret = 6, 7

    elif turn_cunt == 2:
        ret = second_turn(new, board, symbol)

    else:
        ret = random_turn(new, board, symbol, my_sides)

    if getboard(board, ret[0], ret[1]) != "#": ret = rndm(board)
    ret_list.append(ret)
    return ret
