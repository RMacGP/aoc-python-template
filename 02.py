
def part1(data):

  with open("02.txt") as f:
    puzzleInput = list()
    for line in f:
      puzzleInput.append(line.strip("\n"))

  numberOfValidPasswords = countAllValidPasswordsP1(puzzleInput)
  return numberOfValidPasswords

def countAllValidPasswordsP1(myInput):
  validPasswordCounter = 0
  for entry in myInput:
    parsedEntry = parseItem(entry)
    characterFrequency = parsedEntry["Password"].count(parsedEntry["Char"])
    isValid = checkIfValidPwordP1(parsedEntry["Rule"], characterFrequency)
    if isValid:
      validPasswordCounter += 1

  return validPasswordCounter

def parseItem(item):
  threeDataPoints = item.split(" ")
  characterRule = threeDataPoints[0].split("-")
  character = threeDataPoints[1].replace(":", "")
  pword = threeDataPoints[2]
  return {"Rule": characterRule, "Char": character, "Password": pword}

def checkIfValidPwordP1(limit, frequency):
  if frequency >= int(limit[0]) and frequency <= int(limit[1]):
    return True
  else:
    return False

def checkIfValidPwordP2(entry):
  try:
    firstIndex = int(entry["Rule"][0]) -1
    secondIndex = int(entry["Rule"][1]) -1
    if entry["Password"][firstIndex] == entry["Char"] or entry["Password"][secondIndex] == entry["Char"]:
      return True
    else:
      return False
  except TypeError:
    return "whoops"

def part2(data):
  with open("02.txt") as f:
    puzzleInput = list()
    for line in f:
      puzzleInput.append(line.strip("\n"))

  validPwordCounter = 0
  for entry in puzzleInput:
    result = checkIfValidPwordP2(entry)
    if result:
      validPwordCounter += 1
    elif result == "whoops":
      return entry
  # return validPwordCounter

  # parsedEntry = parseItem(puzzleInput[3])
  # return f"{parsedEntry}, {checkIfValidPwordP2(parsedEntry)}"