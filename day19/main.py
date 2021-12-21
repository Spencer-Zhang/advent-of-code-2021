import random
from collections import defaultdict
from copy import copy

ROTATIONS = [
    (-3, -1, 2), (1, -2, -3), (-3, -2, -1),
    (3, -2, 1), (-1, -3, -2), (2, -3, -1),
    (-2, -1, -3), (2, 3, 1), (-1, 2, -3),
    (1, -3, 2), (2, 1, -3), (3, 2, -1),
    (3, 1, 2), (-1, 3, 2), (1, 2, 3),
    (-3, 1, -2), (2, -1, 3), (-2, 1, 3),
    (-1, -2, 3), (-2, 3, -1), (-2, -3, 1),
    (-3, 2, 1), (1, 3, -2), (3, -1, -2)]

class Scanner:
  def __init__(self, beacons):
    self.beacons = copy(beacons)
    self.rotated = copy(beacons)
    self.rotation = None
    self.offset = None

  def apply_rotation(self, rotation):
    self.rotation = rotation
    self.rotated = []
    for beacon in self.beacons:
      next_beacon = []
      for i in range(3):
        next_beacon.append(beacon[abs(rotation[i])-1] * (rotation[i]/abs(rotation[i])))
      self.rotated.append(next_beacon)

  def apply_offset(self, offset):
    self.offset = offset
    for beacon in self.rotated:
      beacon[0] += offset[0]
      beacon[1] += offset[1]
      beacon[2] += offset[2]

  def find_overlaps(self, scanner2):
    global ROTATIONS
    for rotation in ROTATIONS:
      scanner2.apply_rotation(rotation)
      for i in range(len(self.rotated)):
        ref_beacon = self.rotated[i]
        base_coords = set()
        for beacon in self.rotated:
          base_coords.add((beacon[0] - ref_beacon[0], beacon[1] - ref_beacon[1], beacon[2] - ref_beacon[2]))
        for j in range(len(scanner2.rotated)):
          ref_beacon = scanner2.rotated[j]
          coords = copy(base_coords)
          for beacon in scanner2.rotated:
            coords.add((beacon[0] - ref_beacon[0], beacon[1] - ref_beacon[1], beacon[2] - ref_beacon[2]))
          n_overlaps = len(self.beacons) + len(scanner2.beacons) - len(coords)
          if n_overlaps >= 12:
            base_ref = self.rotated[i]
            target_ref = scanner2.rotated[j]
            offset = [base_ref[0] - target_ref[0], base_ref[1] - target_ref[1], base_ref[2] - target_ref[2]]
            scanner2.apply_offset(offset)
            return True
    return False




# with open('example.txt') as f:
with open('input.txt') as f:
  input_lines = f.readlines()

  pending_beacons = []
  scanners = []

  while len(input_lines) > 0:
    next_line = input_lines.pop(0).strip()
    if len(next_line) == 0:
      continue
    elif next_line[0:2] == "--":
      if len(pending_beacons) > 0:
        scanners.append(Scanner(pending_beacons))
        pending_beacons = []
    else:
      coords = map(int, next_line.split(","))
      pending_beacons.append(coords)
  if len(pending_beacons) > 0:
    scanners.append(Scanner(pending_beacons))

solved_scanners = [0]
solved_index = 0

# Use Scanner 0's position and rotation as the point of reference for all other scanners
scanners[0].rotation = (1,2,3)
scanners[0].offset = [0,0,0]

while solved_index < len(solved_scanners):
  print solved_index
  current = solved_scanners[solved_index]

  for i in range(len(scanners)):
    if i in solved_scanners:
      continue
    if scanners[current].find_overlaps(scanners[i]):
      solved_scanners.append(i)
  solved_index += 1

if len(solved_scanners) < len(scanners):
  raise "Couldn't solve for all scanners"


coords = set()

offsets = []

for scanner in scanners:
  for beacon in scanner.rotated:
    coords.add((beacon[0], beacon[1], beacon[2]))
  offsets.append(scanner.offset)
print len(coords)
print offsets

max_distance = 0
for i in offsets:
  for j in offsets:
    distance = 0
    for k in range(3):
      distance += abs(i[k] - j[k])
    if distance > max_distance:
      max_distance = distance
print max_distance