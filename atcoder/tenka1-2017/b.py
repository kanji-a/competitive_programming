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
    BA = []
    for _ in range(N):
        A, B = LI()
        BA.append((B, A))

    BA.sort()
    ans = BA[0][0] + BA[0][1]
    print(ans)

if __name__ == '__main__':
    resolve()
