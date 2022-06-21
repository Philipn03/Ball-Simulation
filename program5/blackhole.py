# A Black_Hole is derived from a Simulton base; it updates by finding+removing
#   any objects (derived from a Prey base) whose center is crosses inside its
#   radius (and returns a set of all eaten simultons); it displays as a black
#   circle with a radius of 10 (e.g., a width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton): 
     
    radius = 10
    
    def __init__(self,x,y,width=20,height=20):
        Simulton.__init__(self,x,y,width,height)
        
    def update(self, model):
        eaten_s = set()
        s = model.find(lambda x: isinstance(x,Prey))
        for i in s:
            if self.contains(i):
                eaten_s.add(i)
                model.remove(i)
        return eaten_s
        
    
    def display(self, canvas):
    
        x = super().get_location()[0]
        y = super().get_location()[1]
        canvas.create_oval(x-super().get_dimension()[0]/2,y-super().get_dimension()[0]/2, x+super().get_dimension()[0]/2, y+super().get_dimension()[0]/2, fill='#000000')
        
    def contains(self,xy):
        try:
            d = xy.get_location()
            center = super().distance(d)
            if center < Black_Hole.radius:
                return True
            return False
        except:
            return self._x - self._width/2  <= xy[0] <= self._x + self._width/2 and\
               self._y - self._height/2 <= xy[1] <= self._y + self._height/2
