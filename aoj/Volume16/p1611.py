import sys
input = lambda: sys.stdin.readline().rstrip() 

def I(): return int(input())
def MI(): return list(map(int, input().split()))

def resolve():
    while True:
        n = I()
        w = MI()
        # n = int(input())
        # w = list(map(int, input().split()))
        if n==0:
            break
        else:
            dp = [[0]*(n+1) for _ in range(n+2)]
            # 幅
            for i in range(2, n+1):
                for l in range(n-i+1):
                    r = l+i
                    if dp[l+1][r-1] == i-2:
                        if abs(w[l]-w[r-1])<=1:
                            dp[l][r] = i
                        else:
                            dp[l][r] = i-2
                    for j in range(l, r):
                        if dp[l][j] + dp[j][r] > dp[l][r]:
                            dp[l][r] = dp[l][j] + dp[j][r]

            print(dp[0][-1])        

if __name__ == '__main__':
    resolve()