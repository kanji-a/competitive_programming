import bisect, collections, copy, heapq, itertools, math, string, sys
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
    N, M = LI()
    if M == 0:
        print(1)
    else:
        A = LI_()
        A.sort()

        d = [A[i+1] - A[i] - 1 for i in range(M - 1) if A[i+1] - A[i] - 1 != 0]
        if A[0] != 0:
            d.append(A[0])
        if N - 1 - A[-1] != 0:
            d.append(N - 1 - A[-1])
        if d:
            k = min(d)
            ans = sum([(i - 1) // k + 1 for i in d])
            print(ans)
        else:
            print(0)

if __name__ == '__main__':
    resolve()
