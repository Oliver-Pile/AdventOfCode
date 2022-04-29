def part1(file):
    input = open(file,"r")
    horiz = 0
    depth = 0
    i = 0
    for line in input:
        ls = line.split(" ")
        if ls[0] == "forward":
            horiz += int(ls[1])
        if ls[0] == "down":
            depth += int(ls[1])
        if ls[0] == "up":
            depth -= int(ls[1])
    input.close()
    return horiz * depth
        
def part2(file):
    input = open(file,"r")
    horiz = 0
    depth = 0
    aim = 0
    i = 0
    for line in input:
        ls = line.split(" ")
        if ls[0] == "forward":
            horiz += int(ls[1])
            depth += aim * int(ls[1])
        if ls[0] == "down":
            aim += int(ls[1])
        if ls[0] == "up":
            aim -= int(ls[1])
    input.close()
    return horiz * depth

print(part1("AdventOfCode/day2.txt"))
print(part2("AdventOfCode/day2.txt"))
