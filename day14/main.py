from collections import defaultdict

# with open('example.txt') as f:
with open('input.txt') as f:
  input_lines = f.readlines()

  polymer = input_lines.pop(0).strip()
  input_lines.pop(0)

  instructions = {}
  while len(input_lines) > 0:
    next_line = input_lines.pop(0).strip().split(" -> ")
    instructions[next_line[0]] = next_line[1]

for i in range(40):
  print i
  next_polymer = ""

  for x in range(len(polymer) - 1):
    next_polymer += polymer[x]
    if polymer[x:x+2] in instructions:
      next_polymer += instructions[polymer[x:x+2]]
  next_polymer += polymer[-1]
  polymer = next_polymer

c_count = defaultdict(int)
for c in polymer:
  c_count[c] += 1

most_common = c_count.keys()[0]
least_common = c_count.keys()[0]


print(c_count)
for c in c_count.keys():
  if c_count[c] > c_count[most_common]:
    most_common = c
  if c_count[c] < c_count[least_common]:
    least_common = c

print most_common
print least_common
print c_count[most_common] - c_count[least_common]