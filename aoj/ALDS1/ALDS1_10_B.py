import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    n = int(input())
    M = [list(map(int, input().split())) for _ in range(n)]

    # dp[i][j]: [i, j)の最小乗算数
    dp = [[0]*(n+1) for _ in range(n)]

    # 幅
    for i in range(2, n+1):
        # 開始位置
        for j in range(n-i+1):
            tmp = []
            # 切れ目
            for k in range(j+1, j+i):
                tmp.append(M[j][0]*M[k][0]*M[j+i-1][1]+dp[j][k]+dp[k][j+i])
            dp[j][j+i] = min(tmp)

    print(dp[0][n])

if __name__ == '__main__':
    resolve()
