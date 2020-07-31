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
    y = I()
    m = I()
    d = I()

    def f(y, m, d):
        if m in (1, 2):
            m += 12
            y -= 1
        return 365 * y + y // 4 - y // 100 + y // 400 + 306 * (m + 1) // 10 + d - 429

    ans = f(2014, 5, 17) - f(y, m, d)
    print(ans)

if __name__ == '__main__':
    resolve()
