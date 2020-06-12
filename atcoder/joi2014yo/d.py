import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
MOD = 10007
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    N = I()
    d = {'J':0, 'O':1, 'I':2}
    Admin = [d[i] for i in S()]

    dp = [[0]*(2**3) for _ in range(N+1)]
    for i in range(2**3):
        if i&1 and i>>Admin[0]&1:
            dp[1][i] = 1

    for day in range(1, N):
        for members_n in range(2**3):
            # 責任者
            if members_n>>Admin[day]&1:
                for members_c in range(2**3):
                    # 鍵
                    has_key = False
                    for member in range(3):
                        if members_n>>member&1 and members_c>>member&1:
                            has_key = True
                    if has_key:
                        dp[day+1][members_n] += dp[day][members_c]
                        dp[day+1][members_n] %= MOD
    # for i in dp:
    #     print(i)
    print(sum(dp[-1])%MOD)

if __name__ == '__main__':
    resolve()