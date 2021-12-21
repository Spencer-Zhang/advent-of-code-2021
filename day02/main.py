with open('input.txt') as f:
  instructions = [s.split() for s in f.readlines()]

x = 0
depth = 0
aim = 0

for command, length in instructions:
  if command == "forward":
    x += int(length)
    depth += aim * int(length)
  elif command == "up":
    aim -= int(length)
  elif command == "down":
    aim += int(length)

print x * depth