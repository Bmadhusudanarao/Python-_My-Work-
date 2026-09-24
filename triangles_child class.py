class Triangle:
    def __init__(self,angle1,angle2,angle3):
        self.angle1=angle1
        self.angle2=angle2
        self.angle3=angle3
        self.number_of_sides=3
    def check_angles(self):
        if self.angle1+self.angle2+self.angle3==180:
            print('These Angles belongs to Triangle formation')
            return True
        else:
            print('Do not form a valid tringle')
            return False
  
class isoceles_triangle (Triangle):
    def iso_tri(self):
        if self.angle1==self.angle2 or self.angle1==self.angle3 or self.angle2==self.angle3:
            print('this is Isosceles triangle')
            
class right_triangle(Triangle):
    def right_tri(self):
        if self.angle1==90 or self.angle2==90 or self.angle3==90:
            print('This is Right Triangle')
class equilateral_triangle(Triangle):
    def equilateral_tri(self):
        if self.angle1==60 and self.angle2==60 and self.angle3==60:
            print('This is equilateral triangle')


a,b,c=[int(x.strip()) for x in  input('Enter three angles  Saparated by Commas:').split(',')]
assert a>0 and b>0 and c>0,'Please enter the angles >0'

iso=isoceles_triangle(a,b,c)
if iso.check_angles():
    iso.iso_tri()
    right=right_triangle(a,b,c)
    right.right_tri()
    equilateral=equilateral_triangle(a,b,c)
    equilateral.equilateral_tri()
