N, Y = map(int, input().split())

exist = False
for x in range(N+1):
    for y in range(N+1-x):
        z = N-x-y
        if 10000*x+5000*y+1000*z == Y:
            exist = True
            print(x, y, z)
            break
    else:
        continue
    break

if not exist: print('-1 -1 -1')