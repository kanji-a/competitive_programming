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
    T = I()
    for _ in range(T):
        N, A, B = LI()

        ans = 0
        L = max(A, B)
        S = min(A, B)
        ans += pow(N - L + 1, 2, MOD) * pow(N - S + 1, 2, MOD)
        ans %= MOD
        ans -= pow(N - L + 1, 2, MOD) * pow(L - S + 1, 2, MOD)
        ans %= MOD

        print(ans)

if __name__ == '__main__':
    resolve()
