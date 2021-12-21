

def part_1():

  with open("Day2-input.txt", "r") as file:
    lines = map(lambda s: s.split(), file.readlines())
    lines = list(map(lambda s: (s[0], int(s[1])), lines))

  depth = 0
  abscissa = 0

  for line in lines:
    command = line[0]

    if command == "forward":
      abscissa += line[1]
    elif command == "down":
      depth += line[1]
    elif command == "up":
      depth -= line[1]

  print(depth)
  print(abscissa)
  print(abscissa*depth)

################################

def part_2():

  with open("Day2-input.txt", "r") as file:
    lines = map(lambda s: s.split(), file.readlines())
    lines = list(map(lambda s: (s[0], int(s[1])), lines))

  depth = 0
  abscissa = 0
  aim = 0

  for line in lines:
    command = line[0]

    if command == "forward":
      abscissa += line[1]
      depth += aim * line[1]
    elif command == "down":
      aim += line[1]
    elif command == "up":
      aim -= line[1]

  print(depth)
  print(abscissa)
  print(abscissa*depth)


if __name__ == "__main__":
  part_1()
  part_2()
