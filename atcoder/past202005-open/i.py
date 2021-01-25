import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
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
    Q = I()
    
    # 行と列の順番を保存
    row = list(range(N))
    col = list(range(N))
    # 転置は真理値で保存
    t = False

    for _ in range(Q):
        Query = LI()
        if Query[0] == 3:
            t = ~t
            continue
        A, B = Query[1:]
        A -= 1
        B -= 1
        if Query[0] == 1 and not t or Query[0] == 2 and t:
            row[A], row[B] = row[B], row[A]
        elif Query[0] == 1 and t or Query[0] == 2 and not t:
            col[A], col[B] = col[B], col[A]
        else:
            if t:
                print(N * row[B] + col[A])
            else:
                print(N * row[A] + col[B])

if __name__ == '__main__':
    resolve()
