H, A = map(int, input().split())

cnt = H//A
if H - A * cnt > 0:
    cnt += 1

print(cnt)