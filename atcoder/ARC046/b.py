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
    A, B = LI()

    if A == B:
        # 相手にA+1個を押し付ければ勝ち
        if N % (A + 1) == 0:
            print('Aoki')
        else:
            print('Takahashi')
    elif A > B or A >= N:
        print('Takahashi')
    else:
        print('Aoki')

if __name__ == '__main__':
    resolve()
