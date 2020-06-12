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
    N = I()
    a = LI()

    r = 1
    ans = 0
    for l in range(N):
        while (r<N and a[r-1]<a[r]) or l==r:
            r += 1
        ans += r-l

    print(ans)

if __name__ == '__main__':
    resolve()