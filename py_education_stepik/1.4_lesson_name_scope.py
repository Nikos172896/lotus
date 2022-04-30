space={'global': {'parent':None, 'vars': []}}

def get(nmsp, var):
    if nmsp in space:
        if var in space[nmsp]['vars']:
            return nmsp
        else:
            return get(space[nmsp]['parent'], var)
    else:
        if var in space['global']['vars']:
            return 'global'
        else:
            return None

def add(nmsp, var):
    if nmsp in space:
        space[nmsp]['vars'].append(var)

def create(nmsp, parent):
    space[nmsp]={'parent': parent, 'vars': []}

while True:
    n=int(input())
    if n<100 and n>1:
        break
while n!=0:
    cmd, nmsp, var=input().split()
    if cmd=='create':
        create(nmsp, var)
    #    print(space)
    if cmd=='add':
        add(nmsp, var)
    #    print(space)
    if cmd=='get':
        ops=get(nmsp, var)
        print(ops)
    n-=1