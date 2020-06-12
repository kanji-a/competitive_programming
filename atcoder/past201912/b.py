N = int(input())
A = [int(input()) for i in range(N)]

for i in range(N-1):
    diff = A[i+1] - A[i]
    if diff > 0:
        print('up', diff)
    elif diff == 0:
        print('stay')
    else:
        print('down', -diff)
