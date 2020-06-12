import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    ans = [[-1]*W for _ in range(H)]
    for i in range(H):
        tmp = -1
        has_cloud = False
        for j in range(W):
            if S[i][j]=='c':
                tmp = 0
                has_cloud = True
            ans[i][j] = tmp
            if has_cloud:
                tmp += 1

    for i in ans:
        print(*i)

if __name__ == '__main__':
    resolve()
