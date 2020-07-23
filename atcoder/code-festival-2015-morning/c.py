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
    N, K, M, R = LI()
    S = [I() for _ in range(N - 1)]

    S.sort(reverse=True)
    score_final = K * R - sum(S[:K-1])

    if K * R <= sum(S[:K]):
        print(0)
    elif score_final > M:
        print(-1)
    else:
        print(score_final)

if __name__ == '__main__':
    resolve()
