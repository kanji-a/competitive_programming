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
    A = LI()

    ans = 1
    if 0 in A:
        ans = 0
    else:
        for i in A:
            ans *= i
            if ans>10**18:
                ans = -1
                break

    print(ans)

if __name__ == '__main__':
    resolve()