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
    N, M, C = LI()
    B = LI()
    A = [LI() for _ in range(N)]

    ans = len([i for i in A if sum([i[j] * B[j] for j in range(M)]) + C > 0])
    print(ans)

if __name__ == '__main__':
    resolve()
