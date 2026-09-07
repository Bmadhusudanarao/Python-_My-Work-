class Vehicle:
    def Fare(self,fare):
        return fare

Bus=Vehicle()
Car=Vehicle()
Train=Vehicle()
Truck=Vehicle()
Ship=Vehicle()
totalFare=Bus.Fare(float(input('enter the bus fare')))+Car.Fare(float(input('enter the Car fare:')))+Train.Fare(float(input('enter the Train fare:')))+Truck.Fare(float(input('enter the Truck fare:')))+Ship.Fare(float(input('enter the Ship fare:')))
print('The Total Fare:',totalFare)
