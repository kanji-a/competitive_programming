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

    cnt0 = collections.Counter()
    for x, y in xy:
        cnt0[x+y] += 1
    ans0 = max(cnt0.keys()) - min(cnt0.keys())

    cnt1 = collections.Counter()
    for x, y in xy:
        cnt1[x-y] += 1
    ans1 = max(cnt1.keys()) - min(cnt1.keys())

    print(max(ans0, ans1))

if __name__ == '__main__':
    resolve()
