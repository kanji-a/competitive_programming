import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    n = int(input())
    ukv = [list(map(int, input().split())) for _ in range(n)]

    ukv.sort()

    d = [-1]*n
    f = [-1]*n
    visited = [False]*n
    t = iter(range(1, 2*n+1))

    def dfs(v):
        d[v] = next(t)
        visited[v] = True
        for i in sorted(ukv[v][2:]):
            if not visited[i-1]:
                dfs(i-1)
        f[v] = next(t)

    for i in range(n):
        if not visited[i]:
            dfs(i)

    for i in range(n):
        print(i+1, d[i], f[i])

if __name__ == '__main__':
    resolve()