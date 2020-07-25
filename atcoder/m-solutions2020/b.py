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
    A, B, C = LI()
    K = I()

    while A >= B:
        B *= 2
        K -= 1
    while B >= C:
        C *= 2
        K -= 1

    if K >= 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    resolve()
