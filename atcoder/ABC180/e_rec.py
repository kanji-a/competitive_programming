import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9+7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N = I()
    XYZ = [LI() for _ in range(N)]

    def cost(a, b, c, p, q, r):
        return abs(p - a) + abs(q - b) + max(0, r - c)

    con = [[cost(i[0], i[1], i[2], j[0], j[1], j[2]) for j in XYZ] for i in XYZ]
    # dp[s][v]: 0スタートで集合sの頂点を通って最後にvを通る場合の最小コスト
    dp = [[INF] * N for i in range(2 ** N)]
    dp[0][0] = 0

    def rec(s, v):
        if dp[s][v] == INF and s & 1:
            for i in range(N):
                if s >> i & 1:
                    t = s ^ 1 << i
                    dp[s][v] = min(rec(t, i) + con[i][v], dp[s][v])
        return dp[s][v]

    rec(2 ** N - 1, 0)
    # print(dp)

    ans = dp[-1][0]
    print(ans)

if __name__ == '__main__':
    resolve()
