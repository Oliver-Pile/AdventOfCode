
class Fish:

    def __init__(self, age):
        self.age = age

    def simulate(self):
        if self.age != 0:
            self.age -= 1
            return False
        else:
            self.age = 6
            return True

    def fastSim(self):
        self.age = (self.age - 6) % 7
