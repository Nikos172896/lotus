objects =[18, 2, 18, 2, 3, [1,2,3], True, 'True', True, [1,2,3]]

objects2=[]
ant=0
for i in range(len(objects)):
    ant=0
    for j in range(i+1, len(objects)):
        if objects[i] is objects[j]: ant+=1
        if ant<1 and j==len(objects)-1: objects2.append(objects[i])
    if i==len(objects)-1: objects2.append(objects[i])
ans=len(objects2)
print(ans)
print(objects2)
'''
object2=[]
object2.append(object[0])
for obj in object:
    if obj not in object2:
        object2.append(obj)
ans=len(object2)
print(ans)
print(object2)
'''
print(len(set(map(lambda x: id(x), objects))))
print(len({id(x) for x in objects}))