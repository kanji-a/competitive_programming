import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    total = sum(A[0:K])
    total_max = total
    for i in range(0, N-K):
        total -= A[i]
        total += A[i+K]
        total_max = max(total, total_max)

    print((total_max+K)/2)

if __name__ == '__main__':
    resolve()
