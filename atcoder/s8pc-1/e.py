import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
MOD = 1000000007
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    N, Q = LI()
    a = LI()
    c = LI()

    acc = [0]*(N+1)
    for i in range(1, N):
        acc[i+1] = acc[i] + pow(a[i-1], a[i], MOD)
        acc[i+1] %= MOD

    ans = acc[c[0]]
    for i in range(Q-1):
        ans += (acc[max(c[i+1], c[i])] - acc[min(c[i+1], c[i])])%MOD
    ans += acc[c[-1]]
    ans %= MOD
    print(ans)

if __name__ == '__main__':
    resolve()