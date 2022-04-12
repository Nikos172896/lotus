#38
'''
a, b, c = 2, 4, 8
print('\ndefoult order\t', a, '*', c,'+', b, '=', a*c+b, sep='')
print('\nforced order\t', a, '*(', c,'+', b, ')=', a*(c+b), sep='')

print('\ndefoult order\t', a, '*', c,'+', b, '=', a*c+b, sep='')
'''
#41
a = input( 'Enter a number:\t')
b = input( 'Now enter another number: \t')
sum = a + b
print('\nData Type sum:', sum, type(sum))

sum = int(a) + int(b)
