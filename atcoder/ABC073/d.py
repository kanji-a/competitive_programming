import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9+7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def warshall_floyd(d):
    V = len(d)
    for i in range(V):
        d[i][i] = 0
    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

def resolve():
    N, M, R = LI()
    r = LI_()
    con = [[INF] * N for _ in range(N)]
    for i in range(N):
        con[i][i] = 0
    for _ in range(M):
        A, B, C = LI()
        con[A-1][B-1] = C
        con[B-1][A-1] = C

    warshall_floyd(con)
    # print(con)

    ans = INF
    for i in itertools.permutations(r):
        tmp = 0
        for j in range(R - 1):
            tmp += con[i[j]][i[j+1]]
        ans = min(tmp, ans)

    print(ans)

if __name__ == '__main__':
    resolve()
