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
    t = [I() for _ in range(N)]

    ans = sum(t)
    for i in range(2 ** N):
        s0 = 0
        s1 = 0
        for j in range(N):
            if i >> j & 1:
                s0 += t[j]
            else:
                s1 += t[j]
        ans = min(max(s0, s1), ans)

    print(ans)

if __name__ == '__main__':
    resolve()
