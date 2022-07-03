#Работа со временем datetime
'''
import datetime
a,b,c=[i for i in input().split()]

date=datetime.date(int(a), int(b), int(c))
days=int(input())
delta=datetime.timedelta(days=days)
date=date+delta
print(date.year, date.month, date.day)
'''
import simplecrypt
import sys
with open("encrypted.bin", 'rb') as inp:
    encrypted=inp.read()
with open("passwords.txt", 'r') as txt:
    passwords=txt.read().split()
print(passwords)
print(encrypted)
for i in passwords:
    try:
        new_txt=simplecrypt.decrypt(i,encrypted)
    except:
        pass
print(new_txt)