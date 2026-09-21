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
    def acute_obtuse_triangle(self):
        if self.angle1<90 and self.angle2<90 and self.angle3<90:
            print('This is acute triangle')
        elif self.angle1>=90 and self.angle1<=180 or self.angle2>=90 and self.angle2<=180 or self.angle3>=90  and self.angle3<=180:
            print('This is Obtuse_triangle')
            
            

a,b,c=[int(x.strip()) for x in  input('Enter three angles  Saparated by Commas:').split(',')]
assert a>0 and b>0 and c>0,'Please enter the angles >0'
tri=Triangle(a,b,c)
if tri.check_angles():
    tri.acute_obtuse_triangle()
            
