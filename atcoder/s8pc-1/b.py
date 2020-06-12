import sys, fractions
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
    H, W, N = LI()
    XY = [LI() for _ in range(N)]

    ans = []
    for i in range(1, W+1):
        is_deleted =  False
        upper = []
        for j in XY:
            if H*j[0]==i*j[1]:
                is_deleted = True
            if i*j[1] > H*j[0]:
                upper.append(j)
        if len(upper)*2==N and not is_deleted:
            ans.append([i, H])
    for i in range(1, H):
        is_deleted = False
        upper = []
        for j in XY:
            if i*j[0]==W*j[1]:
                is_deleted = True
            if W*j[1] > i*j[0]:
                upper.append(j)
        if len(upper)*2==N and not is_deleted:
            ans.append([W, i])
    ans.sort()

    if len(ans)>0:
        for i in ans:
            print('('+str(i[0])+','+str(i[1])+')')
    else:
        print(-1)

if __name__ == '__main__':
    resolve()