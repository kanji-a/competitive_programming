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
    A = LI()

    m = 1000
    up = []
    for i in range(N - 1):
        if A[i] < A[i+1]:
            up.append((A[i], A[i+1]))

    for i in range(len(up)):
        l, h = up[i]
        m = m // l * h + m % l

    print(m)

if __name__ == '__main__':
    resolve()
