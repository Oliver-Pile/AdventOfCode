def part1(filePath):
    with open(filePath) as file:
        input = file.readlines()
    input = [x.strip() for x in input]
    totalRisk = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            lowest = 0
            currentValue = input[y][x]
            if(y > 0):
                if(currentValue < input[y-1][x]):
                    lowest += 1
            else:
                lowest += 1
            if(y < 99):
                if(currentValue < input[y+1][x]):
                    lowest += 1
            else:
                lowest += 1
            if(x > 0):
                if(currentValue < input[y][x-1]):
                    lowest += 1
            else:
                lowest += 1
            if(x < 99):
                if(currentValue < input[y][x+1]):
                    lowest += 1
            else:
                lowest += 1
            if(lowest == 4):
                totalRisk += int(currentValue)+1
    return totalRisk


def part2():
    pass


"""
For part 2:
Loop through and find all low points
For each low point, loop through neighbours.
If neighbour != 9, add to list of todos and increment total
Then loop through all the todos and do the same...
Stop when all neighbours are = 9
Don't go back on yourself (Have a visted list)
Basically a BFS algorithm.
"""


print(part1(""))#Enter file path here
