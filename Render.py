from tkinter import Tk, Canvas
from config import HEIGHT, WIDTH, MULT, bgColor, SEQUENCE
from Entities import Puppy
from time import  sleep
from threading import Thread
from random import choice

class Render:
    def __init__(self):
        self.window = Tk()
        self.started = False
        self.window.protocol ('WM_DELETE_WINDOW', )
        self.canvas = Canvas(self.window, height=HEIGHT * MULT, width=WIDTH * MULT, bg=bgColor)
        self.canvas.pack ( )

        # self.canvas.bind("<1>", self.move)
        # self.canvas.bind("<2>", lambda event: Thread(target=self.lifecycle).start())


    def draw(self, obj_list):
        self.obj_list = obj_list
        for obj in obj_list:
            if isinstance(obj, Puppy):
                x = obj.x * MULT
                y = obj.y * MULT
                obj.id = self.canvas.create_rectangle (x, y, x + MULT, y + MULT,
                                                       fill="#" + str (choice (range (10, 99))) + str (
                                                           choice (range (10, 99))) + str (choice (range (10, 99))))
        # self.thread = Thread (target=self.rerender, daemon=True)
        self.canvas.bind("<1>",lambda event: Thread(target=self.rerender, daemon=True).start() if self.started != True else self.stop())
        self.canvas.bind("<2>",lambda event: print(event))
        self.canvas.bind("<2>",lambda event: self.new_puppy(event.x , event.y))


    def stop(self):
        self.started = False

    def new_puppy(self, x, y):
        obj = Puppy.new_puppy (x//MULT, y//MULT)
        x = obj.x * MULT
        y = obj.y * MULT
        obj.id = self.canvas.create_rectangle (x, y, x + MULT, y + MULT,
                                               fill="#" + str (choice (range (10, 99))) + str (
                                                   choice (range (10, 99))) + str (choice (range (10, 99))))
        self.obj_list.append (obj)


    def rerender(self):
        self.started = True
        # Thread (target=self.move, ).start ( )
        for i in self.obj_list :
            Thread (target=self.move, kwargs={'obj' : i}).start ( )

    def around(self, event):
        tmp = self.obj_list[0]
        tmp.look_around()
        tmp.print_wrld()


    def move(self, obj):
        while self.started:
            obj.move()
            self.canvas.coords(obj.id, obj.x * MULT, obj.y * MULT, obj.x * MULT + MULT, obj.y * MULT + MULT)
            sleep (SEQUENCE)
            # obj.x += x_mult #/ MULT
            # obj.y += y_mult #/ MULT

    def quit(self):
        self.started = False
        self.window.quit()

    # def lifecycle(self):
    #     print("aaa")
    #     while True:
    #         self.move(None, 0, 0)
    #         self.obj.x += choice(range(-1,2)) #/ MULT
    #         self.obj.y += choice(range(-1,2)) #/ MULT
    #         sleep(0.5)

