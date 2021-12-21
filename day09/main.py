from collections import defaultdict
from copy import copy


# with open('example.txt') as f:
with open('input.txt') as f:
  input_lines = f.readlines()
  grid = [map(int, line.strip()) for line in input_lines]

# Find all the low_points in the grid
low_points = []
def read_grid(grid, row, col, default):
  if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
    return default
  return grid[row][col]
for r in range(len(grid)):
  for c in range(len(grid[0])):
    adj = set()
    adj.add(read_grid(grid, r-1, c, 99))
    adj.add(read_grid(grid, r+1, c, 99))
    adj.add(read_grid(grid, r, c-1, 99))
    adj.add(read_grid(grid, r, c+1, 99))
    if grid[r][c] < min(adj):
      low_points.append((r, c))

# Search algorithm to assign an basin id to each point in the grid
search_queue = []
basin_grid = {}
for i in range(len(low_points)):
  point = low_points[i]
  basin_grid[point] = i
  search_queue.append(point)
while len(search_queue) > 0:
  point = search_queue.pop(0)
  basin_id = basin_grid[point]
  for v in [(1,0), (-1,0), (0, 1), (0,-1)]:
    next_point = (point[0] + v[0], point[1] + v[1])
    if next_point in basin_grid:
      continue
    if read_grid(grid, next_point[0], next_point[1], 9) < 9:
      search_queue.append(next_point)
      basin_grid[next_point] = basin_id

area_count = defaultdict(int)
for point in basin_grid:
  area_count[basin_grid[point]] += 1

print area_count
print sorted(area_count.values())
print reduce(lambda x, y: x*y, sorted(area_count.values())[-3:])