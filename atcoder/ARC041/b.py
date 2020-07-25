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
    N, M = LI()
    b = [[int(i) for i in SS()] for _ in range(N)]

    ans = [[0] * M for _ in range(N)]
    # 上から見ていって、アメーバを見つけたらそれらは1個下のマスから分裂したものである
    for i in range(N - 1):
        if b[i].count(0) < M:
            for j in range(M):
                c = b[i][j]
                if c > 0:
                    ans[i+1][j] = c
                    b[i][j] = 0
                    b[i+1][j-1] -= c
                    b[i+1][j+1] -= c
                    b[i+2][j] -= c

    for i in ans:
        print(''.join([str(j) for j in i]))

if __name__ == '__main__':
    resolve()
