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
    W = [SS() for _ in range(N)]

    ans = 'Yes'
    for i in range(N - 1):
        if W[i][-1] != W[i+1][0]:
            ans = 'No'
            break

    if len(set(W)) < len(W):
        ans = 'No'

    print(ans)

if __name__ == '__main__':
    resolve()
