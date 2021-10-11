import random

board = []
symbol = ''


def turn(board_arg, symbol_arg):
   global board
   board = board_arg
   global symbol
   symbol = symbol_arg

   # when I can flip all opponent's stones
   if new_stones(max_stones()[0], max_stones()[1]) > stone_count_opp():
       return max_stones()

   ret = corner()
   if ret:
       return ret

   return optimum()


def is_empty(x, y):
   return board[y][x] == '#'


def is_own(x, y):
   return board[y][x] == symbol


def is_opponent(x, y):
   return not (is_own(x, y) | is_empty(x, y))


def stone_count_own():
   count = 0
   for i in range(8):
       for j in range(8):
           if is_own(i, j):
               count += 1
   return count


def stone_count_opp():
   count = 0
   for i in range(8):
       for j in range(8):
           if is_opponent(i, j):
               count += 1
   return count


def corner():
   # do a corner kill if possible
   ret = corner_kill()
   if ret:
       return ret

   # place in corner if safe
   ret = place_corner()
   if ret:
       return ret

   # make a corner safe
   ret = safe_corner()
   if ret:
       return ret

   return False


# do a corner kill if possible
def corner_kill():
   if is_opponent(0, 0) & is_empty(1, 1):
       return 1, 1  # upper left
   if is_opponent(7, 0) & is_empty(6, 1):
       return 6, 1  # upper right
   if is_opponent(0, 7) & is_empty(1, 6):
       return 1, 6  # lower left
   if is_opponent(7, 7) & is_empty(6, 6):
       return 6, 6  # lower right
   return False     # if no corner kill possible


# place in corner if safe
def place_corner():
   if (not is_empty(1, 1)) & is_empty(0, 0):
       return 0, 0  # upper left
   if (not is_empty(6, 1)) & is_empty(7, 0):
       return 7, 0  # upper right
   if (not is_empty(1, 6)) & is_empty(0, 7):
       return 0, 7  # lower left
   if (not is_empty(6, 6)) & is_empty(7, 7):
       return 7, 7  # lower right
   return False     # if no corner is safe


# make a corner safe
def safe_corner():
   if is_empty(1, 1):
       return 1, 1  # upper left
   if is_empty(6, 1):
       return 6, 1  # upper right
   if is_empty(1, 6):
       return 1, 6  # lower left
   if is_empty(6, 6):
       return 6, 6  # lower right
   return False     # if no corner can be made safe


def optimum():
   me_max_stones = max_stones()
   me_new_stones_max = new_stones(me_max_stones[0], me_max_stones[1])
   opp_max_stones = max_stones_opp()
   opp_new_stones_max = new_stones_opp(opp_max_stones[0], opp_max_stones[1])
   i_opp_max_stones = i_max_stones_opp(me_max_stones[0], me_max_stones[1])
   i_board = board
   i_board[me_max_stones[1]][me_max_stones[0]] = symbol

   if me_new_stones_max < opp_new_stones_max:
       if opp_new_stones_max <= i_opp_max_stones:
           return opp_max_stones

   return me_max_stones


# where can I get most new stones
def max_stones():
   pos = 0, 0
   stones = 0
   for i in range(8):
       for j in range(8):
           current = new_stones(i, j)
           if current > stones:
               pos = i, j
               stones = current
   return pos


# where can my opponent get most new stones
def max_stones_opp():
   pos = 0, 0
   stones = 0
   for i in range(8):
       for j in range(8):
           current = new_stones_opp(i, j)
           if current > stones:
               pos = i, j
               stones = current
   return pos


# how many new stones would I win with x, y
def new_stones(x, y):
   if not is_empty(x, y):
       return 0

   stones = 1
   opp_stones = 0

   # to the right
   for i in range(x+1, 8):
       if is_opponent(i, y):
           opp_stones += 1
       elif is_own(i, y):
           stones += opp_stones
           break
   opp_stones = 0

   # to the left
   for i in range(x-1, -1, -1):
       if is_opponent(i, y):
           opp_stones += 1
       elif is_own(i, y):
           stones += opp_stones
           break
   opp_stones = 0

   # downward
   for i in range(y+1, 8):
       if is_opponent(x, i):
           opp_stones += 1
       elif is_own(x, i):
           stones += opp_stones
           break
   opp_stones = 0

   # upward
   for i in range(y-1, -1, -1):
       if is_opponent(x, i):
           opp_stones += 1
       elif is_own(x, i):
           stones += opp_stones
           break

   # corner cut
   if (x == 1 & y == 1) & is_opponent(0, 0):
       stones += 1
   elif (x == 6 & y == 1) & is_opponent(7, 0):
       stones += 1
   elif (x == 1 & y == 6) & is_opponent(0, 7):
       stones += 1
   elif (x == 6 & y == 6) & is_opponent(7, 7):
       stones += 1

   return stones


# how many new stones would my opponent win with x, y
def new_stones_opp(x, y):
   if not is_empty(x, y):
       return 0

   stones = 1
   own_stones = 0

   # to the right
   for i in range(x+1, 8):
       if is_own(i, y):
           own_stones += 1
       elif is_opponent(i, y):
           stones += own_stones
           break
   own_stones = 0

   # to the left
   for i in range(x-1, -1, -1):
       if is_own(i, y):
           own_stones += 1
       elif is_opponent(i, y):
           stones += own_stones
           break
   own_stones = 0

   # downward
   for i in range(y+1, 8):
       if is_own(x, i):
           own_stones += 1
       elif is_opponent(x, i):
           stones += own_stones
           break
   own_stones = 0

   # upward
   for i in range(y-1, -1, -1):
       if is_own(x, i):
           own_stones += 1
       elif is_opponent(x, i):
           stones += own_stones
           break

   # corner cut
   if (x == 1 & y == 1) & is_own(0, 0):
       stones += 1
   elif (x == 6 & y == 1) & is_own(7, 0):
       stones += 1
   elif (x == 1 & y == 6) & is_own(0, 7):
       stones += 1
   elif (x == 6 & y == 6) & is_own(7, 7):
       stones += 1

   return stones


# how many new stones could my opponent get if I placed on x, y
def i_max_stones_opp(x, y):
   i_board = board
   i_board[x][y] = symbol
   stones = 0
   for i in range(8):
       for j in range(8):
           current = i_new_stones_opp(i_board, i, j)
           if current > stones:
               stones = current
   return stones


# how many new stones would my opponent win with x, y on board i_board
# (quick and very dirty)
def i_new_stones_opp(i_board, x, y):
   if not i_board[y][x] == '#':
       return 0

   stones = 1
   own_stones = 0

   # to the right
   for i in range(x+1, 8):
       if i_board[y][i] == symbol:
           own_stones += 1
       elif (i_board[y][i] != symbol) & (i_board[y][i] != '#'):
           stones += own_stones
           break
   own_stones = 0

   # to the left
   for i in range(x-1, -1, -1):
       if i_board[y][i] == symbol:
           own_stones += 1
       elif (i_board[y][i] != symbol) & (i_board[y][i] != '#'):
           stones += own_stones
           break
   own_stones = 0

   # downward
   for i in range(y+1, 8):
       if i_board[i][x] == symbol:
           own_stones += 1
       elif (i_board[i][x] != symbol) & (i_board[i][x] != '#'):
           stones += own_stones
           break
   own_stones = 0

   # upward
   for i in range(y-1, -1, -1):
       if i_board[i][x] == symbol:
           own_stones += 1
       elif (i_board[i][x] != symbol) & (i_board[i][x] != '#'):
           stones += own_stones
           break

   # corner cut
   if (x == 1 & y == 1) & (i_board[0][0] == symbol):
       stones += 1
   elif (x == 6 & y == 1) & (i_board[0][7] == symbol):
       stones += 1
   elif (x == 1 & y == 6) & (i_board[7][0] == symbol):
       stones += 1
   elif (x == 6 & y == 6) & (i_board[7][7] == symbol):
       stones += 1

   return stones


# set at random position
def rdm():
   while 1:
       x = random.choice(range(8))
       y = random.choice(range(8))
       if is_empty(x, y):
           return x, y