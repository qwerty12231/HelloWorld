print("Введите a:")   # количество километров в первый день
a = int(input())
print("Введите b:")   # количество километров в последний день
b = int(input())
s = a
k = 1                 # единица дня
while s <= b:
    k = k + 1
    s = 1.1 * s
print("на:", k, "день спорсмен достиг результата не менее:", b, "километров.")
