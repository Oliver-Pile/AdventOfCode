class Card:
    scoreCard = []

    def __init__(self):
        self.scoreCard = []

    def addRow(self, row):
        rowList = row.split()
        self.scoreCard.append(rowList)

    # For debugging - Prints in readable format
    def printGame(self):
        for x in self.scoreCard:
            print(f"{x}\n")
        print("Next\n")

    def checkGuess(self, guess):
        i = 0
        for row in self.scoreCard:
            if guess in row:
                index = row.index(guess)
                self.scoreCard[i][index] = "X"
                break
            i += 1

    def checkWin(self, guess, part2):
        winner = False
        for row in self.scoreCard:
            if row.count("X") == len(row):
                winner = True
        rotated = zip(*self.scoreCard[::-1]) #Straight from stack overflow
        for row in rotated:
            if row.count("X") == len(row):
                winner = True
        if not part2:
            if winner:
                total = 0
                for row in self.scoreCard:
                    for num in row:
                        if num != "X":
                            total += int(num)

                return total * int(guess)
        if part2:
            if winner:
                return True
        return None


def part1(fileName):
    with open(fileName) as input:
        input = input.read()
        list = input.split("\n")
    guesses = list[0].split(",")
    del list[0]
    boards = [Card() for _ in range(list.count(""))]
    i = 1
    p = 0
    while i < len(list):
        b = boards[p]
        b.addRow(list[i])
        b.addRow(list[i+1])
        b.addRow(list[i+2])
        b.addRow(list[i+3])
        b.addRow(list[i+4])
        i += 6
        p += 1

    for guess in guesses:
        for b in boards:
            b.checkGuess(guess)
            winner = b.checkWin(guess, False)
            if winner != None:
                return winner


def part2(fileName):
    with open(fileName) as input:
        input = input.read()
        list = input.split("\n")
    guesses = list[0].split(",")
    del list[0]
    boards = [Card() for b in range(list.count(""))]
    i = 1
    p = 0
    while i < len(list):
        b = boards[p]
        b.addRow(list[i])
        b.addRow(list[i+1])
        b.addRow(list[i+2])
        b.addRow(list[i+3])
        b.addRow(list[i+4])
        i += 6
        p += 1

    for guess in guesses:
        z = 0
        for b in boards:
            b.checkGuess(guess)
            if len(boards) != 1:
                if(b.checkWin(guess, True)):
                    del boards[z]
            if len(boards) == 1:
                winner = b.checkWin(guess, False)
                if winner != None:
                    return winner
            z += 1


print(part1("")) #Enter file location in ""
print(part2("")) #Enter file location in ""
