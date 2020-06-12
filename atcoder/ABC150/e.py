N = int(input())
C = list(map(int, input().split()))

a = 10**9+7
C = list(reversed(sorted(C)))

count = 0
# Cに掛ける数
# N=1 1
# N=2 2, 3
# N=3 4, 6, 8
# N=4 8, 12, 16, 20
for i in range(0, N):
    count += C[i] * (2+i)

print(count * 4**(N-1) % a)