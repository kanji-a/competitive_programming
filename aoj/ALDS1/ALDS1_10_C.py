import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    q = int(input())
    for _ in range(q):
        X = input()
        Y = input()

        len_X = len(X)
        len_Y = len(Y)
        dp = [[0]*(len_Y+1) for _ in range(len_X+1)]
        dp[0][0] = 0
        for i in range(1, len_X+1):
            for j in range(1, len_Y+1):
                if X[i-1]==Y[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        print(int(dp[len_X][len_Y]))

if __name__ == '__main__':
    resolve()