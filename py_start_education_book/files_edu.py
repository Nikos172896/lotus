#основная работа с файлами
'''
file=open('examlpe.txt', 'w')
print('File Name:', file.name)
print('File Open Mode:', file.mode)

print('Readable:', file.readable())
print('Writeble:', file.writable())

def get_status(f):
    if (f.closed != False):
        return 'Closed'
    else:
        return 'Open'

print('File Status:', get_status(file))
file.close()
print('\nFile Status:', get_status(file))
'''

#110 Чтение и запись файлов
'''
poem='I never saw a man who looked\n'
poem+='With such a wistful eye\n'
poem+='Upon that little tent of blue\n'
poem+='Which prisoners call the sky\n'
file=open('poem.txt', 'w')
file.write(poem)
file.close()

file=open('poem.txt', 'r')

for line in file:
    print(line, end='')
file.close()

file=open('poem.txt', 'a')
file.write('(Oscar Wilde)')
file.close()
'''
#112 изменение текстового файла
'''
text='The political slogan "Workers Of The World Unite!" is from The Comunist Manifesto.'
with open('update.txt', 'w') as file:
    file.write(text)
    print('\nFile Now Closed?:', file.closed)
print('File Now Closed?:', file.closed)
with open('update.txt', 'r+') as file:
    text=file.read()
    print('\nString:', text)
    print('\nPosition In File Now:', file.tell())
    position=file.seek(33)
    print('Position In File Now:', file.tell())
    file.write('All Lands')
    file.seek(59)
    file.write('the tombstone of Karl Marx')
    file.seek(0)
    text=file.read()
    print('\nString:', text)
'''
#114 Консервация данных
'''
import pickle, os
if not os.path.isfile('pickle.dat'):
    data=[0,1]
    data[0]=input('Enter Topic: ')
    data[1]=input('Enter Series: ')
    file=open('pickle.dat', 'wb')
    pickle.dump(data, file)
    file.close()
else:
    file=open('pickle.dat', 'rb')
    data=pickle.load(file)
    file.close()
    print('Welcom Back To:'+data[0]+','+data[1])
'''
