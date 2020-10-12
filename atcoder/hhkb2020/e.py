import bisect, collections, copy, heapq, itertools, math, string, sys
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
    K = sum([i.count('.') for i in S])

    # 各マスについて、そのマスを照らす照明をおけるマスを数える
    left = [[0] * W for _ in range(H)]
    right = [[0] * W for _ in range(H)]
    for i in range(H):
        cnt_l = 0
        cnt_r = 0
        for j in range(W):
            if S[i][j] == '.':
                cnt_l += 1
                left[i][j] = cnt_l
            else:
                cnt_l = 0
            if S[i][W-j-1] == '.':
                cnt_r += 1
                right[i][W-j-1] = cnt_r
            else:
                cnt_r = 0
    up = [[0] * W for _ in range(H)]
    down = [[0] * W for _ in range(H)]
    for i in range(W):
        cnt_u = 0
        cnt_d = 0
        for j in range(H):
            if S[j][i] == '.':
                cnt_u += 1
                up[j][i] = cnt_u
            else:
                cnt_u = 0
            if S[H-j-1][i] == '.':
                cnt_d += 1
                down[H-j-1][i] = cnt_d
            else:
                cnt_d = 0

    # 各マスが照らされるのは、そのマスを照らせるマスに照明が1つ以上あった場合
    # 余事象を引く形で求める
    ans = pow(2, K, MOD) * K
    ans %= MOD
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                tmp = left[i][j] + right[i][j] + up[i][j] + down[i][j] - 3
                ans -= pow(2, K - tmp, MOD)
                ans %= MOD

    print(ans)

if __name__ == '__main__':
    resolve()
