import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    while True:
        w, h = map(int, input().split())
        if w==h==0:
            break
        c = [list(map(int, input().split())) for _ in range(h)]

        stk = []
        visited = [[False]*w for _ in range(h)]
        dir = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))

        ans = 0

        for i in range(h):
            for j in range(w):
                if c[i][j]==1 and not visited[i][j]:
                    stk.append((i, j))
                    while len(stk)>0:
                        a = stk.pop()
                        visited[a[0]][a[1]] = True
                        for d in dir:
                            ad = (a[0]+d[0], a[1]+d[1])
                            if 0<=ad[0]<h and 0<=ad[1]<w and c[ad[0]][ad[1]]==1 and not visited[ad[0]][ad[1]]:
                                stk.append(ad) 
                    ans += 1

        print(ans)

if __name__ == '__main__':
    resolve()