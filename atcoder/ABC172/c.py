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
    N, M, K = LI()
    A = LI()
    B = LI()

    A_acc = [0] * (N + 1)
    for i in range(N):
        A_acc[i+1] = A_acc[i] + A[i]
    B_acc = [0] * (M + 1)
    for i in range(M):
        B_acc[i+1] = B_acc[i] + B[i]

    ans = 0
    for i in range(N + 1):
        if A_acc[i] > K:
            break
        j = bisect.bisect_right(B_acc, K - A_acc[i]) - 1
        ans = max(i + j, ans)

    print(ans)

if __name__ == '__main__':
    resolve()
