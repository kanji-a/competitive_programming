import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    A, B, X = LI()

    def f(x):
        return A * x + B * len(str(x))

    ng = 10 ** 9 + 1
    ok = 0
    while abs(ok-ng)>1:
        m = (ng+ok)//2
        if X>=f(m):
            ok = m
        else:
            ng = m

    print(ok) 

if __name__ == '__main__':
    resolve()
