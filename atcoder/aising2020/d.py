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
    # 操作後に同じ値になることもあるので覚えておく
    # popcountはそのビット見ればすぐわかる
    # 初回popcountは2種類しかない

    # x = X
    # N = 5
    # X = '10101'
    pc_X = X.count('1')

    next_X_p1 = 0
    next_X_m1 = 0
    pc_p1 = pc_X + 1
    pc_m1 = pc_X - 1
    for i in range(N):
        if X[i] == '1':
            next_X_p1 += pow(2, N - 1 - i, pc_p1)
            next_X_m1 += pow(2, N - 1 - i, pc_m1)

    dp = [-1] * N
    dp[0] = 0
    def dfs(n):
        if dp[n] == -1:
            dp[n] = 1 + dfs(n % bin(n).count('1'))
        return dp[n]
    # print(pc_X, pc_m1, pc_p1, next_X_m1, next_X_p1)
    for i in range(N):
        next = 0
        if X[i] == '1':
            next = next_X_m1 - pow(2, N - 1 - i, pc_m1)
            next %= pc_m1
        else:
            next = next_X_p1 - pow(2, N - 1 - i, pc_p1)
            next %= pc_p1
        # for j in range(N):
        #     if X[j] == '1' and j != i or X[j] == '0' and j == i:
        #         next += pow(2, N - 1 - j, pc)
        if int(X) == 1 and i == N - 1:
            ans = 0
        else:
            ans = dfs(next) + 1
        print(ans)
    print(dp)



    # def f(n):
    #     cnt = 0
    #     while '1' in n:
    #         pc = n.count('1')
    #         n = int(n, 2)
    #         n %= pc
    #         n = bin(n)[2:]
    #         cnt += 1
    #     print(cnt)

    # print(f(x))

if __name__ == '__main__':
    resolve()
