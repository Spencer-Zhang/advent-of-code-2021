WINNING_TARGET = 21

positions = []
# with open('example.txt') as f:
with open('input.txt') as f:
  input_lines = f.readlines()
  for line in input_lines:
    positions.append(int(line.strip().split(" ")[-1]))

# dp[(x,y,z)] is the number of universes in which a player can get x points in y turns, ending on board position z.
dp_list = [{}, {}]

for i in range(2):
  dp_list[i][(0, 0, positions[i])] = 1

def board_modulus(n):
  return ((n - 1) % 10) + 1

# Return the number of universes in which the next 3 rolls add up to n
def comb(n):
  if n == 3:
    return 1
  if n == 4:
    return 3
  if n == 5:
    return 6
  if n == 6:
    return 7
  if n == 7:
    return 6
  if n == 8:
    return 3
  if n == 9:
    return 1
  else:
    return 0

# Get the number of ways player i can have j points by turn k
def get_dp(player, n_points, n_turns):
  return sum([get_dp_internal(player, n_points, n_turns, i) for i in range(1, 11)])

# Get the number of ways player i can have j points by turn k, while ending at ending position m
def get_dp_internal(player, n_points, n_turns, ending_position):
  global dp_list
  dp = dp_list[player]
  if ending_position != board_modulus(ending_position):
    raise
  if (n_points, n_turns, ending_position) in dp:
    return dp[n_points, n_turns, ending_position]
  elif n_points <= 0 or n_turns <= 0:
    return 0
  else:
    n_possibilities = 0
    for roll in range(3, 10):
      n_possibilities += comb(roll) * get_dp_internal(player, n_points - ending_position, n_turns - 1, board_modulus(ending_position - roll))
    dp[n_points, n_turns, ending_position] = n_possibilities
    return n_possibilities

# Number of ways for player X to win on the Nth turn.
def possible_ways_to_win_on_nth_turn(player, n_turns):
  total = 0
  for starting_points in range(WINNING_TARGET - 10, WINNING_TARGET):
    if starting_points < 0:
      continue
    for roll in range(3, 11):
      for starting_position in range(1, 11):
        ending_position = board_modulus(starting_position + roll)
        ending_points = starting_points + ending_position
        if ending_points < WINNING_TARGET:
          continue
        total += comb(roll) * get_dp_internal(player, starting_points, n_turns - 1, starting_position)
  return total

# Number of ways for player X to get to turn Y without earning enough points to win
def possible_ways_to_not_win_by_nth_turn(player, n_turns):
  total = 0
  for i in range(0, WINNING_TARGET):
    total += get_dp(player, i, n_turns)
  return total

total = 0
for i in range(20):
  total += possible_ways_to_win_on_nth_turn(0, i) * possible_ways_to_not_win_by_nth_turn(1, i-1)
print total

total2 = 0
for i in range(20):
  total2 += possible_ways_to_win_on_nth_turn(1, i) * possible_ways_to_not_win_by_nth_turn(0, i)
print total2
