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
    S = I()

    # (0, 0), (10**9, 1), (x, y) とおくと
    # S = 10**9 * y - x
    y = (S - 1) // 10 ** 9 + 1
    x = 10 ** 9 * y - S

    print(0, 0, 10 ** 9, 1, x, y)

if __name__ == '__main__':
    resolve()
