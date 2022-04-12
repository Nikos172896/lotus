#38 арифметические операторы
'''
a, b, c = 2, 4, 8
print('\ndefoult order\t', a, '*', c,'+', b, '=', a*c+b, sep='')
print('\nforced order\t', a, '*(', c,'+', b, ')=', a*(c+b), sep='')

print('\ndefoult order\t', a, '*', c,'+', b, '=', a*c+b, sep='')
'''
#41 типы переменных
'''
a = input( 'Enter a number:\t')
b = input( 'Now enter another number: \t')
sum = a + b
print('\nData Type sum:', sum, type(sum))

sum = int(a) + int(b)
print('Data Type sum:', sum, type(sum))

sum = float(sum)
print('Data type sum', sum, type(sum))

sum = chr(246)
print('Data Type sum:', sum, type(sum))
'''
#43 побитное сдвижение
'''
a, b = 10, 5
print('a=', a, '\tb= ', b)
#1010 ^ 0101 = 1111(десятичное 15)
a = a ^ b
print (a,b)
#1111 ^ 0101 = (десятичное 10)
b = a ^ b
print (a,b)
#1111 ^ 0101 (десятичное 5)
a = a ^ b
print('a=', a, '\tb= ', b)
'''
#47 списки\многомерные списки
'''
quarter=['January', 'February', 'March']

print ('first month:\t', quarter[0])
print ('second month:\t', quarter[1])
print ('third month:\t', quarter[2])

coords= [[1,2,3],[4,5,6]]
print('\nTop left 0,0:\t', coords [0][0])
print('Bottom right 1,2 :', coords[1][2])
print('\nSecond Month First letter: ', quarter[1][0])
'''
#49 списки
'''
basket= ['Apple', 'Bun', 'Cola']
crate= ['Egg', 'Fig', 'Grape']
print('Basket List', basket)
print ('Basket elements:', len(basket))
basket.append('Damson')
print ('Appended:', basket)
print('Last Item removed:', basket.pop())
print('Basket List:', basket)

basket.extend(crate)
print('Extended: ', basket)
del basket[1]
print ('item removed:', basket)
print('Slice removed', *basket)
'''
#51 кортеж, множества
'''
zoo = ('Kangaroo', 'Leopard', 'Moose')
print('Tuple:', zoo, '\tLength:', len(zoo))
print(type(zoo))
bag = {'red', 'green', 'blue'}
bag.add('yellow')
print('\nSet:', bag, '\tLength', len(bag))
print (type(bag))
print('\nGreen is bag set?:', 'green' in bag)
print('Is orange in bag set?:', 'orange' in bag)
box = {'red', 'purple', 'yellow'}
print('\nSer:', box, '\t\tLength', len (box))
print('Common to both sets:', bag.intersection(box))
print('difference:', box.difference(bag))
'''
#53 словари
'''
dict={'name':'Bob', 'ref':'Python', 'sys':'Win'}
print('Dictionary:', dict)
print('\nReference:', dict['ref'])
print('\nKeys:', dict.keys())
del dict['name']
dict['user']='Tom'
print('Dict:', dict)
print ('da') if 'ref' in dict else print('no')
'''
#55 ветвление
'''
num = int(input('Please enter a number: '))
if num>5:
    print('Number Exceeds 5')
elif num<5:
    print(' Number is less than 5')
else:
    print('Number is 5')
'''
#57 цикл while
'''
i = 1
while i<4:
    print('\nOuter loop iteration ', i)
    i+=1
    j=1
    while j<4:
        print('\tInner Loop iteration: ', j)
        j+=1
'''
#59 цикл for
'''
chars=['A', 'B', 'C', 'D', 'E']
fruit=('Apple', 'Banana', 'Cherry', 'Mango')
dict={'name':'Mike', 'ref':'Python', 'sys':'Win'}
print('\nElements:\t', end='')
for item in chars:
    print(item, end='')
print ('\nEnumerated:\t', end='')
for item in enumerate(chars):
    print(item, end='')
print('\nZipped:\t', end='')
for item in zip(fruit, chars):
    print(item, end='')
print('\nPaired:')
for key, value in dict.items():
    print(key, '=', value, end='\t')
    if value=='Mike':
        print(end='\t')
'''
#60 цикл с break
'''
for i in range(1,4):
    for j in range(1,4):
        if i==1 and j==1:
            print('Continues inner loop at i=1 j=1')
            continue
        if i==2 and j==1:
            print('breaks inner loop at i=2 j=1')
            break
        print('Running i=', i, 'j=', j)
'''
#72 добавление заполнителей
'''
bool = True
if bool:
    print('Python in Easy Steps')
else:
    pass
    #сюда добавляем операторы
'''
#76 Обработка исключений
'''
title = 'Python in easy steps'
try:
    print(titel)
except (NameError, IndexError) as msg:
    print(msg)
'''
'''
day=32
try:
    if day>31:
        raise ValueError('Invalid Day Number')
except ValueError as msg:
    print('The program found An', msg)
finally:
    print('But Today Is Beautiful Anyway.')
'''
#Системные запросы sys, keyword
'''
import sys, keyword

print('Python Version: ', sys.version)
print('Python interpreter location:', sys.executable)
print('Python Modules Search Path: ')
for dir in sys.path:
    print(dir)
print('Python Keywords: ')
for word in keyword.kwlist:
    print(word)
'''
#88 математические операции библиотке math
'''
import math, random
print('Rounded Up 9.5', int(math.ceil(9.5)))
print('Rounded down 9.5', math.floor(9.5))
num=4
print(num, 'Squared', int(math.pow(num,2)))
print(num, 'Square root', math.sqrt(num))
nums= random.sample(range(1,49), 6)
print ('Your Lucky lotto Numbers Are:', nums)
'''
#90 Вычисления с десятичными дробями
'''
from decimal import *
item = Decimal(0.71)
rate = Decimal(1.05)

tax=item * rate
total = item + tax
print('Item:\t', '%.2f' % item)
print('Taz:\t', '%.2f' % tax)
print ('Total:\t', '%.2f' % total)
'''
#93 Работа со временем модуль datetime
'''
from datetime import *
today = datetime.today()

for attr in ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
    print (attr, ':\t', getattr(today, attr))
print('Time:', today.hour, ':', today.minute, sep = '')
day=today.strftime('%A')
month=today.strftime('%B')
print('Date:', day, month, today.day)
'''
#94 Работа со временем модуль time
'''
from time import *
start_timer=time()
struct=localtime(start_timer)
print('\nStarting Countdown At:', strftime('%X', struct))

i=10
while i>-1:
    print(i)
    i-=1
    sleep(1)
end_timer=time()
difference=round(end_timer-start_timer)
print(end_timer)
print('\nRuntime:', difference, 'Seconds')
'''
#96 шаблоны соответсвий
'''
from re import *
pattern=compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)' )

def get_address(a=0):
    while a==0:
        address = input('Enter Your Email Address: ')
        is_valid=pattern.match(address)
        if is_valid:
            print ('Valid Address! ', is_valid.group())
            a=1
        else:
            print('Invalid Address ! Please Retry...\n')
get_address()
'''