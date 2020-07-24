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
    N, K = LI()

    # K以下、K、K以上
    ans = ((K - 1) * (N - K) * 6 + (K - 1) * 3 + (N - K) * 3 + 1) / (N ** 3)

    print(ans)

if __name__ == '__main__':
    resolve()
