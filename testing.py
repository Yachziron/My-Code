def func_bace(*args, **kwargs):
    print(*args)
    print('kwargs', kwargs)
    key = (func_bace.__name__,) + tuple(args) + tuple(kwargs.items())
    print(key)

func_bace(1, 2, 3, 4, 5, 23, a=12, b=16, c=75)

