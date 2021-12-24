
from typing import List, Tuple


class Map:
  matrix: List[List[str]]
  width: int
  height: int

  def __init__(self, width: int, height: int):
    self.matrix = [['.'] * width for i in range(height)]
    self.width  = width
    self.height = height



def data_preparation() -> List[Tuple[ Tuple[int, int], Tuple[int, int] ]]:
  with open("Day5\\Day5-input.txt", "r") as file:

    lines = file.readlines()

    transform_1 = lambda line: line.rstrip('\n').split(' -> ')
    transform_2 = lambda line: ( line[0].split(',') , line[1].split(',') )
    transform_3 = lambda line: ( map(int, line[0])  , map(int, line[1])  )
    transform_4 = lambda line: ( tuple(line[0])     , tuple(line[1])     )

    lines = list(map( transform_1, lines ))
    lines = list(map( transform_2, lines ))
    lines = list(map( transform_3, lines ))
    lines = list(map( transform_4, lines ))

  return lines


def next_symbol(s: str) -> str:
  if s == '.': return '1'
  return str(int(s)+1)


def draw_horizontal(m: Map, pair: Tuple[ Tuple[int, int], Tuple[int, int] ]) -> int:
  p1, p2 = pair[0], pair[1]
  freeze_line = p1[0]

  smaller, larger = (p1[1], p2[1]) if p1[1] < p2[1] else (p2[1], p1[1])
  start_column, end_column = smaller, larger

  count_overlap = 0

  # pick Y = pick column = pick width
  for pick_column in range(start_column, end_column +1):
    symbol = m.matrix[freeze_line][pick_column]
    symbol = next_symbol(symbol)
    if symbol == '2': count_overlap += 1
    m.matrix[freeze_line][pick_column] = symbol

  return count_overlap


def draw_vertical(m: Map, pair: Tuple[ Tuple[int, int], Tuple[int, int] ]):
  p1, p2 = pair[0], pair[1]
  freeze_column = p1[1]

  smaller, larger = (p1[0], p2[0]) if p1[0] < p2[0] else (p2[0], p1[0])
  start_line, end_line = smaller, larger

  count_overlap = 0

  # pick X = pick line = pick height
  for pick_line in range(start_line, end_line +1):
    symbol = m.matrix[pick_line][freeze_column]
    symbol = next_symbol(symbol)
    if symbol == '2': count_overlap += 1
    m.matrix[pick_line][freeze_column] = symbol

  return count_overlap


def draw_diagonal(m: Map, pair: Tuple[ Tuple[int, int], Tuple[int, int] ]):
  p1, p2 = pair[0], pair[1]

  """ 4 possible directions
  (1,  -1)   (1,  1)
           X
  (-1, -1)   (-1, 1)  
  """
  direction = ()
  if   p1[0] < p2[0] and p1[1] < p2[1]: direction = (1,1)
  elif p1[0] > p2[0] and p1[1] < p2[1]: direction = (-1,1)
  elif p1[0] < p2[0] and p1[1] > p2[1]: direction = (1,-1)
  else: direction = (-1,-1)

  distance = abs(p1[0] - p2[0]) +1

  count_overlap = 0

  for i in range(distance):
    x = p1[0] + i * direction[0]
    y = p1[1] + i * direction[1]

    symbol = m.matrix[x][y]
    symbol = next_symbol(symbol)
    if symbol == '2': count_overlap += 1
    m.matrix[x][y] = symbol
  
  return count_overlap


def show_map(m: Map, start_line, start_column, lenght):
  for i in range(start_column, start_column + lenght):
    print(i, end=" ")
    for j in range(start_line, start_line + lenght):
      print(m.matrix[i][j], end="")
    print()


def draw_map_in_file(m: Map):
  with open("Day5\\map.txt", "w") as new_file:
    current_line = ''

    for i in range(m.height):
      for j in range(m.width):
        current_line += f"{m.matrix[i][j]:^1}"


      current_line += "\n"
      new_file.writelines(current_line)
      current_line = ''


def count_overlaping_lines(m: Map) -> int:
  count = 0

  for i in range(m.height):
    for j in range(m.width):
      if m.matrix[i][j] != '.' and int(m.matrix[i][j]) > 1:
        count += 1

  return count


################################

def part_1():

  pairs_of_points = data_preparation()
  m: Map = Map(1000, 1000) # 1000 x 1000 matrix

  answer = 0

  for pair in pairs_of_points:

    pair_1_x = pair[0][0]
    pair_1_y = pair[0][1]

    pair_2_x = pair[1][0]
    pair_2_y = pair[1][1]

    if pair_1_x == pair_2_x:
      # Y variation = column variation = width variation = horizontal variation
      answer += draw_horizontal(m, pair)
    elif pair_1_y == pair_2_y:
      # X variation = line variation = height variation = vertical variation
      answer += draw_vertical(m, pair)
    else:
      answer += draw_diagonal(m, pair)



  show_map(m, 0, 0, 10)
  draw_map_in_file(m)

  # answer = count_overlaping_lines(m)

  print(f"Answer 1: {answer}")

################################

def part_2():
  pairs_of_points = data_preparation()
  m: Map = Map(1000, 1000) # 1000 x 1000 matrix

  answer = 0

  for pair in pairs_of_points:

    pair_1_x = pair[0][0]
    pair_1_y = pair[0][1]

    pair_2_x = pair[1][0]
    pair_2_y = pair[1][1]

    if pair_1_x == pair_2_x:
      # Y variation = column variation = width variation = horizontal variation
      answer += draw_horizontal(m, pair)
    elif pair_1_y == pair_2_y:
      # X variation = line variation = height variation = vertical variation
      answer += draw_vertical(m, pair)
    else:
      pass



  show_map(m, 0, 0, 10)
  draw_map_in_file(m)

  # answer = count_overlaping_lines(m)

  print(f"Answer 2: {answer}")

################################

if __name__ == "__main__":
  part_1()
  part_2()
