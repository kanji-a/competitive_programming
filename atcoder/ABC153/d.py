H = int(input())

cnt = -1
temp_h = H
while temp_h > 0:
    temp_h //= 2
    cnt += 1

print(pow(2, cnt+1)-1)