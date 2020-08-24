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
    A, B, C, K = LI()

    ans = (-1) ** (K % 2) * (A - B)
    if abs(ans) > 10 ** 18:
        print('Unfair')
    else:
        print(ans)

if __name__ == '__main__':
    resolve()
