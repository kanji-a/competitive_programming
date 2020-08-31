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

def binsearch_left(a, x):
    ng = -1
    ok = len(a)
    while abs(ok-ng)>1:
        m = (ng+ok)//2
        if x[0] < a[m][0] and x[1] < a[m][1]:
            ok = m
        else:
            ng = m
    return ok

def lis(a):
    dp = [[INF, INF]]*len(a)
    for i in a:
        dp[binsearch_left(dp, i)] = i
    return binsearch_left(dp, [INF, INF])

def resolve():
    N = I()
    hw = [LI() for _ in range(N)]

    # LISでやろうとしたができず
    # 列の中で2つ組の大小関係未定義のペアが存在するから?
    hw.sort()
    print(hw)
    ans = lis(hw)
    print(ans)

if __name__ == '__main__':
    resolve()
