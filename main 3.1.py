# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def num(*args):

    try:
        arg1 = int(input("Input number1 "))
        arg2 = int(input("Input number2 "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Can't be divided by zero"

    return res


print(f'result  {num()}')