from config import *
from random import choice
from World import Point
from math import sqrt, modf
from time import sleep

class Puppy:
    wld = None
    def __init__(self, x, y, world):
        self.x = x
        self.y = y
        self.world = world
        if Puppy.wld is None: Puppy.wld = world
        world.space[y][x].value = self
        self.symb = '♂'
        self.id = -1

    @classmethod
    def new_puppy(cls, x, y):
        print(x, y, sep=', ')
        return Puppy(x, y, Puppy.wld)

    def move(self):
        direction = self.look_around()
        move_dict = {0: self.move_up,
                     1: self.move_down,
                     2: self.move_left,
                     3: self.move_right,
                     4: lambda : 0,
                     5: lambda : 0,
                     6: lambda : 0,
                     7: lambda : 0,
                     8: lambda : 0,
                     9: lambda : 0,
                     }

        # ch = [direction,direction,direction,0,1,2,3,4,5 ]#,4,5,6,7,8,9]
        ch = [direction]

        move_dict[choice(ch)]()

    def move_up(self):
        new_val = self.y - (step if self.y > 0 else 0)
        if (self.world.space[new_val][self.x].value != 0) : return
        self.world.space[self.y][self.x].value = 0
        self.world.space[new_val][self.x].value = self
        self.y = new_val


    def move_down(self):
        new_val = self.y + (step if self.y < HEIGHT-1 else 0)
        if(self.world.space[new_val][self.x].value != 0): return
        self.world.space[self.y][self.x].value = 0
        self.world.space[new_val][self.x].value = self
        self.y = new_val


    def move_left(self):
        new_val = self.x - (step if self.x > 0 else 0)
        if (self.world.space[self.y][new_val].value != 0) : return
        self.world.space[self.y][self.x].value = 0
        self.world.space[self.y][new_val].value = self
        self.x = new_val


    def move_right(self):
        new_val = self.x + (step if self.x < WIDTH-1 else 0)
        if (self.world.space[self.y][new_val].value != 0) : return
        self.world.space[self.y][self.x].value = 0
        self.world.space[self.y][new_val].value = self
        self.x = new_val



    def look_around(self):
        s_list = self.get_points_around_range(SEE_DISTANCE)
        fars = []
        min_val = 0
        target = None
        for level in s_list:
            for i in level:
                if not isinstance(i.value, int):
                    distance = round(sqrt(pow(i.x - self.x, 2)+pow(i.y - self.y, 2)), 2)
                    if distance > min_val:
                        min_val = distance
                        target = i.value

        if target is None: return 4
        height = (target.y - self.y)
        width_dis = target.x - self.x


        def  vertical():
            if(height > 0):
                return 1 # down
            else: return 0 # up
        def horizontal():
            if(width_dis > 0):
                return 3 # right
            else: return 2

        return choice([vertical, horizontal])()



    def print_wrld(self):
        for slice in self.world.space:
            for cell in slice:
                try :
                    print (cell.value.symb, end='')
                except Exception as e :
                    pass
                    print (cell.value, end='')
            print()

    def get_points_around_range(self, side_length):
        x = self.x
        y = self.y
        left_border = x - side_length if ( x - side_length) > 0 else 0
        right_border = x + side_length if ( x + side_length) < (WIDTH-1) else WIDTH-1
        up_border =  y - side_length if ( y - side_length) > 0 else 0
        down_border =  y + side_length if ( y + side_length) < (HEIGHT-1) else HEIGHT-1


        mid = side_length
        result = []

        for level in range(up_border, y):
            # if level <= 0:
            #     result.append([])
            #     break
            up = self.world.space[level][ left_border : right_border+1]
            result.append(up)
            # for i in up:
            #     print("[" + (str(i.y) if isinstance(i.value, int) else str(i.value.symb)) + (" " if (i.y < 10 or not isinstance(i.value, int)) else "") +"]", end='')
            # print()
        middle = self.world.space[y][left_border : x] +[Point(9, 9, 9)]+ self.world.space[y][x+1: right_border+1]
        result.append(middle)
        # for i in middle:
        #     print("[" + (str(i.y) if isinstance(i.value, int)  else str(i.value.symb))  + (" " if (i.y < 10 or not isinstance(i.value, int)) else "") + "]", end='')
        # print()
        for level in range(y+1, down_border):
            # if level >= HEIGHT-1:
            #     result.append([])
            #     break
            down = self.world.space[level][left_border : right_border+1]
            result.append(down)
            # for i in down:
            #     print("[" + (str(i.y) if isinstance(i.value, int) else str(i.value.symb))  + (" " if (i.y < 10 or not isinstance(i.value, int)) else "") + "]", end='')
            # print()



        return result

