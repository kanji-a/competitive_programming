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
    N, M, X = LI()
    C = [0]*N
    A = [[0]*M for _ in range(N)]
    for i in range(N):
        ca = LI()
        C[i] = ca[0]
        A[i] = ca[1:]

    cost_min = INF
    for i in range(2**N):
        cost = 0
        rikaido = [0]*M
        for j in range(N):
            if i>>j&1:
                cost += C[j]
                rikaido = [k+m for k, m in zip(rikaido, A[j])]
        if [j>=X for j in rikaido].count(True)==M:
            cost_min = min(cost, cost_min)

    if cost_min>=INF:
        print(-1)
    else:
        print(cost_min)

if __name__ == '__main__':
    resolve()
