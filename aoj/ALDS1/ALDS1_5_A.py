import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    m = list(map(int, input().split()))

    a = [False]*(max(m)+1)
    for j in range(2**n):
        s = 0
        for k in range(n):
            if (j >> k) & 1:
                s += A[k]
        if s<=max(m):
            a[s] = True
    for i in m:
        if a[i]:
            print('yes')
        else:
            print('no')

if __name__ == '__main__':
    resolve()