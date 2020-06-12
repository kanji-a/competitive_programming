N, K, M = map(int, input().split())
A = list(map(int, input().split()))

ans = max(M*N - sum(A), 0)

if ans <= K:
    print(ans)
else:
    print(-1)