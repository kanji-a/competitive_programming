import sys
import numpy as np
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    N, K = LI()
    A = np.array(LI())
    F = np.array(LI())

    A.sort()
    F.sort()
    F = F[::-1]

    # 時間tで感触できるか
    def can_complete(t):
        return np.maximum(0, A-t//F).sum() <= K

    # for j in range(20):
    #     print(can_complete(j))

    ng = -1
    ok = max(A)*max(F)
    while abs(ok-ng)>1:
        m = (ng+ok)//2
        if can_complete(m):
            ok = m
        else:
            ng = m
    print(ok)

if __name__ == '__main__':
    resolve()
