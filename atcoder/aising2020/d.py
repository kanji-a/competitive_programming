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
    X = SS()

    # 一回の操作でnはN以下になる
    # 2回目以降の操作はメモ化再帰
    # 初回popcountは2種類しかない Xのpopcountから足し引きすればよい

    pc_X = X.count('1')

    if pc_X == 0:
        for i in range(N):
            print(1)
    elif pc_X == 1:
        for i in range(N):
            if i == X.index('1'):
                print(0)
            else:
                # 1が2つある場合、最後の位が1の場合、奇数
                if i == N - 1 or X.index('1') == N - 1:
                    print(2)
                else:
                    print(1)
    else:
        next_X_m1 = 0
        next_X_p1 = 0
        pc_m1 = pc_X - 1
        pc_p1 = pc_X + 1
        for i in range(N):
            if X[i] == '1':
                next_X_m1 += pow(2, N - 1 - i, pc_m1)
                next_X_p1 += pow(2, N - 1 - i, pc_p1)

        dp = [-1] * N
        dp[0] = 0

        def dfs(n):
            if dp[n] == -1:
                dp[n] = 1 + dfs(n % bin(n).count('1'))
            return dp[n]

        for i in range(N):
            next = 0
            if X[i] == '0':
                next = (next_X_p1 + pow(2, N - 1 - i, pc_p1)) % pc_p1
            else:
                next = (next_X_m1 - pow(2, N - 1 - i, pc_m1)) % pc_m1
            ans = dfs(next) + 1
            print(ans)
    # print(dp)

if __name__ == '__main__':
    resolve()
