import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N, Q = map(int, input().split())
    edge = [[] for _ in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    cnt = [0]*N
    for i in range(Q):
        p, x = map(int, input().split())
        cnt[p-1] += x

    stk = []
    stk.append((0, -1))
    while len(stk):
        v, par = stk.pop()
        if v>0:
            cnt[v] += cnt[par]
        for i in edge[v]:
            if i!=par:
                stk.append((i, v))

    print(*cnt)

if __name__ == '__main__':
    resolve()
