import sys, math, itertools
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
MOD = 998244353
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    N, M, K = LI()

    ans = 0
    # K組より多いものを考える K組同じ色にしてそれ以外は任意
    for i in itertools.combinations(range(N-1), K):
        



if __name__ == '__main__':
    resolve()
