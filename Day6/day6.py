from Fish import Fish


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

"""Testing only - Please ignore
def part2(filePath):  # Doesn't work
    # in while loop, take 6 each time. Generate more fish by the amount of fish at level <6 before then increase incrementer by 6. Or 12, 18 etc.
    with open(filePath) as fileInp:
        inputList = fileInp.read().split(",")
    fishList = []
    for fishAge in inputList:
        fishList.append(Fish(int(fishAge)))
    i = 0
    while i < 80:
        total = 0
        for fish in fishList:
            if fish.age < 6:
                fish.fastSim()
                total += 1
            else:
                fish.fastSim()
        fishList += [Fish(8) for _ in range(total)]
        i += 6
    return len(fishList)
"""


# test()
#print(part2("AdventOfCode/Day 6/day6.txt"))
print(day6("AdventOfCode/Day 6/day6.txt", 80))
# print(day6("AdventOfCode/Day 6/day6.txt", 256)) Don't run this
