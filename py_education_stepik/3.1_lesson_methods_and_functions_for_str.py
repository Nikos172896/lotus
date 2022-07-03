#вхождение и замена строки в подстроку
'''
s = input()
a = input()
b = input()
in_s = 0
while s.count(a) > 0 and in_s <= 1000:
    s = s.replace(a, b)
    in_s += 1
if in_s >= 1000:
    print('Impossible')
else:
    print(in_s)
'''
#проверка количества пересекаемых вхождений
import regex
s = input()
t = input()
print(regex.findall(t, s, overlapped=True))


