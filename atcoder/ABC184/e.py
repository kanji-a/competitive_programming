import bisect, collections, copy, heapq, itertools, math, string, sys
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
    H, W = LI()
    a = [SS() for _ in range(H)]
    d = ((1, 0), (0, 1), (-1, 0), (0, -1))

    teleporter = [[] for _ in range(26)]
    S = []
    G = []
    ans = [[-1] * W for _ in range(H)]
    for i, j in itertools.product(range(H), range(W)):
        if a[i][j] == 'S':
            S = (i, j)
            ans[i][j] = 0
        elif a[i][j] == 'G':
            G = (i, j)
        elif a[i][j] in string.ascii_lowercase:
            idx = ord(a[i][j]) - ord('a')
            teleporter[idx].append((i, j))
    # print(teleporter)

    que = collections.deque()
    que.append(S)
    while que:
        cy, cx = que.popleft()
        if (cy, cx) == G:
            break
        for dy, dx in d:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < H and 0 <= nx < W and a[ny][nx] != '#' and ans[ny][nx] == -1:
                ans[ny][nx] = ans[cy][cx] + 1
                que.append((ny, nx))
        if a[cy][cx] in string.ascii_lowercase:
            idx = ord(a[cy][cx]) - ord('a')
            for ny, nx in teleporter[idx]:
                if ans[ny][nx] == -1:
                    ans[ny][nx] = ans[cy][cx] + 1
                    que.append((ny, nx))
            # 一番近いテレポーター以外を踏むのは無意味なので、一度使ったテレポーターを消去
            teleporter[idx] = []
    # for i in ans:
    #     print(i)

    print(ans[G[0]][G[1]])

if __name__ == '__main__':
    resolve()
