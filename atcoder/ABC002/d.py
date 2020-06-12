import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N, M = map(int, input().split())
    xy = [list(map(int, input().split())) for _ in range(M)]

    con = [[False]*N for _ in range(N)]
    for i in xy:
        con[i[0]-1][i[1]-1] = con[i[1]-1][i[0]-1] = True

    ans = 0
    for i in range(2**N):
        ok = True
        for j in range(N-1):
            for k in range(j+1, N):
                if (i>>j)&1 and (i>>k)&1 and not con[j][k]:
                    ok = False
        if ok:
            n = 0
            for k in range(N):
                if (i>>k)&1:
                    n += 1
            ans = max(n, ans)
    print(ans)

if __name__ == '__main__':
    resolve()
