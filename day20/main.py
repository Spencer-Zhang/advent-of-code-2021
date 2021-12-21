from collections import defaultdict
from copy import copy

# with open('example.txt') as f:
with open('input.txt') as f:
  input_lines = f.readlines()

  algorithm = input_lines.pop(0).strip()
  input_lines.pop(0)

  grid = [line.strip() for line in input_lines]


n_rows = len(grid)
n_columns = len(grid[0])

def read_pixel(grid, row, col, default):
  if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
    return default
  elif grid[row][col] == ".":
    return 0
  elif grid[row][col] == "#":
    return 1
  else:
    raise

def enhance_pixel(grid, row, col, default):
  global algorithm
  n = 0
  for r in range(row-1, row+2):
    for c in range(col-1, col+2):
      n = 2*n + read_pixel(grid, r, c, default)
  return n


# Enhance the image once
for i in range(50):
  n_rows += 2
  n_columns += 2
  next_grid = []

  for r in range(n_rows):
    next_row = ""
    for c in range(n_columns):
      next_row += algorithm[enhance_pixel(grid,r-1,c-1, i%2)]
    next_grid.append(next_row)
  grid = next_grid
  for row in next_grid:
    print row

print len("".join(grid).replace('.', ''))
