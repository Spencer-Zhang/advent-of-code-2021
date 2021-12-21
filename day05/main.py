import fractions
from collections import defaultdict
from copy import copy

lines = []

class Line:
  def __init__(self, input_string):
    self.input_string = input_string.strip()
    inputs = input_string.strip().split()
    start = map(int, inputs[0].split(","))
    end = map(int, inputs[2].split(","))

    self.start = (start[0], start[1])
    self.end = (end[0], end[1])
    self.vector = self.get_vector()

  def is_horizontal(self):
    return self.start[0] == self.end[0]

  def is_vertical(self):
    return self.start[1] == self.end[1]

  def contains_point(self, point):
    x, y = point
    return abs(self.start[0] - x) + abs(self.end[0] - x) == abs(self.start[0]-self.end[0]) and abs(self.start[1] - y) + abs(self.end[1] - y) == abs(self.start[1]-self.end[1])

  def get_vector(self):
    dx = self.end[0] - self.start[0]
    dy = self.end[1] - self.start[1]
    if dx == 0:
      return (0, dy/abs(dy))
    elif dy == 0:
      return (dx/abs(dx), 0)
    else:
      gcd = abs(fractions.gcd(dx, dy))
      return (dx/gcd, dy/gcd)

  def get_points(self):
    i = self.start
    points = set()
    points.add(i)
    while True:
      i = (i[0] + self.vector[0], i[1] + self.vector[1])
      points.add(i)
      if i == self.end:
        break
    return points
    

  def __str__(self):
    return self.input_string

lines = []
intersections = set()

# with open('example.txt') as f:
with open('input.txt') as f:
  input_lines = f.readlines()

  for line in input_lines:
    newline = Line(line)
    # if newline.is_horizontal() or newline.is_vertical():
    lines.append(newline)


for i in range(len(lines)):
  for j in range(i + 1, len(lines)):
    # print lines[i], " ", lines[j], " ", lines[i].get_points().intersection(lines[j].get_points())
    for k in lines[i].get_points().intersection(lines[j].get_points()):
      intersections.add(k)

print len(intersections)

    