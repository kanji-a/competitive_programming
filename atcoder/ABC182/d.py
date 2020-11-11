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
    N = I()
    A = LI()

    # 累積和の累積和に、その次に動く範囲での累積和のMAXを足したもののMAX
    ans = 0
    A_acm = list(itertools.accumulate(A, initial=0))
    A_acm_max = [0] * (N + 2)
    for i in range(N + 1):
        A_acm_max[i+1] = max(A_acm[i], A_acm_max[i])
    A_acm_acm = list(itertools.accumulate(A_acm, initial=0))
    # print(A_acm)
    # print(A_acm_max)
    # print(A_acm_acm)
    for i in range(N + 1):
        ans = max(A_acm_acm[i] + A_acm_max[i+1], ans)
    print(ans)

if __name__ == '__main__':
    resolve()
