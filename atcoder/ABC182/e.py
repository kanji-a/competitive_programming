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
    H, W, N, M = LI()
    S = [['.'] * W for _ in range(H)]
    for _ in range(N):
        A, B = LI_()
        S[A][B] = '*'
    for _ in range(M):
        C, D = LI_()
        S[C][D] = '#'

    # for i in S:
    #     print(i)

    # 横方向の光
    light_h = copy.deepcopy(S)
    for i in range(H):
        for j in range(W):
            # 電球を見つけたら左右に光を伸ばしていく
            if S[i][j] == '*':
                # 左方向
                k = j - 1
                while k >= 0 and light_h[i][k] == '.':
                    light_h[i][k] = '*'
                    k -= 1 
                # 右方向
                k = j + 1
                while k < W and light_h[i][k] == '.':
                    light_h[i][k] = '*'
                    k += 1 
    # for i in light_h:
    #     print(i)

    # 縦方向の光
    light_v = copy.deepcopy(S)
    for i in range(W):
        for j in range(H):
            # 電球を見つけたら左右に光を伸ばしていく
            if S[j][i] == '*':
                # 上方向
                k = j - 1
                while k >= 0 and light_v[k][i] == '.':
                    light_v[k][i] = '*'
                    k -= 1 
                # 下方向
                k = j + 1
                while k < H and light_v[k][i] == '.':
                    light_v[k][i] = '*'
                    k += 1 
    # for i in light_v:
    #     print(i)

    ans = 0
    for i, j in itertools.product(range(H), range(W)):
        if light_h[i][j] == '*' or light_v[i][j] == '*':
            ans += 1
    print(ans)

if __name__ == '__main__':
    resolve()
