from Decoder import Display


def part1(filePath):
    with open(filePath) as f:
        inputList = f.readlines()
    splitList = [l.strip().split("|")[1] for l in inputList]
    goodLen = [2, 4, 3, 7]
    total = 0
    for line in splitList:
        for segment in line.split():
            if len(segment) in goodLen:
                total += 1
    return total


# Need to write decoder for each line to find out the arrangements then can use this to determine each
def part2(filePath):
    with open(filePath) as f:
        inputList = f.readlines()
    sumOfValues = 0
    for line in inputList:
        splitList = line.strip().split("|")
        toDecode = sorted(splitList[0].strip().split(" "), key=len)
        """
        Pos 0: Value 1
        Pos 1: Value 7
        Pos 2: Value 4
        Pos 3: Length 5/ Values: 2,3,5
        Pos 4: Length 5/ Values: 2,3,5
        Pos 5: Length 5/ Values: 2,3,5
        Pos 6: Length 6/ Values 0, 6, 9
        Pos 7: Length 6/ Values 0, 6, 9
        Pos 8: Length 6/ Values 0, 6, 9
        Pos 9: Value 8
        """
        display = Display()
        display.addValue(1, str(toDecode[0]))
        display.addValue(7, str(toDecode[1]))
        display.addValue(4, str(toDecode[2]))
        display.addValue(0, str(toDecode[9]))
        # Adds the difference between value 7 and value 1 to the top-mid pos
        display.addSegment("top-mid", findDifference(toDecode[0], toDecode[1]))
        # Adds both letters for value 1 into the positions
        display.addSegment("top-right", toDecode[0])
        display.addSegment("bottem-right", toDecode[0])
        # Adds both letters from the 1-4 diff into the positions
        display.addSegment(
            "top-left", findDifference(toDecode[2], toDecode[0]))
        display.addSegment("mid", findDifference(toDecode[2], toDecode[0]))

        length5 = [toDecode[3], toDecode[4], toDecode[5]]
        for value in length5:
            # If the letters for 1 are in one of the len 5 then its value 3. Can then use to find middle and bottem value
            if (display.endValues[1][0] in value and display.endValues[1][1] in value):
                display.addValue(3, value)
                length5.remove(value)

        # Difference between value 3 and value 4 produces top and bottem middle values
        bmDiff = findDifference(findDifference(
            display.endValues[4], display.endValues[3]), display.segments["top-mid"])
        display.addSegment("bottem-mid", bmDiff)
        # Top left value is difference in reverse
        tlDiff = findDifference(
            display.endValues[4], display.endValues[3], True)
        display.modifySegment("top-left", list(tlDiff))
        # Find the mid segment value...
        for x in display.segments["mid"]:
            if x not in display.segments["top-left"]:
                display.modifySegment("mid", list(x))
        for v in length5:
            # If this is value 5
            if (display.segments["top-left"][0] in v):
                display.addValue(5, v)
                length5.remove(v)
        # Last Lenght 5 is value 2
        display.addValue(2, length5[0])
        # Find the right values
        trDiff = findDifference(
            display.endValues[5], display.endValues[1], True)
        # Changes the top/bottem right value
        display.modifySegment("top-right", list(trDiff))
        brDiff = findDifference(
            display.segments["top-right"][0], (display.segments["bottem-right"]
                                               [0] + display.segments["bottem-right"][1]))
        display.modifySegment("bottem-right", list(brDiff))
        # Fill in final vaue
        blDiff = findDifference(display.returnSegments(), "abcdefg")
        display.modifySegment("bottem-left", list(blDiff))
        display.fillRemaining()
        display.sortFinal()
        # Decoder finished!
        toSum = splitList[1].strip().split(" ")
        finalValue = []
        for x in toSum:
            finalValue.append(str(display.finalValues["".join(sorted(x))]))
        sumOfValues += int("".join(finalValue))
    return sumOfValues


def findDifference(str1, str2, reverse=False):
    largest = str1 if len(str1) > len(str2) else str2
    smallest = str1 if len(str1) < len(str2) else str2
    diff = []
    if not reverse:
        for c in largest:
            if c not in smallest:
                diff.append(c)
    if reverse:
        for c in smallest:
            if c not in largest:
                diff.append(c)
    return "".join(diff)


print(part1("")) #Enter file path
print(part2("")) #Enter file path
