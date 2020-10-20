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
    a = LI()
    cnt = collections.Counter(a)

    # dp[i][j][k]: 1個の皿がi枚、2個の皿がj枚、3個の皿がk枚のときの期待値
    # 0個の皿の枚数はN-(i+j+k)なので添字に持つ必要なし
    dp = [[[-1] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0

    def f(i, j, k):
        if dp[i][j][k] != -1:
            return dp[i][j][k]
        res = N 
        # 期待値の更新式なので、期待値の計算式と同じように確率*別状態の期待値の和+今回の操作1回
        # 状態(i, j, k)からどの個数の皿から食べたらどの状態になるかを書くだけ
        # 問題文通りに考えると右辺が未来のことなので変な感じがするが、そこに囚われないこと
        # 右の式を変形 dp[i][j][k] = ((N - i - j - k) / N) * dp[i][j][k] + i / N * dp[i-1][j][k] + j / N * dp[i+1][j-1][k] + k / N * dp[i][j+1][k-1] + 1
        # 右辺に+1と-1がいて更新順が複雑なのでメモ化再帰
        if i > 0:
            res += i * f(i - 1, j, k)
        if j > 0:
            res += j * f(i + 1, j - 1, k)
        if k > 0:
            res += k * f(i, j + 1, k - 1)
        res /= i + j + k
        dp[i][j][k] = res
        return dp[i][j][k]

    ans = f(cnt[1], cnt[2], cnt[3])

    # for i in dp:
    #     print(i)

    print(ans)

if __name__ == '__main__':
    resolve()
