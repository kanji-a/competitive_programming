import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N, M = map(int, input().split())
    D = [int(input()) for _ in range(N)]
    C = [int(input()) for _ in range(M)]

    dp = [[float('inf')]*(N+1) for _ in range(M+1)]
    for i in dp:
        i[0] = 0
    for i in range(1, M+1):
        for j in range(1, N+1):
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]+D[j-1]*C[i-1])

    print(dp[-1][-1])

if __name__ == '__main__':
    resolve()
