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
    N, M = LI()
    H = LI()
    W = LI()
    H.sort()
    H_d = [H[i+1] - H[i] for i in range(N - 1)]
    H_d_acm_e = [0]
    for i in range(0, N - 1, 2):
        H_d_acm_e.append(H_d_acm_e[-1] + H_d[i])
    H_d_acm_o = [0]
    for i in range(1, N - 1, 2):
        H_d_acm_o.append(H_d_acm_o[-1] + H_d[i])
    # print(H)
    # print(H_d)
    # print(H_d_acm_e)
    # print(H_d_acm_o)

    ans = INF
    for i in W:
        tmp = 0
        idx = bisect.bisect_left(H, i)
        # print(idx)
        # Hに割って入ったところ
        if idx % 2 == 0:
            tmp += H[idx] - i
        else:
            tmp += i - H[idx-1]
        # H前半
        tmp += H_d_acm_e[idx//2]
        # H後半
        tmp += H_d_acm_o[-1] - H_d_acm_o[idx//2]
        # print(tmp)
        ans = min(tmp, ans)

    print(ans)

if __name__ == '__main__':
    resolve()
