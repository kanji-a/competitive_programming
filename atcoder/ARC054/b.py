import sys
input = lambda: sys.stdin.readline().rstrip() 
import math

def resolve():
    P = float(input())

    def df(x):
        return 1+P*(-math.log(2)/1.5)*2**(-x/1.5)

    def f(x):
        return x+P*2**(-x/1.5)

    def binsearch_left():
        l = 0
        r = P
        while r-l>10**(-10):
            m = (l+r)/2
            if 0<=df(m):
                r = m
            else:
                l = m
        return r

    x = binsearch_left()
    print(f(x))

if __name__ == '__main__':
    resolve()
