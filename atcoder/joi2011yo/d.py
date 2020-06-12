import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    dp = [[0]*21 for _ in range(N)]
    dp[1][A[0]] = 1
    for i in range(1, N):
        for j in range(21):
            if 0<=j+A[i-1]<=20:
                dp[i][j+A[i-1]] += dp[i-1][j]
            if 0<=j-A[i-1]<=20:
                dp[i][j-A[i-1]] += dp[i-1][j]

    print(dp[N-1][A[-1]])

if __name__ == '__main__':
    resolve()
