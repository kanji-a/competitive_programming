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
    C = [LI() for _ in range(H)]

    acm_e = [[0] * (W + 1) for _ in range(H + 1)]
    for i in range(H):
        for j in range(W):
            if (i + j) % 2 == 0:
                acm_e[i+1][j+1] = acm_e[i+1][j] + C[i][j]
            else:
                acm_e[i+1][j+1] += acm_e[i+1][j]
    for i in range(W + 1):
        for j in range(H):
            acm_e[j+1][i] += acm_e[j][i]
    # print(acm_e)

    acm_o = [[0] * (W + 1) for _ in range(H + 1)]
    for i in range(H):
        for j in range(W):
            if (i + j) % 2 == 1:
                acm_o[i+1][j+1] = acm_o[i+1][j] + C[i][j]
            else:
                acm_o[i+1][j+1] += acm_o[i+1][j]
    for i in range(W + 1):
        for j in range(H):
            acm_o[j+1][i] += acm_o[j][i]
    # print(acm_o)

    ans = 0
    for h_s, h_t in itertools.combinations(range(H + 1), 2):
        for w_s, w_t in itertools.combinations(range(W + 1), 2):
            sum_e = acm_e[h_t][w_t] - acm_e[h_s][w_t] - acm_e[h_t][w_s] + acm_e[h_s][w_s]
            sum_o = acm_o[h_t][w_t] - acm_o[h_s][w_t] - acm_o[h_t][w_s] + acm_o[h_s][w_s]
            # print(h_s, h_t, w_s, w_t, sum_e, sum_o)
            if sum_e == sum_o:
                ans = max((h_t - h_s) * (w_t - w_s), ans)
    print(ans)

if __name__ == '__main__':
    resolve()
