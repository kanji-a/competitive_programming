import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    dp = [[0]*N for _ in range(N)]
    for l in range(N):
        dp[l][(l+1)%N] = A[l]
    for l in range(N):
        dp[l][(l+2)%N] = max(A[l], A[(l+1)%N])

    for i in range(3, N+1):
        for l in range(N):
            r = (l+i)%N
            lp1 = (l+1)%N
            lp2 = (l+2)%N
            rm1 = (r-1)%N
            rm2 = (r-2)%N
            dp_lp1_rm1 = dp[lp1][rm1]
            # 自分がA[l]を取る場合 [l+1, r)
            tmp_l = 0
            # 相手がA[l+1]を取る場合
            if A[lp1] > A[rm1]:
                tmp_l = dp[lp2][r]
            # 相手がA[r-1]を取る場合
            else:
                tmp_l = dp_lp1_rm1
            # 自分がA[r-1]を取る場合 [l, r-1)
            tmp_r = 0
            # 相手がA[l]を取る場合
            if A[l] > A[rm2]:
                tmp_r = dp_lp1_rm1
            # 相手がA[r-2]を取る場合
            else:
                tmp_r = dp[l][rm2]

            dp[l][r] = max(A[l]+tmp_l, A[rm1]+tmp_r)

    # for i in dp:
    #     print(i)
    ans = 0
    for i in range(N):
        ans = max(dp[i][i], ans)

if __name__ == '__main__':
    resolve()
