import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
import atcoder.twosat as twosat
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9+7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N, D = LI()
    XY = [LI() for _ in range(N)]

    ts = twosat.TwoSAT(4 * N)
    for xy0, xy1 in itertools.combinations(XY, 2):
        for x, y in itertools.product(xy0, xy1):
            if abs(x - y) >= D:
                ts.add_clause(x, True, y, True)

    if ts.satisfiable():
        print('Yes')
        for i in ts.answer():
            print(i)
    else:
        print('No')

if __name__ == '__main__':
    resolve()
