import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    D, N = map(int, input().split())
    T = [int(input()) for _ in range(D)]
    ABC = [list(map(int, input().split())) for _ in range(N)]

    dp = [[-1]*N for _ in range(D+1)]
    for i in range(1, D+1):
        for j in range(N):
            A = ABC[j][0]
            B = ABC[j][1]
            C = ABC[j][2]
            if A<=T[i-1]<=B:
                if i==1:
                    dp[i][j] = 0
                else:
                    tmp = []
                    for k in range(N):
                        if dp[i-1][k]>=0:
                            tmp.append(dp[i-1][k]+abs(ABC[k][2]-C))
                    dp[i][j] = max(tmp)

    print(max(dp[-1]))

if __name__ == '__main__':
    resolve()
