import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    s = sum(A)
    if s<=N:
        print(N-s)
    else:
        print(-1)

if __name__ == '__main__':
    resolve()
