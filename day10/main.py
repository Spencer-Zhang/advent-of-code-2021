
MATCHING = {
  "{": "}",
  "[": "]",
  "(": ")",
  "<": ">"
}

VALUES = {
  ")": 3,
  "]": 57,
  "}": 1197,
  ">": 25137
}

COMPLETION_POINTS = {
  "(": 1,
  "[": 2,
  "{": 3,
  "<": 4
}

points = 0


def check(line):
  global points
  stack = []
  for c in line:
    if c in MATCHING.keys():
      stack.append(c)
    elif c in MATCHING.values():
      if MATCHING[stack[-1]] == c:
        stack.pop()
      else:
        points += VALUES[c]
        return 0
    else:
      raise

  incomplete = 0
  while len(stack) > 0:
    incomplete = 5 * incomplete + COMPLETION_POINTS[stack.pop(-1)]
  return incomplete

with open('input.txt') as f:
  inc_list = []
  for line in f.readlines():
    inc = check(line.strip())
    if inc > 0:
      inc_list.append(inc)
  inc_list = sorted(inc_list)
  print inc_list[(len(inc_list) - 1) / 2]
