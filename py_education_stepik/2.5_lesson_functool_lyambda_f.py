#lambda
def mod_checker(x, mod=0):
    return lambda y: y % x == mod


mod_1 = mod_checker(4, 0)
print(mod_1(4))
