import sys
sys.stdin=open('input_for_lesson_6.txt', 'r')
graph={}
def find_graph(graph, start, end, path=[]):
    path=path+[start]
    if start == end:
        return 'Yes'
    if end in graph:
        pass

def write_graph(first, second):
    pass

n=int(input())
for i in range(n):
    str_l,*str_k=input().split(':')
    graph[str_l]=str_k

print(graph)
