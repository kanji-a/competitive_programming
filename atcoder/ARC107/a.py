import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 998244353
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    A, B, C = LI()

    ans = 1
    ans *= (1 + A) * A // 2 % MOD
    ans *= (1 + B) * B // 2 % MOD
    ans *= (1 + C) * C // 2 % MOD
    print(ans % MOD)

if __name__ == '__main__':
    resolve()
