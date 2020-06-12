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
    P = LI_()
    ABC = [LI() for _ in range(N-1)]

    cnt = [0]*N
    for i in range(M-1):
        p_larger = max(P[i], P[i+1])
        p_smaller = min(P[i], P[i+1])
        cnt[p_smaller] += 1
        cnt[p_larger] -= 1
    for i in range(N-1):
        cnt[i+1] += cnt[i]

    print(sum([min(ABC[i][0]*e, ABC[i][2]+ABC[i][1]*e) for i, e in enumerate(cnt[:-1])]))

if __name__ == '__main__':
    resolve()