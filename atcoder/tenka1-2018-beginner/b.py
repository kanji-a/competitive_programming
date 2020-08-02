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
    A, B, K = LI()

    for i in range(K):
        if i % 2 == 0:
            if A % 2 == 1:
                A -= 1
            A //= 2
            B += A
        else:
            if B % 2 == 1:
                B -= 1
            B //= 2
            A += B

    print(A, B)

if __name__ == '__main__':
    resolve()
