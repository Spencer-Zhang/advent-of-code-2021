with open('input.txt') as f:
  lines = [int(s) for s in f.readlines()]

sliding = []
for i in range(len(lines) - 2):
  sliding.append(lines[i] + lines[i+1] + lines[i+2])

print sliding

n = 0
for i in range(len(sliding) - 1):
  if sliding[i] < sliding[i+1]:
    n += 1

print n