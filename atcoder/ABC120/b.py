import math, sys
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
    A, B, K = LI()

    d = math.gcd(A, B)
    ans = 0
    for i in range(d, 0, -1):
        if A % i == B % i == 0:
            K -= 1
        if K == 0:
            ans = i
            break

    print(ans)

if __name__ == '__main__':
    resolve()