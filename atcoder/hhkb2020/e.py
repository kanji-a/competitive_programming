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
    S = [SS() for _ in range(H)]

    # 2**(H*W) * そのマスを照らす照明をおける数
    # 各マスについて、そのマスを照らす照明をおけるマスを数える
    cnt = [[0] * W for _ in range(H)]
    for i in range(H):
        l = -1
        r = -1
        for j in range(W):
            if S[i][j] == '.':
                l = j
            else:
                r = j

if __name__ == '__main__':
    resolve()
