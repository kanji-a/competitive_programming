import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    H, W = map(int, input().split())
    s = [input() for _ in range(H)]

    ans = [[0]*W for _ in range(H)]
    if s[0][0]=='#':
        ans[0][0] = 1
    for i in range(1, W+H-1):
        for y in range(max(0, i-(W-1)), min(i+1, H)):
            x = i-y
            if y==0:
                if s[y][x-1]=='.' and s[y][x]=='#':
                    ans[y][x] = ans[y][x-1] + 1
                else:
                    ans[y][x] = ans[y][x-1]
            elif x==0:
                if s[y-1][x]=='.' and s[y][x]=='#':
                    ans[y][x] = ans[y-1][x] + 1
                else:
                    ans[y][x] = ans[y-1][x]
            else:
                if s[y][x]=='#':
                    ans[y][x] = min(ans[y-1][x]+(1 if s[y-1][x]=='.' else 0), ans[y][x-1]+(1 if s[y][x-1]=='.' else 0))
                else:
                    ans[y][x] = min(ans[y-1][x], ans[y][x-1])
    print(ans[-1][-1])

if __name__ == '__main__':
    resolve()