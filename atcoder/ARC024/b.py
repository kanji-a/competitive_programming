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
    color = [I() for _ in range(N)]

    g = [[k, len(list(g))] for k, g in itertools.groupby(color)]
    # print(g)

    ans = 0
    # 全部同色の場合、収束しない
    if len(g) == 1:
        ans = -1
    else:
        # 同色列が両端にまたがっていた場合先端に寄せる
        if g[0][0] == g[-1][0]:
            g[0][1] += g[-1][1]
            g.pop()
        # print(g)
        # 同色列の両端以外の色が変わっていく
        ans = max([(n + 1) // 2 for _, n in g])

    print(ans)

if __name__ == '__main__':
    resolve()
