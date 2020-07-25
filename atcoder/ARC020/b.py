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
    n, c = LI()
    a = [I() - 1 for _ in range(n)]

    ans = INF
    for i in range(10):
        for j in range(10):
            if i != j:
                tmp = 0
                for k in range(n):
                    if k % 2 == 0 and a[k] != i or k % 2 == 1 and a[k] != j:
                        tmp += c
                ans = min(tmp, ans)

    print(ans)

if __name__ == '__main__':
    resolve()
