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
    N, M = LI()
    S = [list(SS()) for _ in range(N)]

    d = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def dfs(S, cy, cx):
        for dy, dx in d:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < N and 0 <= nx < M and S[ny][nx] == '.':
                S[ny][nx] = '*'
                dfs(S, ny, nx)

    # 全ての整地候補に対して連結成分カウント
    ans = 0
    # 整地候補
    for i, j in itertools.product(range(N), range(M)):
        S_ = copy.deepcopy(S)
        if S_[i][j] == '#':
            S_[i][j] = '.'
            cnt = 0
            # 始点
            for k, l in itertools.product(range(N), range(M)):
                if S_[k][l] == '.':
                    dfs(S_, k, l)
                    cnt += 1
            if cnt == 1:
                ans += 1

    print(ans)

if __name__ == '__main__':
    resolve()
