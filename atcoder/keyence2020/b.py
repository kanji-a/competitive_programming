N = int(input())
XL = [list(map(int, input().split())) for _ in range(N)]

XL = sorted(XL, key=lambda x: x[0]+x[1])

ans = 1
right = XL[0][0] + XL[0][1]

for i in range(1, N):
    if right <= XL[i][0] - XL[i][1]:
        right = XL[i][0] + XL[i][1]
        ans += 1

print(ans)