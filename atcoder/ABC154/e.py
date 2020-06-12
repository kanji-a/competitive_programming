import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = input()
    K = int(input())

    L = len(N)

    dp0 = [[0]*K for _ in range(L)]
    dp1 = [[0]*K for _ in range(L)]

    dp0[0][1] = N[0]-1
    dp1[0][1] = 1

    for i in range(1, L):
        for k in range(K):
            dp0[i][k] = dp0+dp1
            dp1[i][k] = dp1[i-1][k]


if __name__ == '__main__':
    resolve()
