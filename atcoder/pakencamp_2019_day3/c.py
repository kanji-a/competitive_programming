import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for t1 in range(M-1):
        for t2 in range(t1+1, M):
            score = 0
            for i in range(N):
                score += max(A[i][t1], A[i][t2])
            ans = max(score, ans)

    print(ans)

if __name__ == '__main__':
    resolve()
