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
    N, K = LI()
    A = LI()

    sum_A = sum(A)

    l = [i / (K * (i - 1) / (sum_A - N) + 1) for i in A]
    print(l)
    ans = math.ceil(max(l))
    print(ans)

if __name__ == '__main__':
    resolve()
