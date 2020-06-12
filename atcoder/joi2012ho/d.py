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
    N, M = LI()
    ABX = [LI() for _ in range(M)]

    cnt = [[0]*(i+2) for i in range(N+2)]
    for i in ABX:
        A = i[0]-1
        B = i[1]-1
        X = i[2]
        cnt[A][B] += 1
        cnt[A][B+1] -= 1
        cnt[A+X+1][B] -= 1
        cnt[A+X+2][B+1] += 1
        cnt[A+X+1][B+X+2] += 1
        cnt[A+X+2][B+X+2] -= 1

    for i in range(N):
        for j in range(i+1):
            cnt[i][j+1] += cnt[i][j]
    for i in range(N):
        for j in range(i, N):
            cnt[j+1][i] += cnt[j][i]
    for i in range(N):
        for j in range(N-i):
            # print(i+j, j)
            cnt[i+j+1][j+1] += cnt[i+j][j]

    # for i in cnt:
    #     print(i)

    print(sum([(i+1)-e[:-1].count(0) for i, e in enumerate(cnt[:N])]))

if __name__ == '__main__':
    resolve()