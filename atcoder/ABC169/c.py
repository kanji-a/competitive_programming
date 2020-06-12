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
    A, B = LS()

    A = int(A)
    B0 = int(B[0])
    B1 = int(B[2])
    B2 = int(B[3])
    ans = (A*B0*100 + A*B1*10 + A*B2) // 100
    print(ans)

if __name__ == '__main__':
    resolve()

