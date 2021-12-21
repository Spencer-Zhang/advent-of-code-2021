# Code for Part 1
# Part 2 ended up being something so different that I just ended up writing new code.

from collections import defaultdict
from copy import copy

positions = []
with open('example.txt') as f:
# with open('input.txt') as f:
  input_lines = f.readlines()
  for line in input_lines:
    positions.append(int(line.strip().split(" ")[-1]))

class Dice:
  def __init__(self):
    self.last_roll = 100
    self.n_rolls = 0

  def roll(self):
    self.last_roll += 1
    if self.last_roll > 100:
      self.last_roll = 1
    self.n_rolls += 1
    return self.last_roll

dice = Dice()

current_player = 1
points = [0, 0]
while True:
  current_player = 1 - current_player
  for i in range(3):
    positions[current_player] += dice.roll()
  
  positions[current_player] = ((positions[current_player] - 1) % 10) + 1
  points[current_player] += positions[current_player]
  if points[current_player] >= 1000:
    break

print points[1 - current_player] * dice.n_rolls