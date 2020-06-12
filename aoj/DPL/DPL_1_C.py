import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N, W = map(int, input().split())
    vw = [list(map(int, input().split())) for _ in range(N)]

    # 重さiの場合の最大価値
    dp = [0]*(W+1)

    for i in range(1, W+1):
        for j in range(N):
            v_j = vw[j][0]
            w_j = vw[j][1]
            if i-w_j>=0:
                dp[i] = max(dp[i-w_j]+v_j, dp[i])

    print(dp[W])

if __name__ == '__main__':
    resolve()
