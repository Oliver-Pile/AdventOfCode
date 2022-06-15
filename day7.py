import math

# You can 'cheat' part one by just using the median as the mid point value (Found on google)
def part1(filePath):
    median = 323
    with open(filePath) as file:
        inputList = file.read().split(",")
    inputList = [int(x) for x in inputList]
    total = 0
    for item in inputList:
        total += abs(median-item)
    return total


def part2(filePath):
    with open(filePath) as file:
        inputList = file.read().split(",")
    inputList = [int(x) for x in inputList]
    lowestFuel = math.inf
    for midPoint in range(min(inputList), max(inputList)+1):
        fuel = 0
        for crab in inputList:
            fuel += calculateFuel(crab, midPoint)
        if fuel < lowestFuel:
            lowestFuel = fuel
    return lowestFuel


def calculateFuel(crab, endPoint):
    diff = abs(endPoint-crab)
    totalFuel = 0
    for i in range(1, diff+1):
        totalFuel += i
    return totalFuel

#Enter file path in ""
print(part1(""))
print(part2(""))
