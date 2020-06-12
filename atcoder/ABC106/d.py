import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N, M, Q = map(int, input().split())
    L = [0]*M
    R = [0]*M
    p = [0]*Q
    q = [0]*Q
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    for i in range(Q):
        p[i], q[i] = map(int, input().split())

    temp = [[0]*N for _ in range(N)]
    #s[i][j]: 左がi、右が0からjまでのものの累積個数
    s = [[0]*(N+1) for _ in range(N)]
    for m in range(M):
        temp[L[m]-1][R[m]-1] += 1
    for i in range(N):
        for j in range(N):
            s[i][j+1] = s[i][j] + temp[i][j]

    for i in range(Q):
        ans = 0
        for j in range(p[i]-1, q[i]):
            ans += s[j][q[i]]-s[j][p[i]-1]
        print(ans)

if __name__ == '__main__':
    resolve()
