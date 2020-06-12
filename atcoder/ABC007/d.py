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

    def forbidden_num(N):
        # dp[i][j][k] i:[0, i)桁目まで見た j:未満フラグ k:4または9含むフラグ
        dp = [[[0]*2 for _ in range(2)] for _ in range(len(N)+1)]
        dp[0][0][0] = 1

        for i in range(len(N)):
            D = int(N[i])
            for j in range(2):
                for k in range(2):
                    # jが1のとき0~9、jが0のとき、0~D-1まで1、Dだけ0
                    # kが1のとき1、kが0のときdが49なら1、それ以外なら0
                    for d in range(10 if j else D+1):
                        dp[i+1][j or d<D][k or d==4 or d==9] += dp[i][j][k]
            
        # print(N)
        # for i in dp:
        #     print(i)
        return dp[-1][1][1]

    ans = forbidden_num(str(B+1)) - forbidden_num(str(A))
    print(ans)

if __name__ == '__main__':
    resolve()