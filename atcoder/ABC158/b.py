import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N, A, B = map(int, input().split())
    print(A * (N // (A + B)) + min(N % (A + B), A))

if __name__ == '__main__':
    resolve()
