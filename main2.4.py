my_str = input("введите строку из нескольких слов ")
x = []
num = 1
for el in range(my_str.count(' ') + 1):
    x = my_str.split()
    if len(str(x)) <= 10:
        print(f" {num} {x [el]}")
        num += 1
    else:
        print(f" {num} {x [el] [0:10]}")
        num += 1