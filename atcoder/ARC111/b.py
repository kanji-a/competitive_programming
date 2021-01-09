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
    max_ab = 0
    for _ in range(N):
        a, b = LI_()
        max_ab = max(a, b, max_ab)
        G[a].append(b)
        G[b].append(a)
    # print(G)

    # 連結成分分解
    visited = {k: -1 for k in G.keys()}
    def dfs(c, num):
        visited[c] = num
        for n in G[c]:
            if visited[n] >= 0:
                continue
            dfs(n, num)
    num = 0
    G_keys = G.keys()
    for i in G_keys:
        if visited[i] >= 0:
            continue
        dfs(i, num) 
        num += 1
    # print(visited)

    # 連結成分ごとに木か判定
    ve = [[0, 0] for _ in range(num)]
    for i in G_keys:
        # 頂点カウント
        ve[visited[i]][0] += 1
        # 辺カウント(二重)
        ve[visited[i]][1] += len(G[i])
    for i in ve:
        i[1] //= 2
    # for i in ve:
    #     print(i)

    ans = 0
    for v, e in ve:
        # 木でなければ、全ての色を出す割当が存在する
        if v - 1 == e:
            ans += v - 1
        # 木ならば、全ての色から1つを除いて出す割当が存在する
        else:
            ans += v
    print(ans)

if __name__ == '__main__':
    resolve()
