import math
def part1(fileName):
    file = open(fileName,"r")
    prev = math.inf 
    increased = 0
    for line in file:
        if(int(line)>prev):
            increased+=1
        prev = int(line)
    file.close()
    return increased

print(part1("AdventOfCode/day1.txt")) #Change file location to where your file is stored

def part2(fileName):
    file = open(fileName,"r")
    i = 0
    windows = [0,0,0]
    prev = math.inf
    increased = 0
    for line in file:
        windows[i % 3] = int(line)
        if (i>3):
            if(sum(windows)>prev):
                increased +=1
            prev = sum(windows)
        i+=1
    file.close()
    return increased

print(part2("AdventOfCode/day1.txt")) #Change file location to where your file is stored
