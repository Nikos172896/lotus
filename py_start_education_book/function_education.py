#65 область видимости в функицях
'''
global_var=1
def my_vars():
    print('global Variable:', global_var)
    local_var=2
    print ('Local variable:', local_var)
    global inner_var
    inner_var=3
my_vars()
print('Coerced global:', inner_var)
'''
#67 подстановка аргументов в функцию
'''
def echo(user, lang, sys):
    print ('User:', user, '\nLanguage:', lang, '\nPlatform:', sys)
#echo('Mike', 'Python', 'Windows')
#echo(lang = 'Python', sys='Mac OS', user='Anne')
def mirror(user='Carole', lang='Python'):
    print('\nUser:', user, 'Language', lang)
mirror()
mirror(lang='Java')
mirror(user='Tony')
mirror('Susan', 'C++')
'''
#69 возвращение значений
'''
num=input('Enter an integer:')
def square(num):
    if not num.isdigit():
        return 'Invalid Entry'
    num=int(num)
    return num*num

print (num, 'Squared is:', square(num))
'''
#71 использование обратного вызова lambda
'''
def function_1(x): return x**2
def function_2(x): return x**3
def function_3(x): return x**4
callbacks=[function_1, function_2, function_3]
print('\nNamed Functions: ')
for function in callbacks: print('Result: ', function(3))
callbacks= [lambda x : x**2, lambda x : x**3, lambda x : x**4]
print('\nAnonymous Functions: ')
for function in callbacks: print('Result', function(3))
'''
#71 Генераторы в питоне
'''
def fibonacci_generator():
    a=b=1
    while True:
        yield a
        a, b= b, a+b
fib=fibonacci_generator()
for i in fib:
    if i > 100:
         break
    else:
        print('Generated:', i)
'''
'''
def counter():
    i=1
    while True:
        yield i
        i+=1
        n=input()
        if n=='k': break
for i in counter():
    print(i)
'''

