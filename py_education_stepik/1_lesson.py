'''
fib = lambda x : 1 if x <= 2 else fib(x - 1)+fib(x - 2)
volume_1=fib(31)
print(volume_1)
'''
sum=0
while True:
    kol_vo=input('Введите число от 1 до 100\n')
    try:
        kol_vo=int(kol_vo)
    except:
        print('Не верно')
    else:
        if kol_vo>=1 and kol_vo<=100:
            break
        else: print('Не верно')
for i in range(kol_vo):
    sum+=int(input())
print(kol_vo)
print(sum)