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
    n, m, d = LI()

    # どの組も同じなので1組だけに着目
    if d == 0:
        ans = n * (m - 1) / n ** 2
    else:
        ans = 2 * (n - d) * (m - 1) / n ** 2

    print(ans)

if __name__ == '__main__':
    resolve()
