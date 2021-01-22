int("1234", 9)       # тип данных число
922
int("1234", 19)
7642

n = complex (4, 19)
n
(4+19j)

m = 9 - 7J
m
(9-7j)

n + m
(13+12j)

n -m
(-5+26j)

n * m
(169+143j)

n / m
(-0.7461538461538462+1.5307692307692307j)

n ** n
(4.172924525334652e-07-6.829595587205957e-07j)

# тип данных строка: конкатенация

"Good" + "looking"
'Goodlooking'

"Good" + "  " + "looking"
'Good  looking'

"Good" "  " "looking"
'Good  looking'

"Good" * 3
'GoodGoodGood'

"№" * 11
'№№№№№№№№№№№'

my_str = "Good looking."
my_str
'Good looking.'

# тип данных строка: индексы
my_str[1]
'o'
my_str[8]
'k'
my_str[-1]
'.'
my_str[-2]
'g'

my_str[0:4:1]
'Good'

my_str[0:-9]
'Good'

my_str[5:4000]
'looking.'
#обратная интерация
my_str = "Good looking."
my_str[::-1]
'.gnikool dooG'

len(my_str)
13

"3, 5, 8".split(" ")
['3,', '5,', '8']

"3,   5,     8".split(" ")
['3,', '', '', '5,', '', '', '', '', '8']

"3,   5,     8".split()
['3,', '5,', '8']

" ".join(["Green", "Park"])
'Green Park'

"-".join(["Green", "Park"])
'Green-Park'

"КонСтаНтин".title()
'Константин'

"КонСтаНтин КонСтаНтин КонСтаНтин КонСтаНтин КонСтаНтин".title()
'Константин Константин Константин Константин Константин'

"UsSr".upper()
'USSR'

"UsSr UsSr UsSr UsSr UsSr".upper()
'USSR USSR USSR USSR USSR'

"limpopo".count("po")
2

"limpopo".count("m")
1

"limpopo".count("a")
0

"limpopo".replace("po", " ")
'lim  '

"limpopo".replace("po", "")
'lim'

"limpopo".index("po")
3

"limpopo".index("po", 4)
5

"limpopo".index("po", 8)
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
ValueError: substring
not found

"limpopo".find("po")
3

"limpopo".find("po", 8)
-1

#cписок
list("limpopo")
['l', 'i', 'm', 'p', 'o', 'p', 'o']

list("limpo  po")
['l', 'i', 'm', 'p', 'o', ' ', ' ', 'p', 'o']

my_list = [14, 2.4, "str", False, [4, 6]]
my_list
[14, 2.4, 'str', False, [4, 6]]

[1, 2] + [4, 5]
[1, 2, 4, 5]

[1, 2] * 2
[1, 2, 1, 2]

len(my_list)
5

my_list[0]
14

my_list[-1]
[4, 6]

my_list[::-1]
[[4, 6], False, 'str', 2.4, 14]

my_list[0:3]
[14, 2.4, 'str']

my_list[4]
[4, 6]

my_list[10]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IndexError: list index out of range

my_list[2] = 55
my_list
[14, 2.4, 55, False, [4, 6]]

my_list.append(55)
my_list
[14, 2.4, 55, False, [4, 6], 55]

my_list.insert(3, 55)
my_list
[14, 2.4, 55, 55, False, [4, 6], 55]

my_list.count(55)
3

my_list.index(55)
2

my_list.reverse()
my_list
[55, [4, 6], False, 55, 55, 2.4, 14]

my_list[1]
[4, 6]
my_list[1][0]
4
my_list[1][1]
6
my_list[1][3]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IndexError: list index out of range

my_list.pop()
14
my_list
[55, [4, 6], False, 55, 55, 2.4]

my_list.pop(2)
False
my_list
[55, [4, 6], 55, 55, 2.4]

my_list.remove(55)
my_list
[[4, 6], 55, 55, 2.4]

#кортеж
tuple("limpopo")
('l', 'i', 'm', 'p', 'o', 'p', 'o')

my_tuple = (14, 2.4, 55, 55, False, [4, 6], 55, (3, 4))
my_tuple
(14, 2.4, 55, 55, False, [4, 6], 55, (3, 4))

my_tuple[0]
14
my_tuple[-1]
(3, 4)
my_tuple[3:5]
(55, False)
my_tuple
(14, 2.4, 55, 55, False, [4, 6], 55, (3, 4))

my_tuple[-3].append(5)
my_tuple
(14, 2.4, 55, 55, False, [4, 6, 5], 55, (3, 4))

my_tuple[-3].append([5, 8])
my_tuple
(14, 2.4, 55, 55, False, [4, 6, 5, [5, 8]], 55, (3, 4))

#множество
my_set = {14, 2.4, 55, 55, False, 55, (3, 4)}
my_set
{False, 2.4, (3, 4), 55, 14}

my_set.add("rty")
my_set
{False, True, 2.4, 'rty', (3, 4), 55, 14}
my_set.add(55)
my_set
{False, True, 2.4, 'rty', (3, 4), 55, 14}
my_set.add(22)
my_set
{False, True, 2.4, 'rty', (3, 4), 22, 55, 14}

my_set.remoove(55)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'set' object has no attribute 'remoove'
my_set.discard(55)
my_set
{True, 2.4, 'rty', (3, 4), 22, 14}

{1, 2} - {5, 6}
{1, 2}

{1, 2} | {1, 6, 2}
{1, 2, 6}

#cловарь
dict(M=55, r=4)
{'M': 55, 'r': 4}

#None
n = 0
n
0
