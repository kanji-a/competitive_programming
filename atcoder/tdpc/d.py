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
    N, D = LI()

    ans = collections.Counter()
    temp = D
    for i in (2, 3, 5):
        while temp % i == 0:
            ans[i] += 1
            temp //= i
    if temp > 1:
        print(0)
    else:
        D_pf = ans
        # dp[i][j][k][l]: i回振ったときの2^j*3^k*5^lになる確率
        # ただし、Dに含まれるnの個数がD_pf[n]以上の場合はD_pf[n]にまとめる。
        # そうすると答えを出すときに楽。そのため、配るDPで計算する。
        dp = [[[[0] * (D_pf[5] + 1) for _ in range(D_pf[3] + 1)] for _ in range(D_pf[2] * N + 1)] for _ in range(N + 1)]
        dp[0][0][0][0] = 1
        d = ((0, 1, 0, 2, 0, 1), (0, 0, 1, 0, 0, 1), (0, 0, 0, 0, 1, 0))

        for i in range(N):
            for j, k, l in itertools.product(range(D_pf[2] + 1), range(D_pf[3] + 1), range(D_pf[5] + 1)):
                tmp = dp[i][j][k][l] / 6
                for m in range(6):
                    dp[i+1][min(j+d[0][m], D_pf[2])][min(k+d[1][m], D_pf[3])][min(l+d[2][m], D_pf[5])] += tmp
        # for i in dp:
        #     print(i)

        print(dp[-1][D_pf[2]][D_pf[3]][D_pf[5]])

if __name__ == '__main__':
    resolve()
