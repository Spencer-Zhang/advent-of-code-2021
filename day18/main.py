from collections import defaultdict
from copy import copy

# with open('example.txt') as f:
with open('input.txt') as f:
  input_lines = f.readlines()



class FishPair:
  def __init__(self, value, depth):
    self.value = value
    self.depth = depth

  def __repr__(self):
    return "(" + str(self.value) + " " + str(self.depth) + ")"

class FishNumber:
  def __init__(self, input_string):
    self.numbers = []
    depth = 0
    # parse input string:
    input_list = list(input_string)
    while len(input_list) > 0:
      c = input_list.pop(0)
      if c.isdigit():
        n = int(c)
        while input_string[0].isdigit():
          n = 10 * n + int(input_string.pop(0))
        self.numbers.append(FishPair(n, depth))
      elif c == "[":
        depth += 1
      elif c == "]":
        depth -= 1

  def add(self, next):
    self.numbers += next.numbers
    for n in self.numbers:
      n.depth += 1
    self.reduce()
    return self

  def get_magnitude(self):
    max_depth = max([fn.depth for fn in self.numbers])
    numbers = copy(self.numbers)

    while max_depth > 0:
      ie = None
      for i in range(len(numbers)):
        if numbers[i].depth == max_depth:
          ie = i
          break
      if ie != None:
        if numbers[ie + 1].depth != max_depth:
          raise
        n1 = numbers[ie].value
        n2 = numbers.pop(ie + 1).value
        numbers[ie].value = 3*n1 + 2*n2
        numbers[ie].depth -= 1
        continue
      max_depth -= 1
    return numbers[0].value

  def reduce(self):
    while True:
      # Find the left-most pair of numbers with depth > 4
      ie = None
      for i in range(len(self.numbers)):
        if self.numbers[i].depth > 4:
          ie = i
          break
      if ie != None:
        # print "Exploding number at index",  ie
        if ie - 1 >= 0:
          self.numbers[ie - 1].value += self.numbers[ie].value
        if ie + 2 < len(self.numbers):
          self.numbers[ie + 2].value += self.numbers[ie + 1].value
        self.numbers.pop(ie)
        self.numbers[ie].value = 0
        self.numbers[ie].depth -= 1
        # print self.numbers
        continue

      # Find the left-most pair of numbers with value >= 10
      ie = None
      for i in range(len(self.numbers)):
        if self.numbers[i].value >= 10:
          ie = i
          break
      if ie != None:
        # print "Splitting number at index", ie
        self.numbers.insert(ie + 1, copy(self.numbers[ie]))
        self.numbers[ie].value = self.numbers[ie].value / 2
        self.numbers[ie].depth += 1
        self.numbers[ie+1].value = (self.numbers[ie+1].value + 1) / 2
        self.numbers[ie+1].depth += 1
        # print self.numbers
        continue

      break

# Part 1:
# number = FishNumber(input_lines.pop(0))
# while len(input_lines) > 0:
#   number.add(FishNumber(input_lines.pop(0)))

# Part 2:
max_magnitude = 0

n_numbers = len(input_lines)
for i in range(n_numbers):
  for j in range(n_numbers):
    print "Trying", i, j
    if i == j:
      continue

    n1 = FishNumber(input_lines[i])
    n2 = FishNumber(input_lines[j])
    magnitude = n1.add(n2).get_magnitude()
    if magnitude > max_magnitude:
      max_magnitude = magnitude

print max_magnitude
