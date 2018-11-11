def norm_func(fn):
    print(fn(10))


def norm_func1(fn, *args):
    for args in args:
        print('output is {:^20}'.format(fn(args)))

norm_func(lambda num: num % 2)
norm_func1(lambda num:num % 2, 1,2,3,4,5)
