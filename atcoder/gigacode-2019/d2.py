import sys, itertools
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
    H, W, K, V = LI()
    A = [LI() for _ in range(H)]

    acc = [[0]*(W+1) for _ in range(H+1)]
    for i in range(H):
        for j in range(W):
            acc[i+1][j+1] = acc[i+1][j] + A[i][j] + K
    for i in range(H):
        for j in range(W):
            acc[i+1][j+1] += acc[i][j+1]

    # for i in acc:
    #     print(i)

    ans = 0
    for i in itertools.combinations(range(H+1), 2):
        for j in itertools.combinations(range(W+1), 2):
            cost = acc[i[1]][j[1]] - acc[i[1]][j[0]] - acc[i[0]][j[1]] + acc[i[0]][j[0]]
            if cost<=V:
                ans = max((i[1]-i[0])*(j[1]-j[0]), ans)

    print(ans)

if __name__ == '__main__':
    resolve()