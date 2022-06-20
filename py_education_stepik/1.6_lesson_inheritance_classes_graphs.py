#рекурсия, считывание инпут из файла, словарь, наследование классов

import sys
sys.stdin=open('input_for_lesson_6.txt', 'r')
graph={}
def find_graph(graph, start, end):
    if end not in graph or start not in graph:
        return 'No'
    if start == end:
        return 'Yes'
    for b, j in enumerate(graph[end]):
        if start in graph[end]:
            return 'Yes'
        else:
            if find_graph(graph,start,j)=='Yes':
                return 'Yes'
            else:
                if b==len(graph[end]): return 'No'
    return 'No'



def write_graph(first, second):
    pass

n=int(input())
for i in range(n):
    str_k=input().replace(':',' ').split()
    graph[str_k[0]]=str_k[1:]
    print(str_k)
'''
n=int(input())
for i in range(n):
    str_l,*str_k=input().split(':')
    str_k=''.join(str_k)
    str_k=str_k.split()
    str_k=list(str_k)
    str_l=str_l.strip()
    graph[str_l]=str_k
'''
n=int(input())
for i in range(n):
    start,end=input().split()
    print(find_graph(graph,start,end))
print(graph)

#класс управления элементами стека, наследование от списка
'''
class ExtendedStack(list):
    def sum(self):
        self.append(self.pop()+self.pop())
    def sub(self):
        self.append(self.pop()-self.pop())
    def mul(self):
        self.append(self.pop()*self.pop())
    def div(self):
        self.append(self.pop()//self.pop())
'''
#наследование и изменени функции классов родителей
'''
import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
class LoggableList(Loggable, list):
    def append(self, elem):
        super().append(elem)
        return self.log(elem)

a = LoggableList()
a.append('msg 1')
a.append('msg 2')
print(a)
'''