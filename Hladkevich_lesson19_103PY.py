def debug(func):  # создание декоратора
    def wrapper(a, b):  # создание функции-обёртки
        print(f'Launch a funciton {func.__name__}, which has arguments: a = {a}'
              f' and b = {b}')  # вывод названия функции и её аргументов
        print(f'Function result is {func(a, b)}')  # вывод результата функции

    return wrapper


@debug
def func1(a, b):  # оборачиваемая функции
    return a ** b


func1(4, 2)  # вызов функции

# ============================================================================

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def decor(func):
    def wrapper(foo):
        count = 0
        for i in foo:
            for j in i:
                count += 1
        res = count - len(func(foo))
        print(func(foo))
        print(f'Amount of numbers that aren\'t multiples of 3 equal {res}')

    return wrapper


@decor
def func2(foo):
    bar = []
    for i in foo:
        for j in i:
            if j % 3 == 0:
                bar.append(j)
    return bar


func2(lst)
