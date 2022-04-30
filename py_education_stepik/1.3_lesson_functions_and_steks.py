'''
def closest_mod_5(x):
    if x%5==0:
        return x
    else:
        for i in range(4):
            x+=1
            if x%5==0:
                return x
y=closest_mod_5(12)
print(y)
'''
from functools import lru_cache


@lru_cache
def c(n,k):
    if k==0: return 1
    if k>n: return 0
    return c(n-1, k)+c(n-1, k-1)

n,k =map(int, input().split())
print(c(n,k))