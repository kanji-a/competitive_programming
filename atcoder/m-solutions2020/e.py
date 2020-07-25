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
    XYP = [LI() for _ in range(N)]

    # 縦と横でそれぞれ考えて
    # 1次元だったらどう? 最小はどっかの街に重なるような
    # DPっぽい
    # なるべく合計人口が多くなるような街を通るような道を通す

    x_sum = {}
    y_sum = {}
    for i, x, y, p in enumerate(XYP):
        if x in x_sum.keys():
            x_sum[x] += p
        else:
            x_sum[x] = p
        if y in y_sum.keys():
            y_sum[y] += p
        else:
            y_sum[y] = p
    print(x_sum, y_sum)

    path = []

    for i in range(N  + 1):
        ans = 0
        for j in XYP:
            x, y, p = j
            ans += min(abs(x), abs(y)) * p
        print(ans)

if __name__ == '__main__':
    resolve()
