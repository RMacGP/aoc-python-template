def part1(data):
    puzzleInput = []
    with open("03.txt") as f:
        for line in f:
            puzzleInput.append(line.strip("\n"))
    myInput = tuple(puzzleInput)
    xStep = 3
    yStep = 1
    trees = treesEncountered(myInput, xStep, yStep)
    return trees


def part2(data):

    # Right 1, down 1.
    # Right 3, down 1.
    # Right 5, down 1.
    # Right 7, down 1.
    # Right 1, down 2.

  puzzleInput = []
  with open("03.txt") as f:
    for line in f:
      puzzleInput.append(line.strip("\n"))
  myInput = tuple(puzzleInput)
  rules = [[1,1],[3,1],[5,1],[7,1],[1,2]]
  treesForEachSlope = []
  result = 1
  for i in range(5):
    thisRule = rules[i]
    thisTrees = treesEncountered(myInput, thisRule[0], thisRule[1])
    result *= thisTrees
    treesForEachSlope.append(thisTrees)

  return result


def treesEncountered(theInput, xIncrement, yIncrement):
    treeCounter = 0
    xPos = 0
    for slope in theInput[::yIncrement]:
        if slope[xPos] == "#":
            treeCounter += 1
        if xPos + xIncrement >= 30:
            xPos -= 31 - xIncrement
        else:
            xPos += xIncrement
    return treeCounter

