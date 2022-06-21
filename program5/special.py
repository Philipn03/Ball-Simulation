# This special ball acts like a ball but whenever the special ball
# bounces off a wall, it changes color. 

import random, math
from prey import Prey
import model


class Special(Prey): 
    
    radius = 5

    def __init__(self,x,y,width=10,height=10,angle=90,speed=5):
        Prey.__init__(self,x,y,width,height,angle,speed)
        super().randomize_angle()
        self.color = "#0000FF"

    def random_color(self):
        return "#"+str(hex(random.randint(20,255)))[2:]+str(hex(random.randint(20,255)))[2:]+str(hex(random.randint(20,255)))[2:]

    def update(self, model):
        super().move()
          
    def display(self, canvas):
        x = super().get_location()[0]
        y = super().get_location()[1]
        canvas.create_oval(x-Special.radius,y-Special.radius, x+Special.radius, y+Special.radius, fill=self.color)
        
    def bounce(self,barrier_angle):
        self._angle = 2*barrier_angle - self._angle
        self.color = self.random_color()
        
 
