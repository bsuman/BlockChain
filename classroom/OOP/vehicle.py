class Vehicle:
        
        def __init__(self, starting_top_speed=10):
            self.top_speed = starting_top_speed
            self.__warning = []

        def __repr__(self):
            print('printing own impl')
            return 'Top speed : {} ,  Warnings: {}'.format(self.top_speed,self.__warning)

        def add_warning(self, warning):
            if len(warning)> 0:
                self.__warning.append(warning)

        def drive(self):
            print('I am dirving not more than speed {}'.format(self.top_speed))

        def get_warning(self):
            return self.__warning