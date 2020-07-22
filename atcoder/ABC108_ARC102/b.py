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
    x1, y1, x2, y2 = LI()

    p2p3_x = y1 - y2
    p2p3_y = x2 - x1
    x3 = x2 + p2p3_x
    y3 = y2 + p2p3_y
    p3p4_x = x1 - x2
    p3p4_y = y1 - y2
    x4 = x3 + p3p4_x
    y4 = y3 + p3p4_y

    print(x3, y3, x4, y4)

if __name__ == '__main__':
    resolve()
