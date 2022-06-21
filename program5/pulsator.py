# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    
    counter_constant = 30
    
    def __init__(self,x,y,width=20,height=20):
        Black_Hole.__init__(self,x,y,width,height)
        self.count = 0
        
    def update(self, model):
        p = model.find(lambda x: isinstance(x,Pulsator))
       
        s = super().update(model)
        
        self.count += 1
        
        if len(s) == 1:
            super().change_dimension(1,1)
            self.count = 0
        elif self.count % Pulsator.counter_constant == 0:
            super().change_dimension(-1,-1)
        
        if super().get_dimension()[0] == 0 and super().get_dimension()[1] == 0:
            model.remove(self)
            
        return s
