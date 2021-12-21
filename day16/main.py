from collections import defaultdict
from copy import copy

# with open('example.txt') as f:
with open('input.txt') as f:
  hexa = f.readlines()[0].strip()
  binary_length = len(hexa) * 4

  input_string = bin(int(hexa, 16))[2:].zfill(binary_length)

class Packet:
  def __init__(self, input_string):

    print "Parsing:", input_string

    self.dump()
    self.input_string = input_string
    self.version = int(self.read_next(3), 2)
    self.type = int(self.read_next(3), 2)
    self.subpackets = []
    self.value = -1

    if self.type == 4: # Literal
      n = 0
      while True:
        next = self.read_next(5)
        n = 16 * n + int(next[1:], 2)
        if next[0] == "0":
          break
      self.value = n

      print "Literal packet with value", n, "and version", self.version
    else:
      print "Operator with version", self.version
      length_type = int(self.read_next(1))
      print "Length type", length_type
      if length_type == 0:
        length = int(self.read_next(15), 2)
        print "Length", length
        subpacket_string = self.read_next(length)
        while len(subpacket_string) > 0:
          new_packet = Packet(subpacket_string)
          subpacket_string = new_packet.get_remaining_input()
          self.subpackets.append(new_packet)
      elif length_type == 1:
        length = int(self.read_next(11), 2)
        print "Length", length
        subpacket_string = self.get_remaining_input()
        for i in range(length):
          print "i", i
          new_packet = Packet(subpacket_string)
          subpacket_string = new_packet.get_remaining_input()
          self.subpackets.append(new_packet)
        self.index = 0
        self.input_string = subpacket_string
      else:
        raise "Invalid length type: " + str(length_type)

      child_values = [p.value for p in self.subpackets]
      if self.type == 0:
        self.value = sum(child_values)
      elif self.type == 1:
        self.value = reduce(lambda x, y: x * y, child_values)
      elif self.type == 2:
        self.value = min(child_values)
      elif self.type == 3:
        self.value = max(child_values)
      elif self.type == 5:
        if len(child_values) != 2:
          raise "Invalid number of child_values for greater than"
        if child_values[0] > child_values[1]:
          self.value = 1
        else:
          self.value = 0
      elif self.type == 6:
        if len(child_values) != 2:
          raise "Invalid number of child_values for less than"
        if child_values[0] < child_values[1]:
          self.value = 1
        else:
          self.value = 0
      elif self.type == 7:
        if len(child_values) != 2:
          raise "Invalid number of child_values for equal to"
        if child_values[0] == child_values[1]:
          self.value = 1
        else:
          self.value = 0
      



  def get_version_sum(self):
    return self.version + sum([p.get_version_sum() for p in self.subpackets])

  def get_version(self):
    return self.version

  def read_next(self, i):
    self.index += i
    return self.input_string[self.index - i: self.index]

  def dump(self): # Finished reading a packet; Dump any remaining bits.
    self.read = ""
    self.index = 0

  def get_remaining_input(self):
    return self.input_string[self.index:]

read = ""
index = 0

packet = Packet(input_string)

print packet.get_version_sum()
print packet.value

