# -*- coding: utf-8 -*-
"""Artificial Intelligence #1"""


"""
@author the_blaggy$
@date 06.04.2017
"""

# TODO:
# x Try To Kill Threats, Do Not Protect
# ! Check Injection Creating Through Killing
# ! Check Multi Kills Through Corner Placing
#
#
#
#
#

cou = 0

""" Data """


corners = [(0, 0), (7, 0), (0, 7), (7, 7)]
corner_left = [(1, 0), (7, 1), (0, 6), (6, 7)]
corner_right = [(0, 1), (6, 0), (1, 7), (7, 6)]
corner_diags = [(1, 1), (6, 1), (1, 6), (6, 6)]
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

turn_counter = 0
ret_list = []
my_board = [["#" for x in range(8)] for y in range(8)]

# getboard = lambda board, x, y: board[y][x]


def rndm(board):
    for x in range(8):
        for y in range(8):
            if getboard(board, x, y) == "#":
                return x, y


""" Corners """


def corner_kill(board, symbol):

    """
    for x in range(8):
        for y in range(8):

            if getboard(board, x, y) != '#' and getboard(board, x, y) != symbol:

                free = 0

                for side in sides:
                    for field in side:

                        if field not in corners:

                            if getboard(board, field[0], field[1]) == "#": free += 1

                if free == 0:

                    if x == 0 and y == 0 and getboard(board, 1, 1) == '#':

                        if getboard(board, 7, 0) == "#" and getboard(board, 0, 7) == "#":

                            if getboard(board, 0, 6) == symbol and getboard(board, 6, 0) == symbol:

                                return rating(board, symbol, [(0, 7), (7, 0)])

                            if getboard(board, 1, 1) == "#": return 1, 1

                        if getboard(board, 7, 0) != "#" and getboard(board, 0, 7) != "#":

                            if getboard(board, 7, 7) == "#": return 7, 7
                            if getboard(board, 1, 1) == "#": return 1, 1

                        else: return rating(board, symbol, corners)

                    if x == 0 and y == 7 and getboard(board, 1, 6) == '#':

                        if getboard(board, 0, 0) == "#" and getboard(board, 7, 7) == "#":

                            if getboard(board, 0, 1) == symbol and getboard(board, 6, 7) == symbol:

                                return rating(board, symbol, [(0, 0), (7, 7)])

                            if getboard(board, 1, 6) == "#": return 1, 6

                        if getboard(board, 0, 0) != "#" and getboard(board, 7, 7) != "#":

                            if getboard(board, 7, 0) == "#": return 7, 0
                            if getboard(board, 1, 6) == "#": return 1, 6

                        else: return rating(board, symbol, corners)

                    if x == 7 and y == 0 and getboard(board, 6, 1) == '#':

                        if getboard(board, 7, 7) == "#" and getboard(board, 0, 0) == "#":

                            if getboard(board, 7, 6) == symbol and getboard(board, 1, 0) == symbol:

                                return rating(board, symbol, [(7, 7), (0, 0)])

                            if getboard(board, 6, 1) == "#": return 6, 1

                        if getboard(board, 7, 7) != "#" and getboard(board, 0, 0) != "#":

                            if getboard(board, 0, 7) == "#": return 0, 7
                            if getboard(board, 6, 1) == "#": return 6, 1

                        else: return rating(board, symbol, corners)

                    if x == 7 and y == 7 and getboard(board, 6, 6) == '#':

                        if getboard(board, 0, 7) == "#" and getboard(board, 7, 0) == "#":

                            if getboard(board, 1, 7) == symbol and getboard(board, 7, 1) == symbol:

                                return rating(board, symbol, [(0, 7), (7, 0)])

                            if getboard(board, 6, 6) == "#": return 6, 6

                        if getboard(board, 0, 7) != "#" and getboard(board, 7, 0) != "#":

                            if getboard(board, 0, 0) == "#": return 0, 0
                            if getboard(board, 6, 6) == "#": return 6, 6

                        else: return rating(board, symbol, corners)

                else:

                    if x == 0 and y == 0 and getboard(board, 1, 1) == '#': return 1, 1
                    if x == 0 and y == 7 and getboard(board, 1, 6) == '#': return 1, 6
                    if x == 7 and y == 0 and getboard(board, 6, 1) == '#': return 6, 1
                    if x == 7 and y == 7 and getboard(board, 6, 6) == '#': return 6, 6
    """
    for x in range(8):
        for y in range(8):

            if getboard(board, x, y) != '#' and getboard(board, x, y) != symbol:

                if x == 0 and y == 0 and getboard(board, 1, 1) == '#': return 1, 1
                if x == 0 and y == 7 and getboard(board, 1, 6) == '#': return 1, 6
                if x == 7 and y == 0 and getboard(board, 6, 1) == '#': return 6, 1
                if x == 7 and y == 7 and getboard(board, 6, 6) == '#': return 6, 6


def closed_corner(board):

    for field in corner_diags:
        if getboard(board, field[0], field[1]) != "#":
            if getboard(board, corner_diag_pair[field][0], corner_diag_pair[field][1]) == "#":
                return corner_diag_pair[field]


def last_corner(board, symbol):

    if ret_list[-1] in (corners or corner_diags):

        if ret_list[-1] == (0, 0): return rating(board, symbol, [(1, 7), (6, 7), (7, 6), (7, 1)])
        if ret_list[-1] == (7, 0): return rating(board, symbol, [(0, 1), (0, 6), (1, 7), (6, 7)])
        if ret_list[-1] == (0, 7): return rating(board, symbol, [(7, 6), (7, 1), (6, 0), (1, 0)])
        if ret_list[-1] == (7, 7): return rating(board, symbol, [(6, 0), (1, 0), (0, 1), (0, 6)])


def corner_side(board, symbol):

    return rating(board, symbol, corner_sides)


def second_corner_side(board, symbol):

    my_corner_sides = []
    choices = []

    for corner_side1 in corner_sides:
        if getboard(board, corner_side1[0], corner_side1[1]) == symbol:
            if corner_side1 not in my_corner_sides: my_corner_sides.append(corner_side1)

    if len(my_corner_sides) != 8:
        for corner_side1 in corner_sides:
            if corner_side1 not in my_corner_sides:
                if getboard(board, corner_side1[0], corner_side1[1]) == "#": choices.append(corner_side1)

        return rating(board, symbol, choices)


""" Sides """


def defend_side(board, symbol, new):

    if new in side_top:

        if new in ((2, 0), (3, 0), (6, 0)):
            if getboard(board, 1, 0) == "#": return 1, 0
            if getboard(board, 6, 0) == "#": return 6, 0

        if new in ((1, 0), (4, 0), (5, 0)):
            if getboard(board, 6, 0) == "#": return 6, 0
            if getboard(board, 1, 0) == "#": return 1, 0

        if getboard(board, 1, 0) == symbol and getboard(board, 6, 0) == symbol:

            if new == (3, 0):
                if getboard(board, 2, 0) == "#": return 2, 0
                if getboard(board, 4, 0) == "#": return 4, 0

            if new == (4, 0):
                if getboard(board, 5, 0) == "#": return 5, 0
                if getboard(board, 3, 0) == "#": return 3, 0

        if new == (3, 0):
            if getboard(board, 4, 0) == "#": return 4, 0
            if getboard(board, 2, 0) == "#": return 2, 0

        if new == (4, 0):
            if getboard(board, 3, 0) == "#": return 3, 0
            if getboard(board, 5, 0) == "#": return 5, 0

    if new in side_bottom:

        if new in ((2, 7), (3, 7), (6, 7)):
            if getboard(board, 1, 7) == "#": return 1, 7
            if getboard(board, 6, 7) == "#": return 6, 7

        if new in ((1, 7), (4, 7), (5, 7)):
            if getboard(board, 6, 7) == "#": return 6, 7
            if getboard(board, 1, 7) == "#": return 1, 7

        if getboard(board, 1, 7) == symbol and getboard(board, 6, 7) == symbol:

            if new == (3, 7):
                if getboard(board, 2, 7) == "#": return 2, 7
                if getboard(board, 4, 7) == "#": return 4, 7

            if new == (4, 7):
                if getboard(board, 5, 7) == "#": return 5, 7
                if getboard(board, 3, 7) == "#": return 3, 7

        if new == (3, 7):
            if getboard(board, 4, 7) == "#": return 4, 7
            if getboard(board, 2, 7) == "#": return 2, 7

        if new == (4, 7):
            if getboard(board, 3, 7) == "#": return 3, 7
            if getboard(board, 5, 7) == "#": return 5, 7

    if new in side_left:

        if new in ((0, 2), (0, 3), (0, 6)):
            if getboard(board, 0, 1) == "#": return 0, 1
            if getboard(board, 0, 6) == "#": return 0, 6

        if new in ((0, 1), (0, 4), (0, 5)):
            if getboard(board, 0, 6) == "#": return 0, 6
            if getboard(board, 0, 1) == "#": return 0, 1

        if getboard(board, 0, 1) == symbol and getboard(board, 0, 6) == symbol:

            if new == (0, 3):
                if getboard(board, 0, 2) == "#": return 0, 2
                if getboard(board, 0, 4) == "#": return 0, 4

            if new == (0, 4):
                if getboard(board, 0, 5) == "#": return 0, 5
                if getboard(board, 0, 3) == "#": return 0, 3

        if new == (0, 3):
            if getboard(board, 0, 4) == "#": return 0, 4
            if getboard(board, 0, 2) == "#": return 0, 2

        if new == (0, 4):
            if getboard(board, 0, 3) == "#": return 0, 3
            if getboard(board, 0, 5) == "#": return 0, 5

    if new in side_right:

        if new in ((7, 2), (7, 3), (7, 6)):
            if getboard(board, 7, 1) == "#": return 7, 1
            if getboard(board, 7, 6) == "#": return 7, 6

        if new in ((7, 1), (7, 4), (7, 5)):
            if getboard(board, 7, 6) == "#": return 7, 6
            if getboard(board, 7, 1) == "#": return 7, 1

        if getboard(board, 7, 1) == symbol and getboard(board, 7, 6) == symbol:

            if new == (7, 3):
                if getboard(board, 7, 2) == "#": return 7, 2
                if getboard(board, 7, 4) == "#": return 7, 4

            if new == (7, 4):
                if getboard(board, 7, 5) == "#": return 7, 5
                if getboard(board, 7, 3) == "#": return 7, 3

        if new == (7, 3):
            if getboard(board, 7, 4) == "#": return 7, 4
            if getboard(board, 7, 2) == "#": return 7, 2

        if new == (7, 4):
            if getboard(board, 7, 3) == "#": return 7, 3
            if getboard(board, 7, 5) == "#": return 7, 5


def defend_side_ng(board, symbol, new):

    fields = []

    for side in sides:

        if new in side and new not in corner_diags:

            for field in side:

                injectable = side_injection(board, symbol, field)
                if field not in corners and not injectable: fields.append(field)

            return rating(board, symbol, fields)


def fill_sides(board, symbol):

    enemy = ("X" if symbol == "O" else "O")
    remaining_side_fields = []

    for side in sides:
        for field in side:

            if field not in corners:

                x, y = field[0], field[1]

                adjacent = 0

                if getboard(board, x + 1, y) != "#" and getboard(board, x + 1, y) != enemy: adjacent += 1
                if getboard(board, x - 1, y) != "#" and getboard(board, x - 1, y) != enemy: adjacent += 1
                if getboard(board, x, y + 1) != "#" and getboard(board, x, y + 1) != enemy: adjacent += 1
                if getboard(board, x, y - 1) != "#" and getboard(board, x, y - 1) != enemy: adjacent += 1

                if side == side_top or side == side_bottom:
                    if getboard(board, x + 1, y) == enemy and getboard(board, x + 2, y) == symbol: adjacent += 1
                    if getboard(board, x - 1, y) == enemy and getboard(board, x - 2, y) == symbol: adjacent += 1

                if side == side_left or side == side_right:
                    if getboard(board, x, y + 1) == enemy and getboard(board, x, y + 2) == symbol: adjacent += 1
                    if getboard(board, x, y - 1) == enemy and getboard(board, x, y - 2) == symbol: adjacent += 1

                threatened = rating_threatened(board, symbol, x, y)
                injectable = side_injection(board, symbol, (x, y))

                if adjacent >= 2 and threatened == 0 and not injectable:
                    remaining_side_fields.append(field)

    return rating(board, symbol, remaining_side_fields)


def remaining_sides(board, symbol):

    my_sides = []
    choices = []

    for side in sides:
        for field in side:

            if getboard(board, field[0], field[1]) == symbol:
                if side not in my_sides: my_sides.append(side)

    if len(my_sides) != 4:
        for side in sides:
            if side not in my_sides:
                for field in corner_sides:
                    if field in side:
                        if getboard(board, field[0], field[1]) == "#": choices.append(field)

        return rating(board, symbol, choices)


def side_injection(board, symbol, field):

    enemy = ("X" if symbol == "O" else "O")

    injectable = False
    ignore = False

    if getboard(board, field[0], field[1]) == "#":
        if field not in corners and field not in corner_sides:

            if field in side_top or field in side_bottom:

                if field in side_top: side = side_top
                if field in side_bottom: side = side_bottom

                if getboard(board, field[0] + 1, field[1]) == "#" and getboard(board, field[0] + 2, field[1]) != "#":
                    injectable = True

                if getboard(board, field[0] - 1, field[1]) == "#" and getboard(board, field[0] - 2, field[1]) != "#":
                    injectable = True

            if field in side_left or field in side_right:

                if field in side_left: side = side_left
                if field in side_right: side = side_right

                if getboard(board, field[0], field[1] + 1) == "#" and getboard(board, field[0], field[1] + 2) != "#":
                    injectable = True

                if getboard(board, field[0], field[1] - 1) == "#" and getboard(board, field[0], field[1] - 2) != "#":
                    injectable = True

            for field1 in side:
                if getboard(board, field1[0], field1[1]) == enemy: ignore = True; break

            if injectable and not ignore: return True
            else: return False


""" Remaining Functions """


def fill_middle_ng(board, symbol):

    middle = []

    for x in range(1, 7):
        for y in range(1, 7):

            if (x, y) not in corner_diags: middle.append((x, y))

    return rating(board, symbol, middle)


def flip(board_copy, symbol, x, y):

    enemy = ("X" if symbol == "O" else "O")

    # print(turn_counter, (x, y))
    # print(board_copy)

    # Corner Kill
    if x == 1 and y == 1 and board_copy[0][0] == enemy: board_copy[0][0] = symbol
    if x == 1 and y == 6 and board_copy[7][0] == enemy: board_copy[7][0] = symbol
    if x == 6 and y == 1 and board_copy[0][7] == enemy: board_copy[0][7] = symbol
    if x == 6 and y == 6 and board_copy[7][7] == enemy: board_copy[7][7] = symbol

    # Right Side
    found = False

    for i in range(x + 1, 8):
        if board_copy[y][i] == symbol: found = True

    if found:
        for i in range(x + 1, 8):
            if board_copy[y][i] == symbol: break
            elif board_copy[y][i] == enemy: board_copy[y][i] = symbol

    # Left Side
    found = False

    for i in range(x)[::-1]:
        if board_copy[y][i] == symbol: found = True

    if found:
        for i in range(x)[::-1]:
            if board_copy[y][i] == symbol: break
            elif board_copy[y][i] == enemy: board_copy[y][i] = symbol

    # Bottom Side
    found = False

    for i in range(y + 1, 8):
        if board_copy[i][x] == symbol: found = True

    if found:
        for i in range(y + 1, 8):
            if board_copy[i][x] == symbol: break
            elif board_copy[i][x] == enemy: board_copy[i][x] = symbol

    # Upper Side
    found = False

    for i in range(y)[::-1]:
        if board_copy[i][x] == symbol: found = True

    if found:
        for i in range(y)[::-1]:
            if board_copy[i][x] == symbol: break
            elif board_copy[i][x] == enemy: board_copy[i][x] = symbol

    return board_copy


""" Rating """


def rating(board, symbol, choices):

    rating_dict = {}
    ratings = []

    for element in choices:

        x, y = element[0], element[1]

        if getboard(board, x, y) == "#":

            kills = rating_kills(board, symbol, x, y)
            threats = rating_threats(board, symbol, x, y)
            enemy_kills = rating_protected(board, symbol, x, y)
            threatened = rating_threatened(board, symbol, x, y)
            adjacent_ones = rating_adjacent_ones(board, symbol, x, y)
            in_corner_side = (1 if (x, y) in corner_sides else 0)

            calculated_rating = calculate_rating(kills, threats, enemy_kills, threatened, adjacent_ones, in_corner_side)
            rating_dict.update({(x, y): (calculated_rating,
                                         kills, threats, enemy_kills, threatened, adjacent_ones, in_corner_side)})
            ratings.append(((x, y), calculated_rating))

    try:
        ratings = sorted(ratings, key=lambda x: x[1])

        if turn_counter == 2: return ratings[-1]
        return ratings[-1][0]

    except IndexError:
        pass


def calculate_rating(kills, threats, protected, threatened, adjacent_ones, in_corner_side):

    score = (1.5 * kills + 0.25 * threats + 0.75 * protected + -1 * threatened + 0.5 * adjacent_ones
             + 0.5 * in_corner_side)

    return score


def rating_kills(board, symbol, x, y):

    enemy = ("X" if symbol == "O" else "O")

    # Row
    run, counter, xy_passed, count_row = 0, 0, 0, 0

    for x1 in range(8):

        if (x1, y) == (x, y): xy_passed = 1; run = 1; count_row = counter
        elif getboard(board, x1, y) == symbol and xy_passed == 1: count_row = counter; break
        elif getboard(board, x1, y) == symbol and run == 0: run = 1
        elif getboard(board, x1, y) == symbol and (x1, y) != (x, y): counter = 0
        elif getboard(board, x1, y) == enemy and run == 1: counter += 1

    # Column
    run, counter, xy_passed, count_column = 0, 0, 0, 0

    for y1 in range(8):

        if (x, y1) == (x, y): xy_passed = 1; run = 1; count_column = counter
        elif getboard(board, x, y1) == symbol and xy_passed == 1: count_column = counter; break
        elif getboard(board, x, y1) == symbol and run == 0: run = 1
        elif getboard(board, x, y1) == symbol and (x, y1) != (x, y): counter = 0
        elif getboard(board, x, y1) == enemy and run == 1: counter += 1

    counted_kills = count_row + count_column
    return counted_kills


def rating_threats(board, symbol, x, y):

    enemy = ("X" if symbol == "O" else "O")

    # Row
    run, count_row = 0, 0

    for x1 in range(8):

        if getboard(board, x1, y) == "#": run = 1
        elif getboard(board, x1, y) == enemy and run == 1: count_row += 1
        elif getboard(board, x1, y) == symbol and (x1, y) != (x, y): count_row = 0; run = 0
        elif (x1, y) == (x, y): break

    # Row Reverse
    run, count_row_rev = 0, 0

    for x1 in range(8, 0, -1):

        if getboard(board, x1, y) == "#": run = 1
        elif getboard(board, x1, y) == enemy and run == 1: count_row_rev += 1
        elif getboard(board, x1, y) == symbol and (x1, y) != (x, y): count_row_rev = 0; run = 0
        elif (x1, y) == (x, y): break

    # Column
    run, count_column = 0, 0

    for y1 in range(8):

        if getboard(board, x, y1) == "#": run = 1
        elif getboard(board, x, y1) == enemy and run == 1: count_column += 1
        elif getboard(board, x, y1) == symbol and (x, y1) != (x, y): count_column = 0; run = 0
        elif (x, y1) == (x, y): break

    # Column Reverse
    run, count_column_rev = 0, 0

    for y1 in range(8, 0, -1):

        if getboard(board, x, y1) == "#": run = 1
        elif getboard(board, x, y1) == enemy and run == 1: count_column_rev += 1
        elif getboard(board, x, y1) == symbol and (x, y1) != (x, y): count_column_rev = 0; run = 0
        elif (x, y1) == (x, y): break

    counted_threats = count_row + count_row_rev + count_column + count_column_rev
    return counted_threats


def rating_protected(board, symbol, x, y):

    enemy = ("X" if symbol == "O" else "O")

    # Row
    run, counter, xy_passed, count_row = 0, 0, 0, 0

    for x1 in range(8):

        if (x1, y) == (x, y): xy_passed = 1; run = 1; count_row = counter
        elif getboard(board, x1, y) == enemy and xy_passed == 1: count_row = counter; break
        elif getboard(board, x1, y) == enemy and run == 0: run = 1
        elif getboard(board, x1, y) == enemy and (x1, y) != (x, y): counter = 0
        elif getboard(board, x1, y) == symbol and run == 1: counter += 1

    # Column
    run, counter, xy_passed, count_column = 0, 0, 0, 0

    for y1 in range(8):

        if (x, y1) == (x, y): xy_passed = 1; run = 1; count_column = counter
        elif getboard(board, x, y1) == enemy and xy_passed == 1: count_column = counter; break
        elif getboard(board, x, y1) == enemy and run == 0: run = 1
        elif getboard(board, x, y1) == enemy and (x, y1) != (x, y): counter = 0
        elif getboard(board, x, y1) == symbol and run == 1: counter += 1

    counted_protected = count_row + count_column
    return counted_protected


def rating_threatened(board, symbol, x, y):

    enemy = ("X" if symbol == "O" else "O")

    threatened = 0
    board_copy = board
    board_copy = flip(board_copy, symbol, x, y)

    # Row

    # Enemy -> Symbol -> Free
    run, xy_passed = 0, 0

    for x1 in range(8):

        if getboard(board_copy, x1, y) == enemy: run = 1
        elif (x1, y) == (x, y) and run == 1: xy_passed = 1
        elif getboard(board_copy, x1, y) == "#" and xy_passed == 1: threatened = 1; break
        elif getboard(board_copy, x1, y) == enemy and xy_passed == 1: break

    # Free -> Symbol -> Enemy
    run, xy_passed = 0, 0

    for x1 in range(8):

        if getboard(board_copy, x1, y) == "#": run = 1
        elif (x1, y) == (x, y) and run == 1: xy_passed = 1
        elif getboard(board_copy, x1, y) == enemy and xy_passed == 1: threatened = 1; break

    # Column

    # Enemy -> Symbol -> Free
    run, xy_passed = 0, 0

    for y1 in range(8):

        if getboard(board_copy, x, y1) == enemy: run = 1
        elif (x, y1) == (x, y) and run == 1: xy_passed = 1
        elif getboard(board_copy, x, y1) == "#" and xy_passed == 1: threatened = 1; break
        elif getboard(board_copy, x, y1) == enemy and xy_passed == 1: break

    # Free -> Symbol -> Enemy
    run, xy_passed = 0, 0

    for y1 in range(8):

        if getboard(board_copy, x, y1) == "#": run = 1
        elif (x, y1) == (x, y) and run == 1: xy_passed = 1
        elif getboard(board_copy, x, y1) == enemy and xy_passed == 1: threatened = 1; break

    return threatened


def rating_adjacent_ones(board, symbol, x, y):

    enemy = ("X" if symbol == "O" else "O")

    adjacent = 0
    board_copy = board
    board_copy = flip(board_copy, symbol, x, y)

    if getboard(board_copy, x + 1, y) != "#" and getboard(board_copy, x + 1, y) != enemy: adjacent += 1
    if getboard(board_copy, x - 1, y) != "#" and getboard(board_copy, x - 1, y) != enemy: adjacent += 1
    if getboard(board_copy, x, y + 1) != "#" and getboard(board_copy, x, y + 1) != enemy: adjacent += 1
    if getboard(board_copy, x, y - 1) != "#" and getboard(board_copy, x, y - 1) != enemy: adjacent += 1

    return adjacent


""" Hard Coded Turns """


def first_turn(board, symbol, new):

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
    elif new == (2, 2): return corner_side(board, symbol)
    elif new == (3, 2): return corner_side(board, symbol)
    elif new == (4, 2): return corner_side(board, symbol)
    elif new == (5, 2): return corner_side(board, symbol)
    elif new == (6, 2): return 6, 0
    elif new == (7, 2): return 7, 1

    # Line 3
    elif new == (0, 3): return 0, 1
    elif new == (1, 3): return 1, 0
    elif new == (2, 3): return corner_side(board, symbol)
    elif new == (3, 3): return corner_side(board, symbol)
    elif new == (4, 3): return corner_side(board, symbol)
    elif new == (5, 3): return corner_side(board, symbol)
    elif new == (6, 3): return 6, 0
    elif new == (7, 3): return 7, 1

    # Line 4
    elif new == (0, 4): return 0, 6
    elif new == (1, 4): return 1, 7
    elif new == (2, 4): return corner_side(board, symbol)
    elif new == (3, 4): return corner_side(board, symbol)
    elif new == (4, 4): return corner_side(board, symbol)
    elif new == (5, 4): return corner_side(board, symbol)
    elif new == (6, 4): return 6, 7
    elif new == (7, 4): return 7, 6

    # Line 5
    elif new == (0, 5): return 0, 6
    elif new == (1, 5): return 1, 7
    elif new == (2, 5): return corner_side(board, symbol)
    elif new == (3, 5): return corner_side(board, symbol)
    elif new == (4, 5): return corner_side(board, symbol)
    elif new == (5, 5): return corner_side(board, symbol)
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


def second_turn(board, symbol, new):

    # If Enemy In Corner, Then Corner Kill
    ret = corner_kill(board, symbol)
    if ret is not None: return ret

    # If Enemy Corner Diag, Then Corner
    ret = closed_corner(board)
    if ret is not None: return ret

    # If Enemy At Side, Then Corner Side At Same Side
    ret = defend_side(board, symbol, new)
    if ret is not None: return ret

    # Check For Kill If Placing At Corner Side
    z = rating(board, symbol, corner_sides)
    if z[1] >= 1: return z[0]

    # If Last Turn Corner Side, Then Reverse Corner Side
    if ret_list[-1] in corner_sides: return corner_sides_reverse[ret_list[-1]]

    # If Last Turn Corner Or Corner Sides, Then Reverse Corner Side
    if ret_list[-1] in (corners or corner_diags):

        if ret_list[-1] == (0, 0): return rating(board, symbol, [(6, 7), (7, 6)])
        elif ret_list[-1] == (7, 0): return rating(board, symbol, [(0, 6), (1, 7)])
        elif ret_list[-1] == (0, 7): return rating(board, symbol, [(7, 1), (6, 0)])
        elif ret_list[-1] == (7, 7): return rating(board, symbol, [(1, 0), (0, 1)])


def random_turn(board, symbol, new):

    # If Enemy In Corner, Then Corner Kill
    ret = corner_kill(board, symbol)
    if ret is not None: return ret

    # If Enemy Corner Diag, Then Corner
    ret = closed_corner(board)
    if ret is not None: return ret

    # If Enemy At Side And I Not, Then Corner Side At Same Side
    ret = defend_side(board, symbol, new)
    if ret is not None: return ret

    # If Enemy At Side And I Too, Then Test Best Field
    ret = defend_side_ng(board, symbol, new)
    if ret is not None: return ret

    # If Last Turn Corner Or Corner Sides, Then Reverse Corner Side
    ret = last_corner(board, symbol)
    if ret is not None: return ret

    # Try To Get 3rd and 4th Side
    ret = remaining_sides(board, symbol)
    if ret is not None: return ret

    # Try To Get 2nd Corner Side On Each Side And Kill One
    ret = rating(board, symbol, corner_sides)
    if ret is not None and ret[1] != 0: return ret

    # Try To Get 2nd Corner Side On Each Side
    ret = second_corner_side(board, symbol)
    if ret is not None: return ret

    # Try To Fill Sides
    ret = fill_sides(board, symbol)
    if ret is not None: return ret

    # Try To Fill Middle
    ret = fill_middle_ng(board, symbol)
    if ret is not None: return ret

    # Corners and Corner Diag, Last 4 Turns
    # ret = rating(board, symbol, (rating(board, symbol, corners), rating(board, symbol, corner_diags)))
    # if ret is not None: return ret

    # Last Chance
    ret = rndm(board)
    if ret is not None: return ret


def turn(board, symbol):

    global turn_counter, my_board

    enemy = ("X" if symbol == "O" else "O")
    turn_counter += 1

    draw_board(board, turn_counter)

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

            if my_board[y][x] != old_board[y][x]:
                if my_board[y][x] != symbol and old_board[y][x] == "#":
                    new = (x, y)

    if turn_counter == 1:
        ret = first_turn(board, symbol, new)
        if symbol == "X": ret = 6, 7

    elif turn_counter == 2:
        ret = second_turn(board, symbol, new)

    else:
        ret = random_turn(board, symbol, new)

    draw_board(board, turn_counter)

    ret_list.append(ret)
    return ret


def draw_board(board, turn_counter):

    print(turn_counter)

    for y in range(8):
        for x in range(8):
            print(getboard(board, x, y), end=" ")
        print()
    print()


# the_blaggy$ #
