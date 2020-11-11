import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9+7
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

    k = 2
    num = 0
    for i in range(2, max(A) + 1):
        cnt = len([j for j in A if j % i == 0])
        if cnt > num:
            num = cnt
            k = i

    print(k)

if __name__ == '__main__':
    resolve()
