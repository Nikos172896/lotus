'''
class multifilter:
    def judge_half(pos, neg):
        if pos>=neg:
            return True
    def judge_any(pos, neg):
        if pos>=1:
            return True
    def judge_all(pos, neg):
        if neg==0:
            return True
    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable=iterable
        self.funcs=funcs
        self.judge=judge
    def __iter__(self):
        for i in self.iterable:
            pos, neg=0,0
            for j in self.funcs:
                if j(i)==True:
                    pos+=1
                else:
                    neg+=1
            if self.judge(pos, neg)==True:
                yield i
def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]
'''
def primes():
    a=2
    while True:
        mod_h = 0
        for i in range(1, a):
            if a%i==0:
                mod_h+=1
        if mod_h==1:
            a+=1
            yield a-1
        else:
            a+=1
yo=primes()
for i in range(10):
    print(next(yo))