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
    N, K = LI()
    d = []
    A = []
    for i in range(K):
        d.append(I())
        A.append(LI_())

    snuke = [False]*N
    ans = 0
    for i in A:
        for j in i:
            snuke[j] = True

    print(len([i for i in snuke if not i]))
        
if __name__ == '__main__':
    resolve()