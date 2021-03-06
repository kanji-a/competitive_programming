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
    N, L = LI()

    ans = (2 * L + N - 1) * N // 2
    if 0 <= L:
        ans -= L
    elif L + N <= 0:
        ans -= L + N - 1

    print(ans)

if __name__ == '__main__':
    resolve()
