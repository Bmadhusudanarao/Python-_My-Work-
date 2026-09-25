from abc import ABC, abstractmethod
import math
class Myclass(ABC):
    @abstractmethod
    def calculate(self,x):
        pass


class sub1(Myclass):
    def calculate(self,x):
        print('The square value:',x*x)
class sub2(Myclass):
    def calculate(self,x):
        print('The suqare root value:',math.sqrt(x))
class sub3(Myclass):
    def calculate(self,x):
        print('The cubes value:',x*x*x)


obj1=sub1()
obj1.calculate(2)
obj2=sub2()
obj2.calculate(25)
obj3=sub3()
obj3.calculate(2)
