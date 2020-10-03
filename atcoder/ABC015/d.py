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
    W = I()
    N, K = LI()
    AB = [LI() for _ in range(N)]

    # dp[i][j]: 合計幅i以内の個数jの最大合計重要度
    dp = [[0] * (K + 1) for _ in range(W + 1)]
    for i in range(N):
        A, B = AB[i]
        for j in range(W, 0, -1):
            for k in range(1, K + 1):
                if j - A >= 0:
                    dp[j][k] = max(dp[j][k], dp[j-A][k-1] + B)
    # for i in dp:
    #     print(i)

    ans = max([max(i) for i in dp])
    print(ans)

if __name__ == '__main__':
    resolve()
