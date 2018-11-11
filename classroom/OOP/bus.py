from vehicle import Vehicle
class Bus(Vehicle):

    def __init__(self, starting_top_speed=10):
        super().__init__(starting_top_speed)
        self.__passengers=[]
        

    def add_group(self, passengers):
       self.__passengers.extend(passengers)

    def get_passengers(self):
        return self.__passengers

bus1=Bus(150)
bus1.add_warning('Check the speed limit not more than 80kms/per hr')
bus1.add_group(['Suman','Sugu','Vat'])
print(bus1.get_passengers())
bus1.drive()