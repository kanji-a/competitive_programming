import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N = I()
    W = LI()

    W_cum = [0] * (N + 1)
    for i in range(N):
        W_cum[i+1] = W_cum[i] + W[i]

    sum_W = sum(W)
    ans = INF
    for i in W_cum:
        ans = min(abs(sum_W - 2 * i), ans)

    print(ans)

if __name__ == '__main__':
    resolve()
