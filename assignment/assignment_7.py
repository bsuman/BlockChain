
class Food:
    #1) Create a Food class with a “name” and a “kind” attribute 
    # as well as a “describe() ” method
    # (which prints “name” and “kind” in a sentence).

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    #def describe(self):
        #print('The food has the name: {} and is of the kind: {}'.format(self.name,self.kind))

    #2) Try turning describe()  from an instance method into a
    # class and a static method. Change it back to an instance method thereafter.
    
    #@classmethod
    #def describe(cls,name,kind):
        #print('The food has the name: {} and is of the kind: {}'.format(name,kind))

    #@staticmethod
    #def describe(name,kind):
        #print('The food has the name: {} and is of the kind: {}'.format(name,kind))
    
    def describe(self):
        print('The food has the name: {} and is of the kind: {}'.format(self.name,self.kind))

    #4) Overwrite a “dunder” method to be able to print your “Food” class

    def __repr__(self):
        return str(self.__dict__)

my_food = Food('Tea','Cooked')
my_food.describe()

print(my_food)
#Food.describe(my_food.name,my_food.name)

#3) Create a  “Meat” and a “Fruit” class – both should inherit from “Food”.
# Add a “cook() ” method to “Meat” and “clean() ” to “Fruit”.

class Meat(Food):

        #def __init__(self, name, kind):
            #super().__init__(name,kind)

        def cook(self):
            print('Method cook was called')

my_meat =  Meat('chicken','non-veg')
my_meat.describe()
my_meat.cook()


class Fruit(Food):

        def __init__(self,name,kind, freshness_level=0.0):
            super().__init__(name,kind)
            self.freshness_level =  freshness_level

        def clean(self):
            print('Current freshness level:{} of the fruit with name:{} and kind:{}'.format(self.freshness_level, self.name, self.kind))
            print('After cleaning increased to new freshness level {}'.format(str(self.freshness_level + 1)))

my_fruit = Fruit('Apple','Raw',0.5)
my_fruit.describe()
my_fruit.clean()
print(my_fruit)