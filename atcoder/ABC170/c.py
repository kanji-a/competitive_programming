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
    X, N = LI()
    if N == 0:
        print(X)
        return

    p = LI()

    p_max = max(p)
    p_min = min(p)

    if X < p_min or p_max < X:
        print(X)
        return
    else:
        d = [abs(i-X) for i in range(0, 102) if i not in p]
        d_min = min(d)
        for i in range(0, 102):
            if i not in p:
                if abs(i-X)==d_min:
                    print(i)
                    return

if __name__ == '__main__':
    resolve()
