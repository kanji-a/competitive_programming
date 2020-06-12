import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    N, M = LI()
    C = [I()-1 for _ in range(N)]

    # 累積和
    cnt = [[0]*N for _ in range(M)]
    for i, e in enumerate(C):
        cnt[e][i] = 1
    acc = [[0]*(N+1) for _ in range(M)]
    for i in range(M):
        for j in range(N):
            acc[i][j+1] += acc[i][j] + cnt[i][j]
    # for i in acc:
    #     print(i)

    # 種類ごとの個数
    num_per_type = [sum(i) for i in cnt]

    # dp[s]: sの種類を左から並べた状態にするような最小の取り出し個数
    dp = [INF]*2**M
    dp[0] = 0

    def rec(s):
        if dp[s]<INF:
            return dp[s]
        else:
            # bitをみていく
            tmp = INF
            for i in range(M):
                if s>>i&1:
                    next_s = s&~(1<<i)
                    # 種類iを新たに並べるべきところに違うものがいくつ入っているか
                    # ([sの個数-iの個数, sの個数)の間のiじゃないやつの個数をdp[next_s]に足す
                    arranged_num = sum([num_per_type[j] for j in range(M) if s>>j&1])
                    i_num = acc[i][arranged_num] - acc[i][arranged_num-num_per_type[i]]
                    dp[s] = min(rec(next_s)+num_per_type[i]-i_num, dp[s])
            return dp[s]

    rec(2**M-1)
    # for i in range(2**M):
    #     print(bin(i), dp[i])
    print(dp[-1])


if __name__ == '__main__':
    resolve()