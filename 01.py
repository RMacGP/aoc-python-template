

def part1(data):
    __import__('time').sleep(1)
    with open('01.txt') as f:
    #   myNumbers = list()
    #   for line in f:
    #     return line
    #     myNumbers.append(int(line.strip('\n')))
    # for i in myNumbers:
    #   for j in myNumbers:
    #     if i + j == 2020:
    #       return i*j
    # myNumbers = list()
  for line in data:
    return line
    myNumbers.append(int(line.strip("\n")))
  return myNumbers

def part2(data):
    __import__('time').sleep(1)
    with open('01.txt') as f:
      myNumbers = list()
      for line in f:
        myNumbers.append(int(line.strip('\n')))
    for i in myNumbers:
      for j in myNumbers:
        for k in myNumbers:
          if i + j + k == 2020:
            return i*j*k
