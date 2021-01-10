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
    N = I()
    A = LI()
    A_org = copy.deepcopy(A)

    for i in range(N - 1):
        tmp = []
        for j in range(2 ** (N - 1 - i)):
            tmp.append(max(A[2*j], A[2*j+1]))
        A = tmp

    ans = A_org.index(min(A)) + 1
    print(ans)

if __name__ == '__main__':
    resolve()
