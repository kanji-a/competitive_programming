import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    abc = [list(map(int, input().split())) for _ in range(N)]

    # dp[i]: i日目にa,b,cを選んだ場合のまでの最大幸福度
    dp = [[0, 0, 0] for _ in range(N)]
    dp[0] = [abc[0][0], abc[0][1], abc[0][2]]

    for i in range(1, N):
        prev = dp[i-1]
        preva = prev[0]
        prevb = prev[1]
        prevc = prev[2]
        abci = abc[i]
        a = abci[0]
        b = abci[1]
        c = abci[2]
        dp[i] = [max(prevb+a, prevc+a), max(prevc+b, preva+b), max(preva+c, prevb+c)]

    print(max(dp[N-1]))

if __name__ == '__main__':
    resolve()
