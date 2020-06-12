import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    d = [0]*N
    for i in range(N-1):
        d[i] = abs(A[i+1] - A[i])
    d[-1] = A[0] + K - A[-1]
    print(K-max(d))

if __name__ == '__main__':
    resolve()
