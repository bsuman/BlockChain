from vehicle import Vehicle

class Car(Vehicle):
    
    def brag(self):
        print('Look how cool my car is! ')

temp_car = Car()
temp_car.add_warning('Check speed')
temp_car.drive()
print(temp_car)
print(temp_car.get_warning())

temp_car1 = Car(100)
temp_car1.drive()
print(temp_car1 )

temp_car2 = Car(200)
temp_car2.drive()
print(temp_car2)

print(temp_car.__dict__)
print(temp_car)
