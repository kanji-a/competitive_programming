import numpy as np
 
N = int(input())
P = list(map(int, input().split()))

cnt = 0
minimum = np.inf

for i in range(N):
    if P[i] <= minimum:
        minimum = P[i]
        cnt += 1

print(cnt)