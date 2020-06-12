import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**4)

def resolve():
    m = int(input())
    n = int(input())
    c = [list(map(int, input().split())) for _ in range(n)]

    ans = [0]
    dir = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def dfs(now, step, visited):
        is_end = True
        for dy, dx in dir:
            next = (now[0]+dy, now[1]+dx)
            if 0<=next[0]<n and 0<=next[1]<m and c[next[0]][next[1]]==1 and not next in visited:
                is_end = False
                dfs(next, step+1, visited|{now})
        if is_end:
            ans[0] = max(step, ans[0])

    for i in range(n):
        for j in range(m):
            if c[i][j]==1:
                dfs((i, j), 1, set())

    print(ans[0])

if __name__ == '__main__':
    resolve()
