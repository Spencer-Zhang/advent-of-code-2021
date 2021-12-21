from collections import defaultdict

cave_map = {}

with open('example.txt') as f:
  for line in f.readlines():
    nodes = line.strip().split("-")
    for node in nodes:
      if not node in cave_map:
        cave_map[node] = []
    cave_map[nodes[0]].append(nodes[1])
    cave_map[nodes[1]].append(nodes[0])

def find_next_paths(visited, current_node, revisited, finished_paths):
  if current_node == "end":
    finished_paths.append(current_node)
    return []

  next_nodes = cave_map[current_node]
  next_paths = []

  for n in next_nodes:
    if n == "start":
      continue

    next_visited = set(visited)
    next_visited.add(n)

    if n == n.lower():
      if not revisited:
        next_paths.append((next_visited, n, n in visited))
      else:
        if n in visited:
          continue
        else:
          next_paths.append((next_visited, n, True))
    else:
      next_paths.append((next_visited, n, visited))
  return next_paths

finished_paths = []

paths = [(set(), "start", False)]
while len(paths) > 0:
  visited, current_node, revisited = paths.pop(0)
  paths += find_next_paths(visited, current_node, revisited, finished_paths)

# print cave_map
print len(finished_paths)
# for path in finished_paths:
#   print path