import csv
import time
import re
import collections
import json
import networkx as nx
import matplotlib.pyplot as plt


'''
#поиск типа преступлений встречающихся чаще всего в 2015 году
kol_vo = []
with open('Crimes.csv') as f:
    file = csv.reader(f)
    for i in file:
        if re.match(r'\d\d/\d\d/2015', i['Date']):
            kol_vo.append(i['Primary Type'])
    print(collections.Counter(kol_vo))

#ответы к тестам следующего задания    
A : 10
B : 5
C : 5
D : 4
E : 1
F : 2
G : 1
V : 2
W : 1
X : 5
Y : 3
Z : 3
'''
#подсчет количества предков классов из формата json
inp_json = [  # тестовый граф наследования в виде json-объекта
    {'name': 'G', 'parents': ['F']},  # сначала отнаследуем от F, потом его объявим: корректный алгоритм все равно правильно обойдёт граф, независимо что было раньше: наследование или объявление
    {'name': 'A', 'parents': []},
    {'name': 'B', 'parents': ['A']},
    {'name': 'C', 'parents': ['A']},
    {'name': 'D', 'parents': ['B', 'C']},
    {'name': 'E', 'parents': ['D']},
    {'name': 'F', 'parents': ['D']},
    # а теперь другая ветка наследования
    {'name': 'X', 'parents': []},
    {'name': 'Y', 'parents': ['X', 'A']},  # свяжем две ветки наследования для проверки, обошла ли рекурсия предков Z и предков Y в поисках A
    {'name': 'Z', 'parents': ['X']},
    {'name': 'V', 'parents': ['Z', 'Y']},
    {'name': 'W', 'parents': ['V']},
]
#js = json.loads(inp_json)
#inp_json = json.loads(input())
graph = {}
end_cort = {}
#преобразуем json данные в обычный словарь формата "Наследник" : "Предки"
#и сразу создаем финальный словарь в который будем выводить количество путей
for i in inp_json:
    graph[i['name']]=i['parents']
    end_cort[i['name']] = 0

#используем библиотеку networkx для создания графа из наших данных
graph_2 = nx.DiGraph()
for i in graph:
    graph_2.add_node(i)
    for j in graph.get(i):
        graph_2.add_edge(i, ''.join(j))

#проходим по "финальному" словарю и используя функцию поиска кратчайших путей в графе
#получаем набор проходов каждой вершины к остальным
#подсчитываем количество встречающихся по пути вершин и вносим в финальный словарь
for i in end_cort.keys():
    p=0
    for j in nx.all_pairs_dijkstra_path_length(graph_2):
        for k in j:
            if i in k:
                p += 1
    end_cort[i] = p-1

#сортируем и выводим
end_cort = dict(sorted(end_cort.items(), key=lambda x: x[0]))
for i in end_cort:
    print(i, ':', end_cort.get(i))

#для визуализации графа можно использовать:
#ns.draw_networkx(graph_2, node_color='red', node_size=1000, with_labels=True)
#plt.show()