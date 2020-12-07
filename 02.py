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
  parsedCharacterRule = [int(x) for x in characterRule]
  character = threeDataPoints[1].replace(":", "")
  pword = threeDataPoints[2]
  return {"Rule": parsedCharacterRule, "Char": character, "Password": pword}

def checkIfValidPwordP1(limit, frequency):
  if frequency >= limit[0] and frequency <= limit[1]:
    return True
  else:
    return False

def checkIfValidPwordP2(entry):
  firstIndex = entry["Rule"][0] -1
  secondIndex = entry["Rule"][1] -1
  # print(f"In checker: '{entry}'.", end=" ")

  letters = [entry["Password"][firstIndex], entry["Password"][secondIndex]]
  if  letters.count(entry["Char"]) == 1:
    return True
  else:
    return False

def part2(data):
  with open("02.txt") as f:
    puzzleInput = list()
    for line in f:
      puzzleInput.append(line.strip("\n"))

  validPwordCounter = 0
  for entry in puzzleInput:
    parsedEntry = parseItem(entry)
    result = checkIfValidPwordP2(parsedEntry)
    if result:
      validPwordCounter += 1
      # print("|")
    # else:
    #   print("--")
  print(validPwordCounter)
  return validPwordCounter