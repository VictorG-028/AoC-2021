
from typing import List, Tuple


class Board:
  lines: List[List[str]]
  win: bool

  def __init__(self):
    self.lines = []
    self.win = False



def data_preparation() -> Tuple[List[str], List[Board]]:
  with open("Day4\\Day4-input.txt", "r") as file:
    # Get numbers from file
    numbers: List[str] = file.readline().rstrip('\n').split(',')
    file.readline()

    # Get boards from file
    boards: List[Board] = []
    new_board: Board

    while True:
      new_board = Board()

      for i in range(5):
        current_line = file.readline().rstrip('\n').split(' ')
        current_line = [number for number in current_line if number != '']
        new_board.lines.append(current_line)

      boards.append(new_board)

      if not file.readline(): break # Control de while loop

    return numbers, boards

  
def check_lines(b: Board) -> bool:
  win = False
  count = 0

  for line in b.lines:
    for number in line:

      if number != 'X': break
      else: count += 1

    if count == 5: 
      win = True
      break
    else: count = 0

  return win


def check_columns(b: Board) -> bool:
  win = False
  count = 0

  for i in range(5):
    for j in range(5):

      if b.lines[j][i] != 'X': break
      else: count += 1
    
    if count == 5: 
      win = True
      break
    else: count = 0

  return win


def sum_ummarked(b: Board) -> int:
  points = 0

  for lines in b.lines:
    for number in lines:
      
      if number != 'X': points += int(number)

  return points

################################

def part_1():

  numbers, boards = data_preparation()

  winner: Board = None
  last_marked: str = None

  for number_2_mark in numbers:

    # Mark current number in all the boards
    for board in boards:
      for i in range(5):
        mark = lambda number: 'X' if number == number_2_mark else number
        board.lines[i] = list(map(mark, board.lines[i]))


    # Check if there is a winner board
    for board in boards:
      if check_lines(board) or check_columns(board):
        winner = board
        last_marked = number_2_mark
        break
        
    if winner: break

  print(winner)
  print(last_marked)

  points = sum_ummarked(winner)

  print(f"Answer 1: {int(last_marked) * points}")
    

################################

def part_2():
  numbers, boards = data_preparation()

  last_winner: Board = None
  last_marked: str = None

  for number_2_mark in numbers:

    # Mark current number in all the boards
    for board in boards:
      for i in range(5):
        mark = lambda number: 'X' if number == number_2_mark else number
        board.lines[i] = list(map(mark, board.lines[i]))

    # Check if there is a winner board
    for board in boards:
      if check_lines(board) or check_columns(board):
        board.win = True

    # Game finishes when the last boards gets the win
    if len(boards) == 1 and boards[0].win:
      last_winner = boards[0]
      last_marked = number_2_mark
      break

    # Filter not winner boards
    not_winners = lambda b: not b.win
    boards = list(filter(not_winners, boards))

    
    
  print(last_winner)
  print(last_winner.lines)
  print(last_winner.win)
  print(last_marked)

  points = sum_ummarked(last_winner)

  print(f"Answer 2: {int(last_marked) * points}")


if __name__ == "__main__":
  part_1()
  part_2()
