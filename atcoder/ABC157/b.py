import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    A = [list(map(int, input().split())) for _ in range(3)]
    N = int(input())
    B = [int(input()) for _ in range(N)]

    for b in B:
        for i, a in enumerate(A):
            for j, aa in enumerate(a):
                if b == aa:
                    A[i][j] = 0

    ans = 'No'
    for i in range(3):
        if A[i][0] == A[i][1] == A[i][2]:
            ans = 'Yes'
    for i in range(3):
        if A[0][i] == A[1][i] == A[2][i]:
            ans = 'Yes'
    if A[0][0] == A[1][1] == A[2][2]:
            ans = 'Yes'
    if A[0][2] == A[1][1] == A[2][0]:
            ans = 'Yes'

    print(ans)

if __name__ == '__main__':
    resolve()
