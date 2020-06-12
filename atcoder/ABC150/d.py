from functools import reduce
import fractions
import numpy as np

N, M = map(int, input().split())
a = np.array(list(map(int, input().split())))

a = a // 2

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

l = lcm(*a)
exist = not 0 in ((l//a)%2)

if exist:
    print((M // l + 1 ) // 2)
else:
    print(0)