'''
class MoneyBox:
    def __init__(self, max):
        self.box=0
        self.capacity=max
    def can_add(self, v):
        if self.box+v<=self.capacity:
            return True
        else: return False
    def add(self, v):
        self.box+=v
        return self.capacity-self.box
x=MoneyBox(12)
print(x.can_add(5))
print(x.add(5))
'''
class Buffer:
    def __init__(self):
        self.mass=[]
    def add(self, *a):
        for i in a:
            if len(self.mass)<5:
                self.mass.append(i)
            if len(self.mass)==5:
                print(sum(self.mass))
                self.mass=[]
    def get_current_part(self):
        #print(self.mass)
        return self.mass

buf=Buffer()
buf.add(1,2,3)
buf.get_current_part()
buf.add(4, 5, 6)
buf.get_current_part()
buf.add(7,8,9,10)
buf.get_current_part()
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
buf.get_current_part()