def type_logger(func):
    def wrapper(*args, **kwargs):
        print(x, type(x))
        return func(*args, **kwargs)

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


x = 5
a = calc_cube(x)
print(a)
