'''
with open('txt_try.txt', 'r') as tx, open('txt_try2.txt', 'w') as td:
    op=tx.read().splitlines()
    print(op)
    op.reverse()
    td.write('\n'.join(op))
'''
import os
import os.path
import glob
with open('txt_try.txt', 'w') as f, open('txt_try2.txt', 'w') as f2:
    print(os.listdir('main'))
    end=set()
    end_2=[]
    for current_dir, dirs, files in os.walk("main"):
        #print(files)
        for i in files:
            if i[-3:]=='.py':
                end.add(current_dir)
                end_2.append(current_dir)
    end=sorted(end)
    end_2=sorted(end_2)
    print(end)
    print(end_2)
    f.write('\n'.join(end))
    for j in end_2:
        f2.writelines('\n'.join(j))