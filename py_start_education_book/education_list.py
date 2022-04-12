# метод enumerate()
'''
names=['Nikita', 'Darya', 'Ekaterina', 'Dmitriy', 'Vladmir']
for idx, name in enumerate(names, start=1):
    print(idx,name)
'''
#метод zip
'''
kolp=('12', '124', '441')
names=['Никита', 'Дарья','Екатерина','Дмитрий']
ages=[32, 28, 37, 53]
gender=['Мужчина', 'Женщина', 'Женщина', 'Мужчина']
zipped=zip(names, ages, gender)

print(*zipped)
'''
#метод zip_longest
'''
from itertools import zip_longest
id=[1,2]
leaders=['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']
long_records=zip_longest(id,leaders, fillvalue='AAA')
'''
#List compression
'''
cart=[12, 5, 123, 2, 6, 75]
carshier=[item for item in cart if item%2>0 or item>100]
print(carshier)
'''
