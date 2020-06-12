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

def warshall_floyd(d):
    V = len(d)
    for i in range(V):
        d[i][i] = 0
    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

def resolve():
    N, M = LI()
    cost = [[INF]*N for _ in range(N)]
    for _ in range(M):
        a, b, t = LI()
        cost[a-1][b-1] = t
        cost[b-1][a-1] = t
        
    min_cost = warshall_floyd(cost)
    # for i in min_cost:
    #     print(i)
    print(min([max(i) for i in min_cost]))

if __name__ == '__main__':
    resolve()