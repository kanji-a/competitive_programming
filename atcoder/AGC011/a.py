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
    N, C, K = LI()
    T = [I() for _ in range(N)]
    T.sort()

    t = T[0]
    cnt = 0
    ans = 0
    for i in T:
        cnt += 1
        if cnt > C or i > t + K:
            ans += 1
            cnt = 1
            t = i
    ans += 1

    print(ans)

if __name__ == '__main__':
    resolve()
