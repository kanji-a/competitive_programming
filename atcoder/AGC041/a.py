N, A, B = map(int, input().split())

# print(N)
# print(A)
# print(B)

ans = 0

if (A-B)%2 == 0:
    ans =  abs(A-B)/2
else:
    ans = min(A-1, B-1, N-A, N-B)+1+(abs(A-B)-1)/2
print(int(ans))