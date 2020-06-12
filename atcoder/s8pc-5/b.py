import sys, itertools
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    N, M = LI()
    xyr = [LI() for _ in range(N)]
    xy = [LI() for _ in range(M)]

    # 対固定半径円
    min_r_c = INF
    for i in xy:
        vx = i[0]
        vy = i[1]
        min_r_c_tmp = INF
        for j in xyr:
            cx = j[0]
            cy = j[1]
            cr = j[2]
            d = ((cx-vx)**2 + (cy-vy)**2)**0.5 - cr
            min_r_c_tmp = min(d, min_r_c_tmp)
        min_r_c = min(min_r_c_tmp, min_r_c)

    # 対可変半径円
    min_r_v = INF
    for i in itertools.combinations(range(M), 2):
        x0 = xy[i[0]][0]
        y0 = xy[i[0]][1]
        x1 = xy[i[1]][0]
        y1 = xy[i[1]][1]
        d = (((x1-x0)**2 + (y1-y0)**2)**0.5)/2
        min_r_v = min(d, min_r_v)

    if M==0:
        print(min([i[2] for i in xyr]))
    else:
        print(min(min_r_c, min_r_v))

if __name__ == '__main__':
    resolve()