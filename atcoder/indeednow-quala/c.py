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
    N = I()
    s = [I() for _ in range(N)]
    Q = I()
    s.sort(reverse=True)
    for _ in range(Q):
        k = I()
        if k >= N or s[k] == 0:
            print(0)
        else:
            print(s[k] + 1)

if __name__ == '__main__':
    resolve()
