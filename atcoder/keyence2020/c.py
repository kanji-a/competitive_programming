N, K, S = map(int, input().split())
amax = 10**9

ans = [S for _ in range(K)] + [(S+1)%amax for _ in range(N-K)]
print(' '.join(map(str, ans)))