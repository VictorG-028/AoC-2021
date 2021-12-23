from functools import reduce 

################################

def part_1():

  with open("Day3\\Day3-input.txt", "r") as file:
    lines = file.readlines()
    lines = list(map(lambda l: l.rstrip("\n"), lines))

  columns = 12
  common_count = [0] * columns
  current_column = 0

  for line in lines:
    for char in line:

      if char == '0':
        common_count[current_column] += 1
      else:
        common_count[current_column] -= 1
      current_column += 1

    current_column = 0 # Reset current column

  # position i == column i
  # common_count > 0 -> count 0 > count 1 in position i
  # common_count < 0 -> count 0 < count 1 in position i
  # common_count = 0 -> count 0 = count 1 in position i
  print(common_count)


  gamma = list(map(lambda count: '0' if count > 0 else '1', common_count))
  gamma = reduce(lambda fst, nex: fst+nex, gamma)
  gamma = int(gamma, base=2)
  print("0" + format(gamma, 'b')) # string is two's complement, must be one's complement

  # epsilon = list(map(lambda count: '1' if count > 0 else '0', common_count))
  # epsilon = reduce(lambda fst, nex: fst+nex, epsilon)
  # epsilon = int(epsilon, base=2)
  epsilon = ~gamma + 2**12
  print(format(epsilon, 'b')) # string is two's complement, must be one's complement

  print(f"Answer 1: {gamma * epsilon} | Gamma: {gamma} | Epsilon: {epsilon}")

################################

def part_2():

  def find_most_common_bit(bits_list, column) -> int:
    common_bit_count = 0

    for bits_line in bits_list:
      bit = bits_line[column]
      common_bit_count += 1 if bit == '0' else -1

    return '0' if common_bit_count > 0 else '1'


  def find_most_uncommon_bit(bits_list, column) -> int:
    common_bit_count = 0

    for bits_line in bits_list:
      bit = bits_line[column]
      common_bit_count += 1 if bit == '0' else -1

    return '1' if common_bit_count > 0 else '0'


  with open("Day3-input.txt", "r") as file:
    lines = file.readlines()
    lines = list(map(lambda line: line.rstrip("\n"), lines))

  o2_generation = lines
  co2_scrubber = lines

  for i in range(12):
    if len(o2_generation) == 1: break
    mask_bit = find_most_common_bit(o2_generation, column=i)
    o2_generation = list(filter(lambda line: line[i] == mask_bit, o2_generation))

  for i in range(12):
    if len(co2_scrubber) == 1: break
    mask_bit = find_most_uncommon_bit(co2_scrubber, column=i)
    co2_scrubber = list(filter(lambda line: line[i] == mask_bit, co2_scrubber))

  print(f"o2_generation: {o2_generation} | co2_scrubber: {co2_scrubber}")

  o2_generation = list(map(lambda bit_string: int(bit_string, base=2), o2_generation))
  co2_scrubber = list(map(lambda bit_string: int(bit_string, base=2), co2_scrubber))

  results = []
  for i in o2_generation:
    for j in co2_scrubber:
      results.append(i*j)

  print(f"Answer 2: {results} | o2_generation: {o2_generation} | co2_scrubber: {co2_scrubber}")

################################

if __name__ == "__main__":
  part_1()
  part_2()
