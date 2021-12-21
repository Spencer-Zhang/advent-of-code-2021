numbers = []

with open('input.txt') as f:
  input_lines = f.readlines()
  for line in input_lines:
    numbers.append(line.strip())

print numbers

bit_count = len(numbers[0].strip())

def most_common_bit(numbers, position):
  count = {"0": 0, "1": 0}
  for n in numbers:
    count[n[position]] += 1
  if count["0"] > count["1"]:
    return "0"
  elif count["1"] > count["0"]:
    return "1"
  else:
    return "1"

def least_common_bit(numbers, position):
  count = {"0": 0, "1": 0}
  for n in numbers:
    count[n[position]] += 1
  if count["0"] < count["1"]:
    return "0"
  elif count["1"] < count["0"]:
    return "1"
  else:
    return "0"

def binary_to_decimal(n_string):
  n = 0
  for c in n_string:
    n = 2 * n + int(c)
  return n

gamma = ""
for i in range(bit_count):
  gamma += most_common_bit(numbers, i)

epsilon = ""
for i in range(bit_count):
  epsilon += least_common_bit(numbers, i)

# print binary_to_decimal(gamma)
# print binary_to_decimal(epsilon)
# print binary_to_decimal(gamma) * binary_to_decimal(epsilon)


og_numbers = list(numbers)
for i in range(bit_count):
  if len(og_numbers) == 1:
    break
  mcb = most_common_bit(og_numbers, i)
  og_numbers = [n for n in og_numbers if n[i] == mcb]
print og_numbers

co2_numbers = list(numbers)
for i in range(bit_count):
  if len(co2_numbers) == 1:
    break
  lcb = least_common_bit(co2_numbers, i)
  co2_numbers = [n for n in co2_numbers if n[i] == lcb]

print co2_numbers
print binary_to_decimal(og_numbers[0]) * binary_to_decimal(co2_numbers[0])