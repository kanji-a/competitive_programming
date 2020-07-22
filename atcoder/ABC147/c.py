import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N = I()
    A = []
    xy = []
    for _ in range(N):
        A.append(I())
        xy.append([LI() for _ in range(A[-1])])

    ans = 0
    for i in range(2 ** N):
        # まず正直者を仮定し、正直者の証言に矛盾がないか判定
        is_ok = True
        num = 0
        for j in range(N):
            if i >> j & 1:
                num += 1
                for k in xy[j]:
                    x, y = k
                    x -= 1
                    if i >> x & 1 != y:
                        is_ok = False
        if is_ok:
            ans = max(num, ans)

    print(ans)

if __name__ == '__main__':
    resolve()
