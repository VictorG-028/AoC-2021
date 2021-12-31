from typing import List



def data_preparation():
  with open("Day6\\Day6-input.txt", "r") as file:
    line = file.readline().rstrip('\n').split(',')
    line = list(map(int, line))
  return line


def update_timer(timers: List[int]):
  new_timers_to_born = 0
  for i in range(len(timers)):
    if timers[i] == 0:
      new_timers_to_born += 1
      timers[i] = 6
    else:
      timers[i] -= 1

  return timers, new_timers_to_born


def born_new_timers(timers: List[int], new_timers: int):
  while new_timers > 0:
    timers.append(8)
    new_timers -= 1

  return timers


def progress_day(classes: List[int]) -> List[int]: 
  temp = classes[0]

  for i in range(1, 9):
    classes[i-1] = classes[i]

  classes[6] += temp
  classes[8] = temp

  return classes
 

################################

def part_1():

  timers = data_preparation() # timer = fish
  days_to_simulate = 80

  while days_to_simulate > 0:

    timers, new_timers = update_timer(timers)
    timers = born_new_timers(timers, new_timers)

    days_to_simulate -= 1

  print(f"Answer 1: {len(timers)}")

################################

def part_2():

  """
  1      days to simulate = 7
  0      days = 6
  6 8    days = 5
  5 7    days = 4
  4 6    days = 3
  3 5    days = 2
  2 4    days = 1
  1 3 <- days = 0 = not simulate further (Result of 7 days)
  0 2    days = -1 (Result of 8 days)
  6 1 8  days = -2 (Result of 9 days)
  """
  
  timers = data_preparation()
  days_to_simulate = 256
  classes = [0] * 9 # key = index = class ; value = count


  for timer in timers:
    classes[timer] += 1

  print(f"Classes: {classes}")

  for _ in range(days_to_simulate):
    classes = progress_day(classes)
    # print(f"Classes: {classes} | Sum: {sum(classes)}")

  print(f"Answer 2: {sum(classes)} | Days: {days_to_simulate} | Classes: {classes}")


################################

if __name__ == "__main__":
  part_1()
  part_2()
