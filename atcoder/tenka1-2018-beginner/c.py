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
    A = [I() for _ in range(N)]
    A.sort()

    if N % 2 == 0:
        ans = (2 * sum(A[N//2:]) - A[N//2]) - (2 * sum(A[:N//2]) - A[N//2-1])
        print(ans)
    else:
        ans0 = 2 * sum(A[N//2+1:]) - (2 * sum(A[:N//2+1]) - A[N//2-1] - A[N//2])
        ans1 = (2 * sum(A[N//2:]) - A[N//2] - A[N//2+1]) - 2 * sum(A[:N//2])
        print(max(ans0, ans1))

if __name__ == '__main__':
    resolve()
