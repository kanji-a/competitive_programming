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
    A = [list(SS()) for _ in range(10)]

    d = ((0, 1), (0, -1), (1, 0), (-1, 0))
    def dfs(cy, cx, m, seen):
        for dy, dx in d:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < 10 and 0 <= nx < 10 and m[ny][nx] == 'o' and not seen[ny][nx]:
                seen[ny][nx] = True
                dfs(ny, nx, m, seen)

    ans = 'NO'
    for i, j in itertools.product(range(10), repeat=2):
        if A[i][j] == 'x':
            # Aをコピー
            tmp = [[] for _ in range(10)]
            for k, l in itertools.product(range(10), repeat=2):
                tmp = copy.deepcopy(A)
            tmp[i][j] = 'o'

            # DFSで連結成分カウント
            cnt = [0]
            seen = [[False] * 10 for _ in range(10)]
            for k, l in itertools.product(range(10), repeat=2):
                if tmp[k][l] == 'o' and not seen[k][l]:
                    seen[k][l] = True
                    cnt[0] += 1
                    dfs(k, l, tmp, seen)

            if cnt[0] == 1:
                ans = 'YES'
                break

    print(ans)

if __name__ == '__main__':
    resolve()
