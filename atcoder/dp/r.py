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

def matMulMod(A, B, s):
    C = [[0] * s for _ in range(s)]
    for i in range(s):
        for j in range(s):
            for k in range(s):
                C[i][j] += A[i][k] * B[k][j]
                C[i][j] %= MOD
    return C

def matPowMod(A, n):
    s = len(A)
    B = [[int(i == j) for j in range(s)] for i in range(s)]
    while n > 0:
        if n & 1:
            B = matMulMod(B, A, s)
        A = matMulMod(A, A, s)
        n >>= 1
    return B

def resolve():
    N, K = LI()
    a = [LI() for _ in range(N)]

    # dp[i][j][k]: 長さiのjからkのパス
    # 以下のような更新式なので行列のn乗 dp[i]は単位行列
    # dp[i][j][k] = dp[i-1][j][l] * a[l][k]
    B = matPowMod(a, K)
    # print(B)
    
    ans = sum([sum(i) % MOD for i in B]) % MOD
    print(ans)

if __name__ == '__main__':
    resolve()
