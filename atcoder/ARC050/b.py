import sys
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
    R, B = LI()
    x, y = LI()

    def isOK(m):
        return m<=(R-m)//(x-1)+(B-m)//(y-1)

    def binsearch_left():
        ng = max(R, B)
        ok = 0
        while abs(ok-ng)>1:
            m = (ng+ok)//2
            if isOK(m):
                ok = m
            else:
                ng = m
        return ok

    ans = binsearch_left()
    print(ans)

if __name__ == '__main__':
    resolve()