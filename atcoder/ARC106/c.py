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
    N, M = LI()

    # 差をつかせるパターン 高橋君は下の3つ、青木君は上の1つを取る
    # -------
    #  - - -
    # 差がつかないパターン(個数稼ぎに使う)
    # -----
    #  --- 
    #   -  
    # これらを合体させて
    # -----------
    #  ----- - -
    #   --- 
    #    -  

    if N == 1 and M == 0:
        print(1, 2)
    elif 0 <= M <= N - 2:
        # 2段目2個目以降の小さいやつがM個
        # 2段目1個目からの下向きピラミッドはN - 1 - M段
        for i in range(N - M - 1):
            print(2 + i, 1 + (N - 1 - M) * 2 - i)
        for i in range(M):
            tmp = 2 * N - 2 * M
            print(tmp + 2 * i, tmp + 2 * i + 1)
        print(1, 2 * N)
    else:
        print(-1)

if __name__ == '__main__':
    resolve()
