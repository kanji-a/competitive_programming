import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10 ** 9 + 7
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

    print(sum(A) % MOD)
    # Aの登場回数の偶奇?
    for i in range(N - 1):
        for j in range(i + 1, N):
            print(A[i], A[j], A[i] ^ A[j])

if __name__ == '__main__':
    resolve()
