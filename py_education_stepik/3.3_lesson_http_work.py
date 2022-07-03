'''
import requests
import re

res1 = (input())
res2 = (input())

#достаем все url ссылки из страницы запроса
def readhtml(res):
    result = requests.get(res)
    print(result.text)
    if result.status_code == 200:
        return re.findall(r'<a href="(.*)">', result.text)
    else:
        return 'No'

#ищем где через 2 ссылки есть нужная
if readhtml(res1) != 'No' and readhtml(res2) != 'No':
    print(readhtml(res1))
    for i in readhtml(res1):
        if res2 in readhtml(i):
            k = 0
            print('Yes')
            break
        else:
            k = 1
    if k == 1:
        print('No')
else:
    print('No')
'''

import requests
import re

#скачиваем текст из страницы сайта и сохраняем
result = requests.get('https://pastebin.com/raw/7543p0ns')
lol= set()
with open('html_new.html', 'w+') as t:
    t.write(result.text)
with open('html_new.html', 'r') as t:
    file = t.read()

#ищем все названия сайтов формата google.com
for i in re.findall(r'<a.*href="(http://|ftp://|https://)?([.\w-]*\.\w{2,3}).*".*>', file):
    lol.add(i[1])
#сортируем по первому символу
lol = sorted(lol, key=lambda x: x[0])
print(len(lol))
for i in lol:
    print(i)