import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    m = int(input())
    n = int(input())
    c = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    stk = []
    dir = ((0, 1), (1, 0), (0, -1), (-1, 0))

    for i in range(n):
        for j in range(m):
            if c[i][j]==1:
                print(i, j)
                stk.append(((i, j), 1, set()))
                step = 0
                # visited = set()
                while len(stk)>0:
                    # print(stk)
                    k = stk.pop()
                    # visited.add(k[0])
                    print('k', k)
                    step = max(k[1], step)
                    for dy, dx in dir:
                        kd = (k[0][0]+dy, k[0][1]+dx)
                        if 0<=kd[0]<n and 0<=kd[1]<m and c[kd[0]][kd[1]]==1 and not kd in k[2]:
                            k[2].add(k[0])
                            stk.append((kd, k[1]+1, k[2]))
                ans = max(step, ans) 

    print(ans)

if __name__ == '__main__':
    resolve()
