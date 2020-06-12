import sys, bisect
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
    N = I()
    c = [I() for _ in range(N)]

    # L[i]: 長さi+1の増加部分列の最後の最小数字
    L = []
    for i in c:
        idx = bisect.bisect_left(L, i)
        if idx==len(L):
            L.append(i)
        else:
            idx = max(idx, 0)
            L[idx] = i

    print(N-len(L))

if __name__ == '__main__':
    resolve()