# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10). 


from prey import Prey


class Ball(Prey): 
    radius = 5
    def __init__(self,x,y,width=10,height=10,angle=90,speed=5):
        Prey.__init__(self,x,y,width,height,angle,speed)
        super().randomize_angle()
    
    def update(self, model):
        super().move()
    
    def display(self, canvas):
        x = super().get_location()[0]
        y = super().get_location()[1]
        canvas.create_oval(x-Ball.radius,y-Ball.radius, x+Ball.radius, y+Ball.radius, fill='#0000FF')