import math


class Triangle:
    def __init__(self):
        self.a = 30
        self.b = 30
        self.__c = 0

    @property
    def c(self):
        return math.sqrt(self.a ** 2 + self.b ** 2)

    @c.setter
    def c(self, x):
        print('WARNING: C is can notbe se')


t = Triangle()

print(t.a, t.b, t.c)
