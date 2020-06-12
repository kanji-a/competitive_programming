import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    s = [0]*(N+1)
    for i in range(N):
        s[i+1] = s[i] + A[i]

    for k in range(1, N+1):
        ans = 0
        for m in range(N-k+1):
            ans = max(s[m+k]-s[m], ans)
        print(ans)

if __name__ == '__main__':
    resolve()