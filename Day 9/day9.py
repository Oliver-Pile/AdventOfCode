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


def part2(filePath):
    # Finds all low points
    with open(filePath) as file:
        input = file.readlines()
    input = [x.strip() for x in input]
    lowPoints = []
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
                lowPoints.append([int(x), int(y)])
    basinSizes = []
    visited = []
    # Loop through all low points
    for x, y in lowPoints:
        visited.append([x, y])
        currentSize = 1
        # Find initial neighbours
        neighbours = findNeighbour(x, y, input, visited)
        # Loop through each eligable neighbour, with the potential to add more each time
        for x1, y1 in neighbours:
            # Ensuring it doesn't go back on itself
            if([x1, y1] not in visited):
                visited.append([x1, y1])
                currentSize += 1
                # Find neighbours of neighbour
                newNeighbours = findNeighbour(x1, y1, input, visited)
                for newCoord in newNeighbours:
                    neighbours.append([newCoord[0], newCoord[1]])
        # Adds the basin size to the list
        basinSizes.append(currentSize)
    # Finds biggest sizes
    sortedSizes = sorted(basinSizes, reverse=True)
    return sortedSizes[0] * sortedSizes[1] * sortedSizes[2]


def findNeighbour(x, y, heatMap, visited):
    temp = []
    if(y > 0 and int(heatMap[y-1][x]) != 9 and [x, y-1] not in visited):
        temp.append([x, y-1])
    if(y < 99 and int(heatMap[y+1][x]) != 9 and [x, y+1] not in visited):
        temp.append([x, y+1])
    if(x > 0 and int(heatMap[y][x-1]) != 9 and [x-1, y] not in visited):
        temp.append([x-1, y])
    if(x < 99 and int(heatMap[y][x+1]) != 9 and [x+1, y] not in visited):
        temp.append([x+1, y])
    return temp


# Initial thoughts for part 2:
"""
Loop through and find all low points - DONE
For each low point, loop through neighbours.
If neighbour != 9, add to list of todos and increment total
Then loop through all the todos and do the same...
Stop when all neighbours are = 9
Don't go back on yourself (Have a visted list)
Basically a BFS algorithm.
"""


print(part1("")) #Enter file path
print(part2("")) #Enter file path
