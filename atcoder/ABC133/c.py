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
    L, R = LI()

    ans = 2018    
    for i, j in itertools.combinations(range(L, min(L + 2018, R) + 1), 2):
        ans = min(i * j % 2019, ans)

    print(ans)

if __name__ == '__main__':
    resolve()
