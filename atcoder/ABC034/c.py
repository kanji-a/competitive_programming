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

def combMod(n, r, p):
    numer = 1
    denom = 1
    for i in range(1, r+1):
        numer = numer * (n-r+i) % p
        denom = denom * i % p
    return numer * pow(denom, p-2, p) % p

def resolve():
    W, H = LI()

    print(combMod((W+H-2), min(W-1, H-1), MOD))

if __name__ == '__main__':
    resolve()
