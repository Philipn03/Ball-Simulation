# A Hunter class is derived from a Pulsator and then Mobile_Simulton base.
#   It inherits updating+displaying from Pusator/Mobile_Simulton: it pursues
#   any close prey, or moves in a straight line (see Mobile_Simultion).


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):  
    
    distance = 200
    
    def __init__(self,x,y):
        Pulsator.__init__(self,x,y)
        Mobile_Simulton.set_speed(self,5)
        Mobile_Simulton.randomize_angle(self)
        
    def update(self, model):
        s = model.find(lambda x: isinstance(x,Prey))
        new = set()
        for i in s:
            if super().distance(i.get_location()) <= 200:
                new.add(i)
                
        if len(new) != 0:
            c = sorted(new, key=lambda x: x.distance(self.get_location()))[0]
            xy_coord = c.get_location()     
            hunter_xy = self.get_location()
            
            dis_x = xy_coord[0] - hunter_xy[0]
            dis_y = xy_coord[1] - hunter_xy[1]
            
            self.set_angle(atan2(dis_y,dis_x))
            
        Pulsator.update(self, model)
        super().move()
        
            
            
            
        
         
