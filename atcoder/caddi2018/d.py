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
    a = [I() for _ in range(N)]

    # 1種類で奇数個なら自分の勝ち
    # 奇数個のりんごを1個食べて偶数個にする
    if len([i for i in a if i % 2 == 1]) == 0:
        print('second')
    else:
        print('first')

if __name__ == '__main__':
    resolve()
