import math

class circle:
    def __init__(self,radius):
        self.radius=radius
    def set_radius(self):
        self.radius=radius
    def get_radius(self):
        return self.radius
    def __add__(self,circle_obj,c3):
        return (self.radius+circle_obj.radius+c3.radius)

c1=circle(2)
c2=circle(3)
c3=circle(4)

print(c1+c2+c3)
