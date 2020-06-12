import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1

    ans = [0]*(N-1)
    d = [[0]*N for i in range(N)]

    for i in range(N-1):
        for j in range(i+1, N):
            if (i<X and j<X) or (Y<i and Y<j):
                d[i][j] = j-i
            elif X<=i and j<=Y:
                d[i][j] = min(j-i, (Y-X+1)-(j-i))
            elif i<X and Y<j:
                d[i][j] = j-Y+X-i+1
            elif i<X and X<=j<=Y:
                d[i][j] = X-i+min(j-X, Y-j+1)
            elif X<=i<=Y and Y<j:
                d[i][j] = min(Y-i, i-X+1)+j-Y

    for i in range(N-1):
        for j in range(i+1, N):
            ans[d[i][j]-1] += 1
        
    for i in ans:
        print(i)

if __name__ == '__main__':
    resolve()
