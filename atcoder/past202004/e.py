import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    ans = [0]*N
    for i in range(N):
        cnt = 1
        tmp = A[i]-1
        while tmp!=i:
            tmp = A[tmp]-1
            cnt += 1
        ans[i] = cnt

    print(*ans)

if __name__ == '__main__':
    resolve()
