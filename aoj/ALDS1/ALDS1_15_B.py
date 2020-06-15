import sys, collections
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N, W = LI()
    vw = [LI() for _ in range(N)]

    vw.sort(key=lambda x: x[0]/x[1], reverse=True)
    ans = 0
    i = 0
    while i < N and W - vw[i][1] > 0:
        ans += vw[i][0]
        W -= vw[i][1]
        i += 1

    if i < N:
        ans += vw[i][0] * W / vw[i][1]

    print(ans)

if __name__ == '__main__':
    resolve()
