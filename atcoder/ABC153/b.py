H, N = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)
if total >= H:
    print('Yes')
else:
    print('No')
