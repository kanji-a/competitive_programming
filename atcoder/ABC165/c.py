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
    N, M, Q = LI()
    abcd = [LI() for _ in range(Q)]

    ans = 0
    for i in itertools.combinations_with_replacement(range(1, M+1), N):
        # print(i)
        score = 0
        for j in abcd:
            a = j[0]-1
            b = j[1]-1
            c = j[2]
            d = j[3]
            if i[b]-i[a]==c:
                score += d
        ans = max(score, ans)

    print(ans)


if __name__ == '__main__':
    resolve()
