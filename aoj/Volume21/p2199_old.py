import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    while True:
        N, M = map(int, input().split())
        C = [int(input()) for _ in range(M)]
        x = [int(input()) for _ in range(N)]
        if N==M==0:
            break
        else:
            dp = [[[float('inf'), 0] for _ in range(M)] for _ in range(N+1)]
            dp[0] = [[0, 128] for _ in range(M)]
            for i in range(N):
                for j in range(M):
                    prev = dp[i][j]
                    for k in range(M):
                        next = max(min(prev[1]+C[k], 255), 0)
                        total = prev[0]+(next-x[i])**2
                        if total < dp[i+1][k][0]:
                            dp[i+1][k][0] = total
                            dp[i+1][k][1] = next

            print(min([i[0] for i in dp[-1]]))

if __name__ == '__main__':
    resolve()