from Fish import Fish
from collections import Counter

# Works for small number of days. (Would work for large numbers, will just take an age...)
def day6(filePath, days):
    with open(filePath) as fileInp:
        inputList = fileInp.read().split(",")
    fishList = []
    for fishAge in inputList:
        fishList.append(Fish(int(fishAge)))
    for x in range(days):
        temp = []
        for fish in fishList:
            newFish = fish.simulate()
            if newFish:
                temp.append(Fish(8))
        fishList += temp
    return len(fishList)


# Works for both parts (And is quicker)
def part2(filePath, days):
    with open(filePath) as fileInp:
        inputList = fileInp.read().split(",")
    fishAges = Counter({'0': 0, '1': 0, '2': 0, '3': 0,
                       '4': 0, '5': 0, '6': 0, '7': 0, '8': 0})
    fishAges.update(inputList)
    for day in range(days):
        fishAges = Counter({'0': fishAges['1'], '1': fishAges['2'],
                            '2': fishAges['3'], '3': fishAges['4'], '4': fishAges['5'], '5': fishAges['6'], '6': (fishAges['0'] + fishAges['7']), '7': fishAges['8'], '8': fishAges['0']})
    return sum(fishAges.values())

#Enter file path in ""
print(day6("", 80))
print(part2("", 256))

