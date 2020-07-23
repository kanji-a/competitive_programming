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
    x1, y1, r = LI()
    x2, y2, x3, y3 = LI()

    if x2 <= x1 - r and x1 + r <= x3 and y2 <= y1 - r and y1 + r <= y3:
        print('NO')
    else:
        print('YES')

    if (x2 - x1) ** 2 + (y2 - y1) ** 2 <= r ** 2 and (x3 - x1) ** 2 + (y2 - y1) ** 2 <= r ** 2 and (x2 - x1) ** 2 + (y3 - y1) ** 2 <= r ** 2 and (x3 - x1) ** 2 + (y3 - y1) ** 2 <= r ** 2:
        print('NO')
    else:
        print('YES')

if __name__ == '__main__':
    resolve()
