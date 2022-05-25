

class Vent:
    def __init__(self, x1, y1, x2, y2):
        self.startX = x1
        self.startY = y1
        self.endX = x2
        self.endY = y2

    def fillIn(self, part2):
        if self.startY == self.endY:
            if self.startX < self.endX:
                for i in range(self.startX, self.endX+1):
                    area[self.startY][i] += 1
            else:
                for i in range(self.endX, self.startX+1):
                    area[self.startY][i] += 1
        elif self.startX == self.endX:
            if self.startY < self.endY:
                for i in range(self.startY, self.endY+1):
                    area[i][self.startX] += 1
            else:
                for i in range(self.endY, self.startY+1):
                    area[i][self.startX] += 1
        else:
            if(part2):
                diff = abs(self.startX-self.endX)
                for i in range(diff+1):
                    if self.startX < self.endX and self.startY < self.endY:
                        area[self.startY + i][self.startX + i] += 1
                    if self.startX > self.endX and self.startY < self.endY:
                        area[self.startY + i][self.startX - i] += 1
                    if self.startX < self.endX and self.startY > self.endY:
                        area[self.startY - i][self.startX + i] += 1
                    if self.startX > self.endX and self.startY > self.endY:
                        area[self.startY - i][self.startX - i] += 1


def day5(fileName, part2):
    lines = []
    with open(fileName) as input:
        for line in input:
            l = line.strip().split(" -> ")
            c = []
            for p in l:
                temp = p.split(",")
                c.append(temp[0])
                c.append(temp[1])
            lines.append(Vent(int(c[0]), int(c[1]), int(c[2]), int(c[3])))
    for v in lines:
        v.fillIn(part2)
    total = 0
    for i in range(len(area)):
        for j in range(len(area[i])):
            if area[i][j] > 1:
                total += 1
    print(total)


area = [[0 for _ in range(1000)] for x in range(1000)]
day5("", False) #Enter your file path here
area = [[0 for _ in range(1000)] for x in range(1000)]
day5("", True) #Enter your file path here
