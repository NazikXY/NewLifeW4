from World import  World
from Entities import Puppy
from Render import Render
from random import randint
from config import *

wld = World("first")
obj_list = []


delim = 20
print(WIDTH * HEIGHT //delim)
for i in range(WIDTH * HEIGHT // delim):
    obj_list.append(Puppy(randint(0, WIDTH-1), randint(0, HEIGHT -1), wld))

render = Render()

render.draw(obj_list)


render.window.mainloop()

# for i in range(HEIGHT):
#     for a in range(WIDTH):
#         if (i != puppy.y) or (a != puppy.x):
#             print("_", end='')
#         else:
#             print(puppy.symb, end='')
#
#     print()