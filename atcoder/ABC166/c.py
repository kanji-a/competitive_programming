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
    H = LI()
    AB = [LI_() for _ in range(M)]
    good = [True]*N
    for i in AB:
        if H[i[0]]>=H[i[1]]:
            good[i[1]] = False
        if H[i[0]]<=H[i[1]]:
            good[i[0]] = False

    print(len([i for i in good if i]))

if __name__ == '__main__':
    resolve()
