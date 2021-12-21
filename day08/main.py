from collections import defaultdict
from copy import copy

# with open('example.txt') as f:
with open('input.txt') as f:
  input_lines = f.readlines()

total = 0


LENGTH_TO_DIGIT = {
  2: 1,
  3: 7,

  #5: 2,3,5
  #6: 6,9, 0
  4: 4,
  7: 8,
}

def alphasort(string):
  return "".join(sorted(string))

def decode_patterns(patterns):
  decoded = {}
  digit_count = defaultdict(int)
  for pattern in patterns:
    for c in pattern:
      digit_count[c] += 1
    if len(pattern) in LENGTH_TO_DIGIT:
      decoded[pattern] = LENGTH_TO_DIGIT[len(pattern)]

  for char in digit_count:
    if digit_count[char] == 6:
      char_b = char
    elif digit_count[char] == 4:
      char_e = char
    elif digit_count[char] == 9:
      char_f = char

  for pattern in patterns:
    if len(pattern) == 5:
      if char_b in pattern:
        decoded[pattern] = 5
        decoded[alphasort(pattern + char_e)] = 6
      elif char_e in pattern:
        decoded[pattern] = 2
      else:
        decoded[pattern] = 3
  for pattern in patterns:
    if pattern in decoded:
      continue
    if len(pattern) == 6:
      if not char_e in pattern:
        decoded[pattern] = 9
      else:
        decoded[pattern] = 0

  return decoded


total = 0
for line in input_lines:
  unique_patterns, output_value = line.strip().split("|")
  unique_patterns = unique_patterns.split()
  unique_patterns = [alphasort(string) for string in unique_patterns]
  output_value = output_value.split()
  output_value = [alphasort(string) for string in output_value]
  decoded = decode_patterns(unique_patterns)
  n = 0
  for pattern in output_value:
    n = 10*n + decoded[pattern]
  total += n

  print n
 

print total