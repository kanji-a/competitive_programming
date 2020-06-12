import sys, math
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
    a, b, x = LI()

    if 2*x<(a**2)*b:
        ans = 90 - math.degrees(math.atan(2*x / (a*(b**2))))
    elif (a**2)*b == x:
        ans = 0
    else:
        ans = 90 - math.degrees(math.atan(a**3 / (2*((a**2)*b-x))))
    print(ans)

if __name__ == '__main__':
    resolve()