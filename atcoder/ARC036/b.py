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
    h = [I() for _ in range(N)]

    L = [0] * N
    for i in range(N - 1):
        if h[i] < h[i+1]:
            L[i+1] = L[i] + 1
    # print(L)

    R = [0] * N
    for i in range(N - 1):
        if h[N-1-i] < h[N-2-i]:
            R[N-2-i] = R[N-1-i] + 1
    # print(R)

    ans = max([i + j + 1 for i, j in zip(L, R)])
    print(ans)

if __name__ == '__main__':
    resolve()
