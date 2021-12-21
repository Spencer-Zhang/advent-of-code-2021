# from collections import defaultdict
# from copy import copy

# with open('example.txt') as f:
#   input_lines = f.readlines()

# input: target area: x=236..262, y=-78..-58
# experiment: target area: x=20..30, y=-10..-5

target_x = (236, 262)
target_y = (-78, -58)

# target_x = (20, 30)
# target_y = (-10, -5)

def is_valid_velocity(dx0, dy0):
  global target_x
  global target_y

  x = 0;
  y = 0;
  dx = dx0;
  dy = dy0;

  while True:
    x += dx
    y += dy
    if dx > 0:
      dx -= 1
    dy -= 1

    if x > target_x[1] or y < target_y[0]:
      return False
    elif x >= target_x[0] and y <= target_y[1]:
      return True

total = 0
for dx0 in range(1, 263):
  for dy0 in range(-78, 78):
    if is_valid_velocity(dx0, dy0):
      print (dx0, dy0)
      total += 1
print total