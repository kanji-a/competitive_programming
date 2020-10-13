import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    A, B = LI()

    # x以下の禁止された数の個数
    def f(x):
        len_x = len(x)
        # dp[i][j]: [0, i)の禁止された数の個数、j: 未満フラグ、k: 禁止された数であるフラグ 
        dp = [[[0] * 2 for _ in range(2)] for _ in range(len_x + 1)]
        dp[0][0][0] = 1
        for i in range(len_x):
            x_i = int(x[i])
            for j in range(x_i):
                if j == 4 or j == 9:
                    dp[i+1][1][1] += dp[i][0][0] + dp[i][0][1]
                else:
                    dp[i+1][1][0] += dp[i][0][0]
                    dp[i+1][1][1] += dp[i][0][1]
            if x_i == 4 or x_i == 9:
                dp[i+1][0][1] += dp[i][0][0] + dp[i][0][1]
            else:
                dp[i+1][0][0] += dp[i][0][0]
                dp[i+1][0][1] += dp[i][0][1]
            dp[i+1][1][0] += 8 * dp[i][1][0]
            dp[i+1][1][1] += 2 * dp[i][1][0] + 10 * dp[i][1][1]
        return dp[-1][0][1] + dp[-1][1][1]

    ans = f(str(B)) - f(str(A - 1))
    print(ans)

if __name__ == '__main__':
    resolve()