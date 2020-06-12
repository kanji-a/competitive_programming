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
    A, B, H, M = LI()

    rad_M = 2*math.pi * M / 60
    rad_H = 2*math.pi * (60*H+M) / 720

    ans = (A**2+B**2-2*A*B*math.cos(rad_H-rad_M))**0.5

    print(ans)

if __name__ == '__main__':
    resolve()
