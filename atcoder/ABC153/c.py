N, K = map(int, input().split())
H = list(map(int, input().split()))

H = list(reversed(sorted(H)))

print(sum(H[K:]))