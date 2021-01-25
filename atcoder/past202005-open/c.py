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
    A, R, N = LI()

    if R == 1:
        print(A)
        return 
    ans = A
    for _ in range(N - 1):
        ans *= R
        if ans > 10 ** 9:
            print('large')
            return
    print(ans)

if __name__ == '__main__':
    resolve()
