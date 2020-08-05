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
    A = LI_()
    B = LI()
    C = LI()

    ans = 0
    for i in range(N - 1):
        a0, a1 = A[i], A[i+1]
        ans += B[a0]
        if a1 - a0 == 1:
            ans += C[a0]
    ans += B[A[N-1]]

    print(ans)

if __name__ == '__main__':
    resolve()
