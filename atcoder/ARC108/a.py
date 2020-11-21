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
    S, P = LI()

    ans = 'No'
    for i in range(int(P ** 0.5) + 1):
        if i * (S - i) == P:
            ans = 'Yes'

    print(ans)

if __name__ == '__main__':
    resolve()
