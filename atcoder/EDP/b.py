import numpy as np

N, K = map(int, input().split())
h = np.array(list(map(int, input().split())))

# dp = np.array([-1 for _ in range(N)])
dp = np.zeros(N, dtype=int)

dp[0] = 0

for i in range(1, N):
    start = max(0, i-K)
    dp[i] = min(dp[start: i] + np.abs(h[i] - h[start: i]))

print(dp[-1])
