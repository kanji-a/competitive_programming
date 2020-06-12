import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    M = int(input())
    A = list(map(int, input().split()))
    B = [list(map(int, input().split())) for _ in range(M)]

    ans = [0]*N
    for i in range(M):
        for j in range(N):
            if B[i][j]-1==A[i]-1:
                ans[j] += 1
            else:
                ans[A[i]-1] += 1

    for i in ans:
        print(i)

if __name__ == '__main__':
    resolve()
