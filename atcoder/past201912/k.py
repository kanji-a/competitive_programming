import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9+7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N = I()
    G = collections.defaultdict(list)
    s = -1
    for i in range(N):
        p = I() - 1
        if p == -2:
            s = i
            continue
        G[p].append(i)

    # 木をDFSで走査して頂点を通る順番を比較して判定する
    o = [[-1, -1] for _ in range(N)]
    num = [0]

    def dfs(c, p):
        o[c][0] = num[0]
        num[0] += 1
        for n in G[c]:
            if n != p:
                dfs(n, c)
        o[c][1] = num[0]
        num[0] += 1

    dfs(s, -1)
    # print(o)

    M = I()
    for _ in range(M):
        a, b = LI_()
        if o[b][0] < o[a][0] and o[a][1] < o[b][1]:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    resolve()
