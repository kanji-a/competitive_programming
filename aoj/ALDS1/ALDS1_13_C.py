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
    S = []
    for _ in range(4):
        S.append(LI())

    ans = 0
    for i in range(4):
        for j in range(4):
            if S[i][j]!=0:
                r = (S[i][j]-1) // 4
                c = (S[i][j]-1) % 4
                ans += abs(i-r) + abs(j-c)
    print(ans)

if __name__ == '__main__':
    resolve()
