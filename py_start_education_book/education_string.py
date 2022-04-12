#73 добавление заполнителей continue, pass
'''
title= '\nPython in easy steps\n'
for char in title:print(char, end=' ')

for char in title:
    if char=='y':
        print('*', end=' ')
        continue
    print(char, end=' ')
'''
#замена символа предыдущего перед Y на | просто вывыод
#выборочный вывод строки
'''
l=0
for char in title:
    if l!=len(title):
        if title[l+1]=='y':
            print('|', end=' ')
            l+=1
            continue
    print(char, end=' ')
    l+=1
'''
#замена символа предыдущего перед Y на | изменяя строку
#метод строки .count(), .find(), .replace()
'''
title= 'yPython in easy stepsy'
fsym=-1
for i in range(title.count('y')):
    fsym = title.find('y', fsym + 1)
    if fsym!=0:
        title=title.replace(title[fsym-1], '|', 1)
    print(title[fsym-1])
print(title)
'''
#замена символа предыдущего перед Y на | строка в список
#метод строки .list(), ''.join()
'''
title= 'yPython in easy stepsy'
tlist=list(title)
print(tlist)
for i in range(len(tlist)):
    if tlist[i]=='y':
        if i!=0:
            tlist[i-1]='|'
        else: continue
print(tlist)
title=''.join(tlist)
print(title)
'''
#метод .split()
'''
my_string='I code for 2 hours everyday'
my_string=my_string.split()
print(my_string)
my_string='Apples,Oranges,Pears, Bananas, Berries'
print(my_string.split(',',2))
'''
#метод ''.join()
'''
my_list=my_string.split(',')
print(', '.join(my_list))
'''
#str.format(), аргументы позиций
'''
print('Hello, my name is {}.I am a {} turned {}.'\
      .format('Jessica', 'musician', 'programmer'))
print('Steve plays {1} and {0}.'.format('trumpet', 'drums'))
'''
#str.format(), аргументы ключи
'''
print('{organization} is {adjective}!'\
      .format(organization='Pythonist', adjective='awesome'))
'''
#Именованные и позиционные ключи
'''
name='Sam'
adjective='amazing'
number=200
disney_ride='Space Mountain'
print('I wend to {0} with {name}.\nIt was {adjective}.\
        \nWe waited for {hours} hours to ride {ride}'\
    .format('Disneyland', name=name, adjective=adjective,\
    hours=number, ride=disney_ride))
'''
# F строки
'''
name='Jessica'
print(f'Maria and {name}, have been friend since grade school')
'''
# F строки форматирование словаря
'''
rankings={'Gonzaga':31, 'Baylor':28, 'Michigan':25,\
          'Illinois':24, 'Houston':21}
for team, score in rankings.items():
    print(f'{team:10}==>{score:4d}')
'''
# шаблонные строки
'''
from string import Template
print(Template('I love to learn with $name!')\
      .substitute(name='Pythonist'))
'''
#100 работа со строками
'''
def display(s):
   Выводим значение аргумента
    print(s)
display(display.__doc__)
display(r'C:\Programm files')
display('\nHello'+' Python')
display('Python In Easy Steps\n'[7:])
display('p' in 'Python')
display('P' in 'Python')
'''
#103 форматирование строк
'''
snack='{1} and {0}'.format('Burger', 'Fries')
print('\nReplaced:', snack)
snack='%s and %s' %('Milk', 'Cookies')
print('\nSubstituted:', snack)
'''
#104 модификация строк object str
'''
string='python is easy steps'
print('\nCapitalized:\t', string.capitalize())
print('\nTitled:\t\t', string.title())
print('\nCentered:\t', string.center(30, '*'))

print('\nUppercase:\t', string.upper())
print('\nJoined:\t\t', string.join('**'))

print('\nJustified:\t', string.rjust(30, '*'))
print('\nReplaced:\t', string.replace('s', '*'))
'''
#106 преобразование строк ASCII и Unicode
'''
s='Röd'
print('\nRed String:', s)
print('Type:', type(s), '\tLentgh:', len(s))

s=s.encode('utf-8')
print('\nEncoded String:', s)
print('Type:', type(s), '\tLength: ', len(s))

s=s.decode('utf-8')
print('nDecode String:', s)
print('Type:', type(s), '\tLength:', len(s))

import unicodedata
for i in range(len(s)):
    print(s[i], unicodedata.name(s[i]), sep=':')
s=b'Gr\xc3\xb6n'
print('\nGreen String:' , s.decode('utf-8'))

s='Gr\N{LATIN SMALL LETTER O WITH DIAERESIS}n'
print('Green String:', s)
'''
