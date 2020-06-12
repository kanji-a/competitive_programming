import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    C = [int(input()) for _ in range(N)]

    C.append(0)
    C1 = []
    cnt = 1
    for i in range(1, N+1):
        if C[i-1]==C[i]:
            cnt += 1
        else:
            C1.append((C[i-1], cnt))
            cnt = 1

    S = [0]*(N+1)
    sum = 0
    for i in C1:


if __name__ == '__main__':
    resolve()
