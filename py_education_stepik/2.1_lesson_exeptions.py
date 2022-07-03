'''
try:
    foo()
except ArithmeticError:
    print('ArithmeticError')
except AssertionError:
    print('AsserionError')
except ZeroDivisionError:
    print('ZeroDivisionError')
'''

'''
import sys
sys.stdin=open('input_for lesson_2.1.txt', 'r')

graph={}
def find_graph(graph, start, end):#функция поиска вхождения предка в родителя
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


opls=[]
for _ in range(int(input())):
    str_k=input().replace(':', ' ').split()
    if len(str_k)==1:
        if str_k[0] not in graph.keys():
            graph[str_k[0]]=[]
    else:
        for i in range(1, len(str_k)):
            if str_k[0] not in graph.keys():
                graph[str_k[0]]=[]
            if str_k[i] not in graph:
                graph[str_k[i]]=[]
                graph[str_k[i]].append(str_k[0])
            else:
                graph[str_k[i]].append(str_k[0])
#print(graph)
str_l=[]
str_d=set()
[str_l.append(input()) for _ in range(int(input()))]
xindex=0
for i, main in enumerate(str_l):
    for j in range(i+1, len(str_l)):
        if find_graph(graph, str_l[j], main)=='Yes':
            #print(str_l[j])
            str_d.add(str_l[j])

#print(str_l)
plot={}
for m in str_d:
    plot[m]=str_l.index(m)
#print(plot)
sorted_plot={}
sorted_plot_key=sorted(plot, key=plot.get)
for p in sorted_plot_key:
    sorted_plot[p]=plot[p]
#print(sorted_plot)
str_d=sorted_plot.keys()
for m in str_d:
    print(m)
'''
#Наследование классов
class PositiveList(list):
    def append(self, x):
        if x>0:
            super().append(x)
        else:
            raise NonPositiveError
class NonPositiveError(Exception):
    pass
x=PositiveList()
x.append(4)
print(x)