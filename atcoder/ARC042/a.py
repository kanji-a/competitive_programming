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
    N, M = LI()
    a = [I() - 1 for _ in range(M)]

    seen = [False] * N

    for i in reversed(a):
        if not seen[i]:
            print(i + 1)
            seen[i] = True

    for i in range(N):
        if not seen[i]:
            print(i + 1)

if __name__ == '__main__':
    resolve()
