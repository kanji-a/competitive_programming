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
    sx, sy, tx, ty = LI()

    dx = tx - sx
    dy = ty - sy
    ans_f0 = 'U' * dy + 'R' * dx
    ans_b0 = 'D' * dy + 'L' * dx
    ans_f1 = 'L' + 'U' * (dy + 1) + 'R' * (dx + 1) + 'D'
    ans_b1 = 'R' + 'D' * (dy + 1) + 'L' * (dx + 1) + 'U'

    print(ans_f0 + ans_b0 + ans_f1 + ans_b1)

if __name__ == '__main__':
    resolve()
