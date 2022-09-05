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
