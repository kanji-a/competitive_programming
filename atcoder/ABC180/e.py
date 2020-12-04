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

    for s in range(2 ** N - 1):
        for i in range(N):
            for j in range(N):
                # sが空集合の場合、追加する頂点は0から向かうことになる
                # 空集合でなければ、sに含まれる頂点から伸ばす
                if (s == 0 or s >> i & 1) and not s >> j & 1:
                    t = s | 1 << j
                    dp[t][j] = min(dp[s][i] + con[i][j], dp[t][j])
    # print(dp)

    ans = dp[-1][0]
    print(ans)

if __name__ == '__main__':
    resolve()
