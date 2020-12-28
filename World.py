from config import *


class World:
    def __init__(self, name):
        self.space = [[Point(x,y,0) for x in range(WIDTH)] for y in range(HEIGHT)]
        self.name = name


class Point:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value