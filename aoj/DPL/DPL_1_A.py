import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    n, m = map(int, input().split())
    c = list(map(int, input().split()))

    # dp[i]: i円を払う最小枚数
    dp = [float('inf')]*(n+1)
    dp[0] = 0

    for i in range(1, n+1):
        for j in range(m):
            if i>=c[j]:
                dp[i] = min(dp[i-c[j]]+1, dp[i])

    print(dp[n])

if __name__ == '__main__':
    resolve()
