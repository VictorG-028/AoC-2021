from typing import List

################################

def part_1():
  
  with open("input.txt", "r") as file:
    first_line = int(file.readline())  # head
    lines = map(int, file.readlines()) # tail

  previous_line = first_line
  larger_than_previous_measurement = 0

  for line in lines:

    if line > previous_line:
      larger_than_previous_measurement += 1
    
    previous_line = line

  print(larger_than_previous_measurement)

################################

def part_2():

  def array_to_3windows(array: List[int]) -> List[ tuple[int] ]:
    windows = []

    for i in range(len(array)-2):
      current_window = (array[i], array[i+1], array[i+2])
      windows.append(current_window)

    return windows
    

  with open("Day1\\Day1-input.txt", "r") as file:
    windows = array_to_3windows(list(map(int, file.readlines())))

  fst_window = windows.pop(0)
  previous_window = fst_window
  larger_than_previous_measurement = 0

  for window in windows:

    if sum(window) > sum(previous_window):
      larger_than_previous_measurement += 1
    
    previous_window = window

  print(larger_than_previous_measurement)

################################

if __name__ == "__main__":
  part_1()
  part_2()
