N = int(input())
txy = [list(map(int, input().split())) for _ in range(N)]

txy = [[0, 0, 0]] + txy
ans = 'Yes'
for i in range(len(txy)-1):
    diff_time = txy[i+1][0] - txy[i][0]
    diff_xy = abs(txy[i+1][1] - txy[i][1]) + abs(txy[i+1][2] - txy[i][2])
    # 到達不能条件
    #   道のりより時間が短い
    #   パリティ違う
    if diff_time < diff_xy or diff_time%2 != diff_xy%2:
        ans = 'No'
        break

print(ans)