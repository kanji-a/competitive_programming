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

def lis(a):
    dp = [INF]*len(a)
    for i in a:
        dp[bisect.bisect_left(dp, i)] = i
    return bisect.bisect_left(dp, INF)

def resolve():
    N = I()
    hw = [LI() for _ in range(N)]

    # hでソートしてwのLISをとる
    # 同じhのwを複数取らないよう、wを降順ソートしておく
    hw.sort(key=lambda x: x[1], reverse=True)
    hw.sort(key=lambda x: x[0])
    w = [i[1] for i in hw]

    ans = lis(w)
    print(ans)

if __name__ == '__main__':
    resolve()
