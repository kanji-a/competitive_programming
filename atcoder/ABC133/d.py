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
    A = LI()

    ans = [0] * N

    for i in range(N):
        ans[0] += (-1) ** i * A[i]

    for i in range(N - 1):
        ans[i+1] = 2 * A[i] - ans[i]

    print(*ans)

if __name__ == '__main__':
    resolve()
