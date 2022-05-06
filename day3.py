def part1(file):
    with open(file) as input:
        i = 0
        mcb = [0,0,0,0,0,0,0,0,0,0,0,0]
        for line in input:
            line = line.strip()
            for digit in line:
                if digit == "0":
                    mcb[i] -= 1
                else:
                    mcb[i] += 1
                i+=1
            i=0
        gammaList = []
        epsilonList = []
        for x in mcb:
            if x>0:
                gammaList.append("1")
                epsilonList.append("0")
            else:
                gammaList.append("0")
                epsilonList.append("1")

        gammaBin = "0b" + "".join(gammaList)
        epsilonBin = "0b" + "".join(epsilonList)
        gammaInt = int(gammaBin, 2)
        epsilonInt = int(epsilonBin, 2)
        return gammaInt * epsilonInt


print(part1("")) #Enter file locaiton as parameter

def part2(file):
    with open(file) as input:
        valid = input.readlines()
        i = 0
        while len(valid) > 1:
            valid = findMCB(valid, i)
            print(valid)
            i +=1
        print(f"Final: {valid}")
    with open(file) as input2:
        valid2 = input2.readlines()
        i = 0
        while len(valid2) > 1:
            valid2 = findLCB(valid2, i)
            print(valid2)
            i +=1
        print(f"Final2: {valid2}")
    oxBin = "0b" + "".join(valid)
    coBin = "0b" + "".join(valid2)
    return int(oxBin,2) * int(coBin, 2)
        
def findMCB(list, pos):
    mcb = 0
    list0 = []
    list1 = []
    for line in list:
        line = line.strip()
        if line[pos] == "0":
            list0.append(line)
            mcb -=1
        else:
            mcb +=1
            list1.append(line)
    if mcb>=0 :
        return list1
    else:
        return list0
def findLCB(list, pos):
    lcb = 0
    list0 = []
    list1 = []
    for line in list:
        line = line.strip()
        if line[pos] == "0":
            list0.append(line)
            lcb -=1
        else:
            lcb +=1
            list1.append(line)
    if lcb>=0 :
        return list0
    else:
        return list1

print(part2("")) #Enter file locaiton as parameter
