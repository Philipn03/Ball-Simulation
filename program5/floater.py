# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


# from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey): 
    
    radius = 5
    
    def __init__(self,x,y,width=10,height=10,angle=90,speed=5):
        Prey.__init__(self,x,y,width,height,angle,speed)
        super().randomize_angle()
        
    def update(self,model):
        if model.cycle_count % 3 == 0:
            random_speed = random()
            random_angle = random()
            
            if random_speed < .5:
                random_speed -= .5
            if random_angle < .5:
                random_angle -= .5
                
            new_speed = super().get_speed() + random_speed
            new_angle = super().get_angle() + random_angle
            
            if new_speed < 3:
                new_speed = 3
            elif new_speed > 7:
                new_speed = 7
                
            super().set_speed(new_speed)
            super().set_angle(new_angle)
        
        super().move()
    
    def display(self, canvas):
        x = super().get_location()[0]
        y = super().get_location()[1]
        canvas.create_oval(x-Floater.radius,y-Floater.radius, x+Floater.radius, y+Floater.radius, fill='#FF0000')
