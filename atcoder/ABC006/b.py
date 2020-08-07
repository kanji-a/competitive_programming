import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10007
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    n = I()

    a = [0] * max(n, 3)
    a[2] = 1

    for i in range(3, n):
        a[i] = (a[i-1] + a[i-2] + a[i-3]) % MOD

    print(a[n-1])

if __name__ == '__main__':
    resolve()
