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
    N, T = LI()
    ct = [LI() for _ in range(N)]

    l = [i[0] for i in ct if i[1] <= T]

    if l:
        print(min(l))
    else:
        print('TLE')

if __name__ == '__main__':
    resolve()
