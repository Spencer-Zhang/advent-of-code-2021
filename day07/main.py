from collections import defaultdict
from copy import copy

# with open('example.txt') as f:
with open('input.txt') as f:
  input_lines = f.readlines()

crabs = map(int, input_lines[0].strip().split(","))


best_position = None
best_fuel = None

def fuel_cost(length):
  return (length) * (length+1) / 2

for i in range(min(crabs), max(crabs)):
  fuel = sum(fuel_cost(abs(i - c)) for c in crabs)
  if fuel < best_fuel or best_fuel == None:
    best_fuel = fuel
    best_position = i

print best_fuel, best_position
