import numpy as np

H, N = map(int, input().split())
AB = np.array([list(map(int, input().split())) for i in range(N)])
A = AB[:, 0]
B = AB[:, 1]

# インデックスはライフ 値はそれを以下にする最小MP
dp = np.array([0 for i in range(H+1)])

for i in range(1, H+1):
    dp[i] = np.min(dp[np.maximum(i - A, 0)] + B)

print(dp[-1])