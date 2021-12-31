from collections import Counter
from statistics import median, mean
from matplotlib import pyplot as plt
import pandas as pd
from math import floor

from typing import List

# all classes here


def data_preparation():
  with open("Day7\\Day7-input.txt", "r") as file:
    line = file.readline().rstrip('\n').split(',')
    line = list(map(int, line))
  return line


def align_to(align_to: int, crabs_horizontal: List[int], expensive = False) -> int:
  used_fuel = 0
  extra_cost = lambda dist: sum( [i+1 for i in range(dist)] )

  for h in crabs_horizontal:

    if not expensive:
      used_fuel += abs(h-align_to)
    else:
      used_fuel += extra_cost(abs(h-align_to))

  return used_fuel


################################

def part_1():
  crabs_horizontal = data_preparation()

  _median = int(median(crabs_horizontal)) # int() is for rounding

  # # Statistics tested
  # l = len(crabs_horizontal)
  # _mean = mean(crabs_horizontal)
  # most_common_element = Counter(crabs_horizontal).most_common(1)
  # first_elements = crabs_horizontal[0:5]
  # last_elements = list(reversed(list(reversed(crabs_horizontal))[0:5]))
  # s = sum(crabs_horizontal)

  # # Prints
  # print(f"Len: {l} | Mediana: {_median} | Média: {_mean}")
  # print(f"Max value: {crabs_horizontal[-1]}")
  # print(f"Most common element: {most_common_element[0][0]} | frequência: {most_common_element[0][1]}")
  # print(f"5 first elements: {first_elements}")
  # print(f"5 last elements: {last_elements}")
  # print(f"Sum: {s}")

  # df = pd.DataFrame.from_dict(Counter(crabs_horizontal), orient='index')
  # df.plot(kind='bar')

  x = _median
  total_fuel_used = align_to(x, crabs_horizontal)

  print(f"Answer 1: {total_fuel_used} | h_pos = median = {x}")
  plt.show()

################################

def part_2():
  crabs_horizontal = data_preparation()

  x = [x for x in range(360, 861)]
  y = [align_to(y, crabs_horizontal, expensive=True) for y in x]

  plt.plot(x, y)
  plt.xlabel('x - align to')
  plt.ylabel('y - total fuel used')

  _mean = int(mean(crabs_horizontal)) # int() is for rounding

  x = _mean
  total_fuel_used = align_to(x, crabs_horizontal, expensive=True)

  print(f"Answer 2: {total_fuel_used} | h_pos = mean = {x}")
  plt.show()

################################

if __name__ == "__main__":
  part_1()
  part_2()
