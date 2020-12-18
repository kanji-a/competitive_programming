import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9+7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    H, W = LI()
    S = [SS() for _ in range(H)]
    d = ((1, 0), (0, 1), (1, 1))

    # dp[i][j]: (i, j)からスタートして先手勝つなら1、負けるなら2、置けなければ0
    dp = [[0] * W for _ in range(H)]

    def rec(cy, cx):
        if dp[cy][cx] == 0:
            tmp = []
            for dy, dx in d:
                ny = cy + dy
                nx = cx + dx
                if 0 <= ny < H and 0 <= nx < W and S[ny][nx] == '.':
                    tmp.append(rec(ny, nx))
            if not tmp:
                # 袋小路とか右下
                dp[cy][cx] = 2
            else:
                if 2 in tmp:
                    # 移動先候補に1つでも後手有利な場所があれば、先手はそこへ駒を移動する
                    dp[cy][cx] = 1
                else:
                    dp[cy][cx] = 2

        return dp[cy][cx]
    
    rec(0, 0)
    # for i in dp:
    #     print(i)

    if dp[0][0] == 1:
        print('First')
    else:
        print('Second')

if __name__ == '__main__':
    resolve()
