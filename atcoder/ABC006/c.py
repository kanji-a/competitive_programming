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

    ans = (-1, -1, -1)
    for i in range(N + 1):
        # 残りを老人と赤ちゃんで鶴亀算
        j = 4 * (N - i) - (M - 2 * i)
        k = (M - 2 * i) - 3 * (N - i)
        if j >= 0 and k >= 0:
            ans = (i, j, k)
            break

    print(*ans)

if __name__ == '__main__':
    resolve()
