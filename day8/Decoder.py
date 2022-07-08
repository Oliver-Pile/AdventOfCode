
class Display:

    def __init__(self):
        self.segments = {
            "top-mid": [],
            "top-left": [],
            "top-right": [],
            "mid": [],
            "bottem-left": [],
            "bottem-right": [],
            "bottem-mid": []
        }
        self.endValues = {

        }
        self.finalValues = {

        }

    def addSegment(self, position, values):
        for v in values:
            self.segments[position].append(v)

    def addValue(self, value, code):
        self.endValues.update({value: code})

    def modifySegment(self, position, value):
        self.segments[position] = value

    def returnSegments(self):
        # Returns str of all current segment values
        temp = []
        for i in self.segments.values():
            if len(i) == 1:
                temp.append(i[0])
        return "".join(temp)

    def fillRemaining(self):
        # Adds value 8
        self.addValue(8, "abcdefg")
        # Adds value 6
        self.addValue(6, (self.segmentStr("top-mid") + self.segmentStr("top-left") + self.segmentStr("mid") +
                      self.segmentStr("bottem-left") + self.segmentStr("bottem-right") + self.segmentStr("bottem-mid")))
        # Adds value 9
        self.addValue(9, (self.segmentStr("top-mid") + self.segmentStr("top-left") + self.segmentStr("mid") +
                      self.segmentStr("top-right") + self.segmentStr("bottem-right") + self.segmentStr("bottem-mid")))
        # Adds value 0
        self.addValue(0, (self.segmentStr("top-mid") + self.segmentStr("top-left") + self.segmentStr("bottem-left") +
                      self.segmentStr("top-right") + self.segmentStr("bottem-right") + self.segmentStr("bottem-mid")))

    def segmentStr(self, pos):
        return self.segments[pos][0]

    def sortFinal(self):
        for k, v in self.endValues.items():
            self.finalValues.update({"".join(sorted(v)): k})
