lines = []
n_flashes = 0

def printlines():
  for line in lines:
    print line
  print "-----------"

with open('input.txt') as f:
  for line in f.readlines():
    lines.append([int(c) for c in line.strip()])


flashes = []

def energize(r, c):
  if r < 0 or r > 9 or c < 0 or c > 9:
    return
  else:
    lines[r][c] += 1
    if lines[r][c] == 10:
      flashes.append((r,c))

def spread(r, c):
  energize(r-1, c-1)
  energize(r-1, c)
  energize(r-1, c+1)
  energize(r, c-1)
  energize(r, c+1)
  energize(r+1, c-1)
  energize(r+1, c)
  energize(r+1, c+1)


printlines()

def iterate(i):
  n = 0
  # Increase the energy level of each spot by 1
  for r in range(10):
    for c in range(10):
      energize(r,c)

  # For each new flash, energize all cells around it.
  while len(flashes) > 0:
    flash = flashes.pop()
    spread(flash[0], flash[1])

  # Reduce all cells that have flashed to zero
  for r in range(10):
    for c in range(10):
      if lines[r][c] > 9:
        n += 1
        lines[r][c] = 0
  return n

for i in range(500):
  n = iterate(i)
  if n == 100:
    print i + 1

  n_flashes += n
print n_flashes

