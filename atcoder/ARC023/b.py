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
    R, C, D = LI()
    A = [LI() for _ in range(R)]

    ans = 0
    for i, j in itertools.product(range(R), range(C)):
        if i + j <= D and (i + j) % 2 == D % 2:
            ans = max(A[i][j], ans)    

    print(ans)

if __name__ == '__main__':
    resolve()
