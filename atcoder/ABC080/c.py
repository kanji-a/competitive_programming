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
    F = [LI() for _ in range(N)]
    P = [LI() for _ in range(N)]

    ans = -INF
    for i in range(1, 2 ** 10):
        tmp = 0
        for j in range(N):
            cnt = 0
            for k in range(10):
                if i >> k & 1:
                    cnt += F[j][k]
            tmp += P[j][cnt]
        ans = max(tmp, ans)

    print(ans)

if __name__ == '__main__':
    resolve()
