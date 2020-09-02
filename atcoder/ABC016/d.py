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
    Ax, Ay, Bx, By = LI()
    N = I()
    XY = [LI() for _ in range(N)]
    
    def op(x0, y0, x1, y1):
        return x0 * y1 - x1 * y0

    def intersect(x0, y0, x1, y1, x2, y2, x3, y3):
        op_01_2 = op(x1 - x0, y1 - y0, x2 - x0, y2 - y0)
        op_3_01 = op(x3 - x0, y3 - y0, x1 - x0, y1 - y0)
        op_23_0 = op(x3 - x2, y3 - y2, x0 - x2, y0 - y2)
        op_1_23 = op(x1 - x2, y1 - y2, x3 - x2, y3 - y2)
        return op_01_2 * op_3_01 > 0 and op_23_0 * op_1_23 > 0

    cnt = 0
    for i in range(N):
        Cx, Cy = XY[i]
        Dx, Dy = XY[(i+1)%N]
        if intersect(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy):
            cnt += 1

    print(1 + cnt // 2)

if __name__ == '__main__':
    resolve()
