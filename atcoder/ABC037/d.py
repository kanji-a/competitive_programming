import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
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
    H, W = LI()
    a = [LI() for _ in range(H)]

    d = ((0, 1), (1, 0), (0, -1), (-1, 0))
    dp = [[0] * W for _ in range(H)]

    def rec(cy, cx):
        if dp[cy][cx] == 0:
            tmp = 1
            for dy, dx in d:
                ny = cy + dy
                nx = cx + dx
                if 0 <= ny < H and 0 <= nx < W and a[ny][nx] > a[cy][cx]:
                    tmp += rec(ny, nx)
                    tmp %= MOD
            dp[cy][cx] = tmp
        return dp[cy][cx]

    for i, j in itertools.product(range(H), range(W)):
        rec(i, j)
    # for i in dp:
    #     print(i)

    ans = 0
    for i, j in itertools.product(range(H), range(W)):
        ans += dp[i][j]
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    resolve()
