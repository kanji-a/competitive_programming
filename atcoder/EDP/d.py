import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N, W = map(int, input().split())
    wv = [list(map(int, input().split())) for _ in range(N)]

    # dp[i][j]: 0〜(i-1)まで使ったときの重さjのときの価値の最大値
    dp = [[0]*(W+1) for i in range(N+1)]

    for i in range(1, N+1):
        for w in range(0, W+1):
            # i番目を入れられる場合
            if w - wv[i-1][0] >= 0:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-wv[i-1][0]] + wv[i-1][1])
            else:
                dp[i][w] = dp[i-1][w]

    print(max(dp[N]))

if __name__ == '__main__':
    resolve()
