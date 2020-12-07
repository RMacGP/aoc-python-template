def part1(data):
  puzzleInput = list()
  with open("04.txt") as f:
    for line in f:
      puzzleInput.append(line.strip("\n"))
  firstPassportIndex = puzzleInput.index('') - 1
  firstPassport = puzzleInput[:firstPassportIndex]
  for idx, item in enumerate(firstPassport):
    splitData = item.split()
    firstPassport.append(splitData)
    # firstPassport.append(item.split())
    # firstPassport.remove(item)
    # firstPassport[idx] = item.split()
  #   itemLength = len(item)
  #   if itemLength > 0:
  #     for i in item:
  #       firstPassport.append(i)
  return splitData

def part2(data):
  pass