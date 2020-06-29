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
    N, M, X, Y = LI()
    x = LI()
    y = LI()

    x.sort()
    y.sort()

    has_war = True
    for Z in range(X, Y+1):
        if X < Z <= Y and x[-1] < Z <= y[0]:
            has_war = False

    if has_war:
        print('War')
    else:
        print('No War')

if __name__ == '__main__':
    resolve()
