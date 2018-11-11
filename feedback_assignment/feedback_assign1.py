#1 Create two variables – one with your name and one with your age
 
my_age = 37
my_name = 'Ricardo'
 
#2 Create a function which prints your data as one string
print(str(my_age) + my_name)

#3 Create a function which prints ANY data (two arguments) as one string
i1= input('Enter data 1')
i2= input ('Enter data 2')
def Printing_two_arguments(e1,e2):
    print(e1+''+e2)
Printing_two_arguments(i1,i2)

#4 Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)
def how_many_decades_have_i_lived():
     return int(my_age/10)


print (how_many_decades_have_i_lived())
