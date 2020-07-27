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
    L, H = LI()
    N = I()
    A = [I() for _ in range(N)]

    for i in A:
        if i > H:
            print(-1)
        else:
            print(max(L - i, 0))

if __name__ == '__main__':
    resolve()
