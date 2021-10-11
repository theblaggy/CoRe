import random


# MaxFlips V11
def turn(board, symbol):
    debug = 0  # make KI more talkative
    depth = 0  # depth to take into account in countReturnFlips(). 0 means only our move-options and the enemy reactions are calculated.
    other = "X"  # symbol for opponent
    if (symbol == other): other = "O"

    field = []  # create our own memory construct of the playing field
    move = 0
    for x in range(8):
        field.append([])
        for y in range(8):
            field[x].append(0)
            if getboard(board, x, y) == symbol: field[x][y] = 1
            if getboard(board, x, y) == other: field[x][y] = -1
            if field[x][y] != 0: move += 1

    if debug: print("\nMaxFlips V11 # Move {}".format(move))

    if move == 0:  # hard coded choice of first moves
        firstMoves = []
        firstMoves.append((2, 0))
        firstMoves.append((5, 0))
        firstMoves.append((2, 7))
        firstMoves.append((5, 7))
        firstMoves.append((0, 2))
        firstMoves.append((0, 5))
        firstMoves.append((7, 2))
        firstMoves.append((7, 5))
        return firstMoves[random.randrange(len(firstMoves))]

    self = 1;
    other = -1;
    free = 0  # define short hands for field occupations

    # check for corner kills
    if field[0][0] == other and field[1][1] == free:
        if debug: print("Move to {}, {}: Corner Kill upper left".format(2, 2))
        return (1, 1)
    if field[7][0] == other and field[6][1] == free:
        if debug: print("Move to {}, {}: Corner Kill upper right".format(7, 2))
        return (6, 1)
    if field[0][7] == other and field[1][6] == free:
        if debug: print("Move to {}, {}: Corner Kill lower left".format(2, 7))
        return (1, 6)
    if field[7][7] == other and field[6][6] == free:
        if debug: print("Move to {}, {}: Corner Kill lower right".format(7, 7))
        return (6, 6)

    # check for unkillable corner
    if field[0][0] == free and field[1][1] != free:
        if debug: print("Move to {}, {}: Occupy Corner upper left".format(1, 1))
        return (0, 0)
    if field[7][0] == free and field[6][1] != free:
        if debug: print("Move to {}, {}: Occupy Corner upper right".format(8, 1))
        return (7, 0)
    if field[0][7] == free and field[1][6] != free:
        if debug: print("Move to {}, {}: Occupy Corner lower left".format(1, 8))
        return (0, 7)
    if field[7][7] == free and field[6][6] != free:
        if debug: print("Move to {}, {}: Occupy Corner lower right".format(8, 8))
        return (7, 7)

    flipMatrix = createFlipMatrix(
        field)  # calculate immediately following flips for each move and build the base value matrix from it
    if debug:
        print("Immediate Flips:")
        printMatrix(field, flipMatrix)

    maskOccupiedFields(field, flipMatrix)  # set the value of all occupied fields to -64

    countReturnFlips(field, flipMatrix,
                     depth)  # calculate maximum possible return flips for each move and subtract that from the values
    if debug:
        print("Flip Matrix depth {}:".format(depth))
        printMatrix(field, flipMatrix)

    valueOpponentFlips(field,
                       flipMatrix)  # calculate which fields would yield flips for the opponent and add those to the values (so we take them defensively)

    valuePlacement(field, flipMatrix)  # give more value to fields without free spaces around

    # valueEvenSpaces(field, flipMatrix) # if there is an even number of free spaces in the row / column the fields get a penalty

    # valueStrategicValue(field, flipMatrix) # Moves clearing a row / column from opponent stones get a bonus

    if debug:
        print("Final Value Matrix:")
        printMatrix(field, flipMatrix)

    # Now we just have to find the positions with the best scores and pick one. :)
    # Assemble list of best moves according to the matrix
    bestMoveList = getBestMoves(flipMatrix)
    if debug: print("{} positions with best value of {} found".format(len(bestMoveList), findMaxInMaxtrix(flipMatrix)))

    # If only one best rated move available - we take a shortcut here
    if len(bestMoveList) == 1:
        if debug: print("Move to {}, {}: Can't be picky".format(bestMoveList[0][0] + 1, bestMoveList[0][1] + 1))
        return bestMoveList[0]

    # special priorities for picking a move from the bestMoveList
    # 1. Corner fields
    for i in range(len(bestMoveList)):
        x = bestMoveList[i][0]
        y = bestMoveList[i][1]
        if (x == 0 or x == 7) and (y == 0 or y == 7):
            if debug: print("Occupy Corner {}, {}".format(x + 1, y + 1))
            return (x, y)

    # 2. Border fields next to an enemy
    for i in range(len(bestMoveList)):
        x = bestMoveList[i][0]
        y = bestMoveList[i][1]
        if (x == 0 and field[1][y] == -1) \
                or (x == 7 and field[6][y] == -1) \
                or (y == 0 and field[x][1] == -1) \
                or (y == 7 and field[x][6] == -1):
            if debug: print("Occupy Border next to opponent at {}, {}".format(x + 1, y + 1))
            return (x, y)

    # 3. Border fields in general
    for i in range(len(bestMoveList)):
        x = bestMoveList[i][0]
        y = bestMoveList[i][1]
        if x == 0 or x == 7 or y == 0 or y == 7:
            if debug: print("Occupy Border at {}, {}".format(x + 1, y + 1))
            return (x, y)

    # 4. check if the best rated moves cotain any other position with an enemy stone next to it
    for i in range(len(bestMoveList)):
        x = bestMoveList[i][0]
        y = bestMoveList[i][1]
        if x < 7 and field[x + 1][y] == -1:  # check right
            if debug: print("Move to {}, {}: Picking field close to opponent to the right".format(x + 1, y + 1))
            return (x, y)
        if x > 0 and field[x - 1][y] == -1:  # check left
            if debug: print("Move to {}, {}: Picking field close to opponent to the left".format(x + 1, y + 1))
            return (x, y)
        if y > 0 and field[x][y - 1] == -1:  # check top
            if debug: print("Move to {}, {}: Picking field close to opponent to the top".format(x + 1, y + 1))
            return (x, y)
        if y < 7 and field[x][y + 1] == -1:  # check bottom
            if debug: print("Move to {}, {}: Picking field close to opponent to the bottom".format(x + 1, y + 1))
            return (x, y)

    # 5. random move
    iRand = random.randrange(len(bestMoveList))
    if debug: print("Move to {}, {}: Random pick".format(bestMoveList[iRand][0] + 1, bestMoveList[iRand][1] + 1))
    return bestMoveList[iRand]


def createFlipMatrix(field):
    # create array holding the count of flips for each field
    flipMatrix = createMatrix()
    countFlips(field, flipMatrix)
    return flipMatrix


# Counts the possible flips for all free fields and stores them in the flipMatrix
def countFlips(field, flipMatrix):
    for x in range(8):
        for y in range(8):
            if flipMatrix[x][y] > -64:
                flipMatrix[x][y] += countFlipsForMove(field, x, y)


# count for each possible move, how many flips the opponent could reach
def countReturnFlips(field, flipMatrix, depth):
    for x in range(8):
        for y in range(8):
            if field[x][y] == 0 and flipMatrix[x][y] > -64:
                # make copy of the field in opponent view
                fieldCopy = copyFieldReversed(field)
                # make our move in the copy
                makeMove(fieldCopy, x, y, -1)
                # calculate the possible flips for the opponent on a board with the current move made
                moveMatrix = createFlipMatrix(fieldCopy)
                if depth > 0: moveMatrix = countReturnFlips(fieldCopy, moveMatrix, depth - 1)
                # subtract the maximum of possible opponent flips from our number of immediate flips
                flipMatrix[x][y] -= findMaxInMaxtrix(moveMatrix)
                # if depth % 2 != 0: flipMatrix[x][y] -= findMaxInMaxtrix(moveMatrix)
                # else: flipMatrix[x][y] -= avgValue(fieldCopy, moveMatrix)
    return flipMatrix


# check which free fields are most valuable for the opponent in terms of flips
def valueOpponentFlips(field, flipMatrix):
    fieldCopy = copyFieldReversed(field)
    opponentMatrix = createFlipMatrix(fieldCopy)
    for x in range(8):
        for y in range(8):
            oppVal = opponentMatrix[x][y]
            if oppVal < 0: oppVal = 0;  # limit to positive values
            # print ("Opponent value {}, {}: {}".format(x, y,  oppVal))
            flipMatrix[x][y] += oppVal
    return flipMatrix


# value fields next to other stones higher
def valuePlacement(field, flipMatrix):
    # evaluate neighboring fields
    corner = 2
    value = 1
    for x in range(8):
        for y in range(8):
            # check left
            # if x == 0: flipMatrix[x][y] += corner
            if x != 0 and field[x - 1][y] != 0: flipMatrix[x][y] += value
            # check right
            # if x == 7: flipMatrix[x][y] += corner
            if x != 7 and field[x + 1][y] != 0: flipMatrix[x][y] += value
            # check top
            # if y == 0: flipMatrix[x][y] += corner
            if y != 0 and field[x][y - 1] != 0: flipMatrix[x][y] += value
            # check top
            # if y == 7: flipMatrix[x][y] += corner
            if y != 7 and field[x][y + 1] != 0: flipMatrix[x][y] += value

    # corners on empty rows / columns
    for x in range(8):
        # if isColumnEmpty(field, x):
        flipMatrix[x][0] += corner
        flipMatrix[x][7] += corner

    for y in range(8):
        # if isRowEmpty(field, y):
        flipMatrix[0][y] += corner
        flipMatrix[7][y] += corner


# If there is an even number of free spaces in the row / column the fields get a penalty
def valueEvenSpaces(field, flipMatrix):
    penaltyEvenRows = 1
    bonusLastSpace = 2
    # evaluate rows
    for y in range(8):
        spaces = 0
        for x in range(8):
            if field[x][y] == 0: spaces += 1
        if spaces > 0 and spaces % 2 == 0:
            for x in range(8): flipMatrix[x][y] -= penaltyEvenRows
        if spaces == 1:
            for x in range(8): flipMatrix[x][y] += bonusLastSpace

    # evaluate columns
    for x in range(8):
        spaces = 0
        for y in range(8):
            if field[x][y] == 0: spaces += 1
        if spaces > 0 and spaces % 2 == 0:
            for y in range(8): flipMatrix[x][y] -= penaltyEvenRows
        if spaces == 1:
            for x in range(8): flipMatrix[x][y] += bonusLastSpace


# Moves clearing a row / column from opponent stones get a bonus
def valueStrategicValue(field, flipMatrix):
    value = 1
    for x in range(8):
        for y in range(8):
            if field[x][y] == 0 and flipMatrix[x][y] > -64:
                fail = 0
                # check left
                oppL = 0
                ownL = 0
                for ix in range(x):
                    if field[ix][y] == 1:
                        if oppL == 0: ownL = 1
                        else: fail = 1; break
                    if field[ix][y] == -1:
                        if ownL == 1: oppL = 1
                        else: fail = 1; break
                # check right
                oppR = 0
                ownR = 0
                for ix in range(7, x, -1):
                    if field[ix][y] == 1:
                        if oppR == 0: ownR = 1
                        else: fail = 1; break
                    if field[ix][y] == -1:
                        if ownR == 1: oppR = 1
                        else: fail = 1; break

                if fail == 0 and (oppR == 1 or oppL == 1): flipMatrix[x][y] += value

                # check top
                oppL = 0
                ownL = 0
                for iy in range(y):
                    if field[x][iy] == 1:
                        if oppL == 0: ownL = 1
                        else: fail = 1; break
                    if field[x][iy] == -1:
                        if ownL == 1: oppL = 1
                        else: fail = 1; break
                # check bottom
                oppR = 0
                ownR = 0
                for iy in range(7, y, -1):
                    if field[x][iy] == 1:
                        if oppR == 0: ownR = 1
                        else: fail = 1; break
                    if field[x][iy] == -1:
                        if ownR == 1: oppR = 1
                        else: fail = 1; break

                if fail == 0 and (oppR == 1 or oppL == 1): flipMatrix[x][y] += value


# count flips on the field if a move to x, y is made
# for occupied fields the function returns 0
def countFlipsForMove(field, x, y):
    # calculate flips only for free fields
    if field[x][y] != 0: return 0

    # variable for counting possible flips
    flips = 0

    # check for corner kill situations and score them higher
    cornerKillWeight = 8
    if x == 1 and y == 1 and field[0][0] == -1: flips += cornerKillWeight
    if x == 6 and y == 1 and field[7][0] == -1: flips += cornerKillWeight
    if x == 1 and y == 6 and field[0][7] == -1: flips += cornerKillWeight
    if x == 6 and y == 6 and field[7][7] == -1: flips += cornerKillWeight

    rangeLeft = range(x - 1, -1, -1)
    rangeRight = range(x + 1, 8, 1)
    rangeTop = range(y - 1, -1, -1)
    rangeBottom = range(y + 1, 8, 1)

    otherInRow = 0
    for ix in rangeLeft:
        if field[ix][y] == -1:  # other
            otherInRow += 1
        elif field[ix][y] == 1:  # own stone - all other stones encountered until here will flip
            flips += otherInRow
            break

    otherInRow = 0
    for ix in rangeRight:
        if field[ix][y] == -1:  # other
            otherInRow += 1
        elif field[ix][y] == 1:  # own stone - all other stones encountered until here will flip
            flips += otherInRow
            break

    otherInRow = 0
    for iy in rangeTop:
        if field[x][iy] == -1:  # other
            otherInRow += 1
        elif field[x][iy] == 1:  # own stone - all other stones encountered until here will flip
            flips += otherInRow
            break

    otherInRow = 0
    for iy in rangeBottom:
        if field[x][iy] == -1:  # other
            otherInRow += 1
        elif field[x][iy] == 1:  # own stone - all other stones encountered until here will flip
            flips += otherInRow
            break

    return flips


# make a move to the space at x, y in field
# flip all opponent stones like the game does
def makeMove(field, x, y, self=1):
    # print("Before make move")
    # printMatrix(field, createMatrix())
    # illegal move
    if field[x][y] != 0:
        print("Error: illegal move ")
        return 0

    other = -1
    if self == other: other = 1

    # check for corner kills
    if x == 1 and y == 1 and field[0][0] == other: field[0][0] = self
    if x == 6 and y == 1 and field[7][0] == other: field[7][0] = self
    if x == 1 and y == 6 and field[0][7] == other: field[0][7] = self
    if x == 6 and y == 6 and field[7][7] == other: field[7][7] = self

    # flips to the left
    otherInRow = 0
    for ix in range(x - 1, -1, -1):
        if field[ix][y] == other:
            otherInRow = 1
        elif field[ix][y] == self:  # own stone - all other stones encountered until here will flip
            if otherInRow:
                for ix in range(x - 1, -1, -1):  # flip
                    if field[ix][y] == other: field[ix][y] = self
                    elif field[ix][y] == self: break
            break

    # flips to the right
    otherInRow = 0
    for ix in range(x + 1, 8, 1):
        if field[ix][y] == other:
            otherInRow = 1
        elif field[ix][y] == self:  # own stone - all other stones encountered until here will flip
            if otherInRow:
                for ix in range(x + 1, 8, 1):  # flip
                    if field[ix][y] == other: field[ix][y] = self
                    elif field[ix][y] == self: break
            break

    # flips to the top
    otherInRow = 0
    for iy in range(y - 1, -1, -1):
        if field[x][iy] == other:
            otherInRow = 1
        elif field[x][iy] == self:  # own stone - all other stones encountered until here will flip
            if otherInRow:
                for iy in range(y - 1, -1, -1):  # flip
                    if field[x][iy] == other: field[x][iy] = self
                    elif field[x][iy] == self: break
            break

    # flips to the bottom
    otherInRow = 0
    for iy in range(y + 1, 8, 1):
        if field[x][iy] == other:
            otherInRow = 1
        elif field[x][iy] == self:  # own stone - all other stones encountered until here will flip
            if otherInRow:
                for iy in range(y + 1, 8, 1):  # flip
                    if field[x][iy] == other: field[x][iy] = self
                    elif field[x][iy] == self: break
            break
    # finally plac stone
    field[x][y] = self
    # print("After make move")
    # printMatrix(field, createMatrix())


def createMatrix(initialValue=0):
    matrix = []
    for x in range(8):
        matrix.append([])
        for y in range(8):
            matrix[x].append(initialValue)
    return matrix


def copyField(field):
    copy = []
    for x in range(8):
        copy.append([])
        for y in range(8):
            copy[x].append(field[x][y])
    return copy


def copyFieldReversed(field):
    copy = []
    for x in range(8):
        copy.append([])
        for y in range(8):
            copy[x].append(-1 * field[x][y])
    return copy


def findMaxInMaxtrix(matrix):
    max = -64 * 64  # TODO something like Int.min
    for x in range(8):
        for y in range(8):
            if matrix[x][y] > max:
                max = matrix[x][y]
    return max


# put the value of all occupied fields to -64 in the matrix
def maskOccupiedFields(field, matrix):
    max = -64 * 64  # TODO something like Int.min
    for x in range(8):
        for y in range(8):
            if field[x][y] != 0:
                matrix[x][y] = -64


# print the specified field and value matrix to console
def printMatrix(field, matrix):
    for y in range(8):
        value = []
        for x in range(8):
            value.append(matrix[x][y])
            if field[x][y] == 1: value[x] = "ooo"
            if field[x][y] == -1: value[x] = "xxx"
        print("{0:3} {1:3} {2:3} {3:3} {4:3} {5:3} {6:3} {7:3}".format(value[0], value[1], value[2], value[3], value[4],
                                                                       value[5], value[6], value[7]))


def getBestMoves(matrix):
    # Assemble list of best moves according to the matrix
    bestMoveList = []
    maxFlips = findMaxInMaxtrix(matrix)
    for x in range(8):
        for y in range(8):
            if matrix[x][y] == maxFlips:
                bestMoveList.append((x, y))
    return bestMoveList


# only leaves the maximum entries unchanged - all other values will be set to -64
def filterBestValues(matrix):
    maxFlips = findMaxInMaxtrix(matrix)
    for x in range(8):
        for y in range(8):
            if matrix[x][y] != maxFlips: matrix[x][y] = -64


def isColumnEmpty(field, x):
    foundStone = 0
    for y in range(8):
        if field[x][y] != 0:
            foundStone = 1
            break
    return foundStone == 0


def isRowEmpty(field, y):
    foundStone = 0
    for x in range(8):
        if field[x][y] != 0:
            foundStone = 1
            break
    return foundStone == 0