class Triangle:
    def __init__(self,angle1,angle2,angle3):
        self.angle1=angle1
        self.angle2=angle2
        self.angle3=angle3
        self.number_of_sides=3
    def check_angles(self):
        if self.angle1+self.angle2+self.angle3==180:
            print('These Angles belongs to Triangle formation')
        else:
            print('Do not form a valid tringle')



a,b,c=[int(x.strip()) for x in  input('Enter three angles  Saparated by Commas:').split(',')]
assert a>0 or b>0 or c>0,'Please enter the angles >0'
tri=Triangle(a,b,c)
tri.check_angles()
            
