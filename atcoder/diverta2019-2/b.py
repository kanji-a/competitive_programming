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
    xy = [LI() for _ in range(N)]

    if N == 1:
        print(1)
    else:
        interval = []
        for i in range(N):
            for j in range(N):
                if i != j:
                    interval.append((xy[i][0] - xy[j][0], xy[i][1] - xy[j][1]))

        cnt = collections.Counter(interval)
        nocost = max(cnt.values())
        ans = N - nocost
        print(ans)

if __name__ == '__main__':
    resolve()
