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
    A = [I() for _ in range(N)]
    
    A_first = max(A)
    A_second = 0
    if A.count(A_first) >= 2:
        A_second = A_first
    else:
        for i in A:
            if i != A_first:
                A_second = max(i, A_second)

    for i in A:
        if i == A_first:
            print(A_second)
        else:
            print(A_first)

if __name__ == '__main__':
    resolve()
