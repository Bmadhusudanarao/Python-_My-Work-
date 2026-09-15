Car={'x_position':10,'y_position':72,'speed':'Medium'}
print('Before modify the Disctionery')
for k,v in Car.items():
    print(k,':',v)
speed=input('enter the car speed')
if speed=='Slow':
    Car['x_position']=Car['x_position']+2
    Car['speed']=speed
elif speed=='Medium':
    Car['x_position']=Car['x_position']+9
    Car['speed']=speed
elif speed=='Fast':
    Car['x_position']=Car['x_position']+22
    Car['speed']=speed

print('After modify the Disctionery')
for k,v in Car.items():
    print(k,':',v)
