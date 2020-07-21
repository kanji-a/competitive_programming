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

    ans = 0
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            ans += i
            if N // i != i:
                ans += N // i

    if ans == 2 * N:
        print('Perfect')
    elif ans < 2 * N:
        print('Deficient')
    else:
        print('Abundant')

if __name__ == '__main__':
    resolve()
