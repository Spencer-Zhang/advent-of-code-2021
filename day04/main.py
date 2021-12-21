COMPLETED_LINES = [
  (0,1,2,3,4),
  (5,6,7,8,9),
  (10,11,12,13,14),
  (15,16,17,18,19),
  (20,21,22,23,24),
  (0,5,10,15,20),
  (1,6,11,16,21),
  (2,7,12,17,22),
  (3,8,13,18,23),
  (4,9,14,19,24),
  # (0,6,12,18,24),
  # (4,8,12,16,20)
]


with open('input.txt') as f:
  input_lines = f.readlines()
  callouts = map(int, input_lines.pop(0).strip().split(","))

  boards = []

  board_number = 0
  while(len(input_lines) > 0):
    board = {}
    input_lines.pop(0)
    for r in range(5):
      next_row = map(int, input_lines.pop(0).strip().split())
      for c in range(5):
        board[next_row[c]] = 5*r + c
    boards.append(board)


filled = []
for board in boards:
  filled.append(set())

called_numbers = set()
finished_boards = set()
last_finished = -1

for c in callouts:
  called_numbers.add(c)
  finished_board = -1
  for b in range(len(boards)):
    if b in finished_boards:
      continue
    board = boards[b]
    if c in board:
      filled[b].add(board[c])
      for completed in COMPLETED_LINES:
        if filled[b].issuperset(completed):
          last_finished = b
          finished_boards.add(b)
          break

  if len(finished_boards) == len(boards):
    break


total = 0
for called in boards[last_finished]:
  if not called in called_numbers:
    total += called
print total

print total * c