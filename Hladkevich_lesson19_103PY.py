def debug(func):
    def wrapper(a, b):
        print(f'Launch a funciton {func.__name__}, which has arguments: a = {a}'
              f' and b = {b}')
        print(f'Function result is {func(a, b)}')

    return wrapper


@debug
def func1(a, b):
    return a ** b


func1(4, 2)
