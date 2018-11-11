import functools
def normal(func):

    print(func(100))





normal(lambda x: x/2)



def paranormal(func, *args):

    print(func(100))

    for argument in args:

        print(argument)



paranormal(lambda x: x/5, 1,2,3,4,5)



def mystery(func, *args):

    print(func(100))

    for argument in args:

        print('Here you go; {:^100.1f}'.format(func(argument)))

mystery(lambda x: x/5, 1,3,5,7,9)

def normal_function(arg_func, *arg):
    for name in arg:
         print('{:^20}'.format(arg_func(name)))
 
normal_function(lambda el: 'Euro ' + str(el),1.6, 1.45)
final_str = functools.reduce(lambda el, fstring:str(el) + fstring,['Euro ',1.6, 1.45],'')
print(final_str)