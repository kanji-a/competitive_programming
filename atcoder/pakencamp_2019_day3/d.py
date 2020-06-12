import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    S = [input() for _ in range(5)]

    # dp[i][j]: i-1列を色jで塗るときの合計最小塗替え数
    dp = [[0]*3 for _ in range(N+1)]
    for i in range(1, N+1):
        cnt = [0, 0, 0]
        for j in range(5):
            if S[j][i-1]=='R':
                cnt[0]+=1
            if S[j][i-1]=='B':
                cnt[1]+=1
            if S[j][i-1]=='W':
                cnt[2]+=1
        for j in range(3):
            tmp = []
            for k in range(3):
                if j!=k:
                    tmp.append(dp[i-1][k] + (5 - cnt[k]))
            dp[i][j] += min(tmp)

    print(min(dp[-1]))

if __name__ == '__main__':
    resolve()
