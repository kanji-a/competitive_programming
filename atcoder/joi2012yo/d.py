import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N, K = map(int, input().split())
    P = [-1]*N
    for _ in range(K):
        A, B = list(map(int, input().split()))
        P[A-1] = B-1

    # dp[i][j][k]: i日目がjでi-1日目がkの場合の数
    dp = [[[0]*3 for _ in range(3)] for _ in range(N)]
    if P[0]==-1:
        if P[1]==-1:
            for i in range(3):
                for j in range(3):
                    dp[1][i][j] = 1
        else:
            for i in range(3):
                dp[1][P[1]][i] = 1
    else:
        if P[1]==-1:
            for i in range(3):
                dp[1][i][P[0]] = 1
        else:
            dp[1][P[1]][P[0]] = 1

    for i in range(2, N):
        if P[i]==-1:
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        if not j==k==l:
                            dp[i][j][k] += dp[i-1][k][l]
        else:
            for j in range(3):
                for k in range(3):
                    if not j==k==P[i]:
                        dp[i][P[i]][j] += dp[i-1][j][k]

    ans = 0
    for i in dp[-1]:
        for j in i:
            ans += j
            ans %= 10000
    print(ans)

if __name__ == '__main__':
    resolve()
