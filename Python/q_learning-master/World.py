import numpy as np
from threadsafe_tkinter import *
master = Tk()

class World(object):
    def __init__(self, width, axis_x, axis_y):
        # static 
        self.WIDTH = width
        (self.AXIS_X, self.AXIS_Y) = (axis_x, axis_y)
        self.WALK_REWARD = -0.04
        self.ACTIONS = [["up", 0, -1], ["down", 0, 1], ["left", -1, 0], ["right", 1, 0]]
        self.N_OBJECTS = round((axis_x * axis_y) / 4)

        # Init objects, then add special green square
        self.OBJECTS = self.init_objects(axis_x, axis_y)
        x_green, y_green = self.gen_pos()
        self.OBJECTS.append((x_green, y_green, "green", 5))
        
        # init remaining variables
        self.board = Canvas(master, width=self.AXIS_X*self.WIDTH, height=self.AXIS_Y*self.WIDTH)
        self.score = 1
        self.restart = False 
        self.Player = self.gen_pos()
        self.me = self.board.create_rectangle(self.Player[0]*self.WIDTH+self.WIDTH*2/10, self.Player[1]*self.WIDTH+self.WIDTH*2/10,
            self.Player[0]*self.WIDTH+self.WIDTH*8/10, self.Player[1]*self.WIDTH+self.WIDTH*8/10, fill="orange", width=1, tag="me")

    def init_objects(self, axis_x, axis_y):
        objects = set([])
        n_of_red_squares = round(self.N_OBJECTS / 5)
        
        for i in range(self.N_OBJECTS):
            # First add N amount of walls, then add N amount of OBJECTS to objects
            if i < n_of_red_squares:
                # add red squares
                objects.add((np.random.randint(0, axis_x), np.random.randint(0, axis_y), "red", -5))
            else:
                #add walls
                objects.add((np.random.randint(0, axis_x), np.random.randint(0, axis_y), "black", -1))
                
        return list(objects)
    
    def gen_pos(self):
        while True:
            x = np.random.randint(0, self.AXIS_X)
            y = np.random.randint(0, self.AXIS_Y)
            check_for_rows = [e for e in self.OBJECTS if x == e[0] and y == e[1]]

            if not check_for_rows:
                break
        return (x, y)
    
    def render_grid(self):
        for i in range(self.AXIS_X):
            for j in range(self.AXIS_Y):
                # Check if objects for current coordinates
                objects = [e for e in self.OBJECTS if i == e[0] and j == e[1]]

                if objects and ((i, j) == objects[0][0:2]):
                    self.board.create_rectangle(i*self.WIDTH, j*self.WIDTH, (i+1)*self.WIDTH, 
                        (j+1)*self.WIDTH, fill=objects[0][2], width=1)
                else:
                    self.board.create_rectangle(i*self.WIDTH, j*self.WIDTH, (i+1)*self.WIDTH, 
                        (j+1)*self.WIDTH, fill="white", width=1)
                    
    def start_game(self):
        master.mainloop()

    def try_move(self, dx, dy):
        if self.restart:
            restart_game()
        new_x = self.Player[0] + dx
        new_y = self.Player[1] + dy
        self.score += self.WALK_REWARD
        
        if (new_x >= 0) and (new_x < self.AXIS_X) and (new_y >= 0) and (new_y < self.AXIS_Y) and not ((new_x, new_y) in self.OBJECTS):
            self.board.coords(self.me, new_x*self.WIDTH+self.WIDTH*2/10, new_y*self.WIDTH+self.WIDTH*2/10, 
                new_x*self.WIDTH+self.WIDTH*8/10, new_y*self.WIDTH+self.WIDTH*8/10)
            
            self.Player = (new_x, new_y)
        
        for (i, j, c, w) in self.OBJECTS:
            if new_x == i and new_y == j:
                self.score -= self.WALK_REWARD
                self.score += w
                if self.score > 0:
                    print("Success! score: ", self.score)
                else:
                    print("Fail! score: ", self.score)
                self.restart = True
                return
    

    def restart_game(self):
        self.Player = self.gen_pos()
        self.score = 1
        self.restart = False
        self.board.coords(self.me, self.Player[0]*self.WIDTH+self.WIDTH*2/10, 
            self.Player[1]*self.WIDTH+self.WIDTH*2/10, self.Player[0]*self.WIDTH+self.WIDTH*8/10, 
            self.Player[1]*self.WIDTH+self.WIDTH*8/10)

    def has_restarted(self):
        return self.restart