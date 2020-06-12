import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N, W = map(int, input().split())
    w = [0] * N
    v = [0] * N
    for i in range(N):
        w[i], v[i] = map(int, input().split()) 

    sum_v = sum(v)

    # dp[i][j]: 0〜(i-1)まで使ったときの価値jのときの重みの総和の最小値
    dp = [[sum(w)]*(sum_v+1) for i in range(N+1)]
    dp[0][0] = 0

    for i in range(1, N+1):
        for j in range(sum_v+1):
            if j-v[i-1] >= 0:
                dp[i][j] = min(dp[i-1][j-v[i-1]] + w[i-1], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    print(max([i for i, w in enumerate(dp[N]) if w<=W]))

if __name__ == '__main__':
    resolve()
