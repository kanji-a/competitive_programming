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
    abcde = [LI() for _ in range(N)]

    s = [900 * (a + b + c + d) + 110 * e for a, b, c, d, e in abcde]

    print(max(s) / 900)

if __name__ == '__main__':
    resolve()
