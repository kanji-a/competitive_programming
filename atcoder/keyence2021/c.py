import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 998244353
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    H, W, K = LI()
    hwc = {}
    for _ in range(K):
        h, w, c = LSS()
        hwc[(int(h) - 1, int(w) - 1)] = c

    # 空白マスのパターンごとだと間に合わないので切り口を変える
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = pow(3, H * W - K, MOD)

    inv = pow(3, MOD - 2, MOD)
    hwc_keys = set(hwc.keys())
    for i in range(H):
        for j in range(W):
            if (i, j) not in hwc_keys:
                tmp = dp[i][j] * 2
                tmp *= inv
                if j + 1 < W:
                    dp[i][j+1] += tmp
                    dp[i][j+1] %= MOD
                if i + 1 < H:
                    dp[i+1][j] += tmp
                    dp[i+1][j] %= MOD
                continue
            if hwc[(i, j)] in ('R', 'X') and j + 1 < W:
                dp[i][j+1] += dp[i][j]
                dp[i][j+1] %= MOD
            if hwc[(i, j)] in ('D', 'X') and i + 1 < H:
                dp[i+1][j] += dp[i][j]
                dp[i+1][j] %= MOD

    # for i in dp:
    #     print(i)

    print(dp[-1][-1])

if __name__ == '__main__':
    resolve()

