import sys, itertools, bisect
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
    n = I()
    xy = [tuple(LI()) for _ in range(n)]
    xy = set(xy)

    ans = 0
    for i, j in itertools.combinations(xy, 2):
        dx = j[0]-i[0]
        dy = j[1]-i[1]
        x0 = i[0]-dy
        y0 = i[1]+dx
        x1 = j[0]-dy
        y1 = j[1]+dx
        if (x0, y0) in xy and (x1, y1) in xy:
            ans = max(dx**2+dy**2, ans)

    print(ans)

if __name__ == '__main__':
    resolve()