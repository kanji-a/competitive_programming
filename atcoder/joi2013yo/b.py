import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)] 

    ans = [0]*N
    for i in range(3):
        tmp = []
        for j in range(N):
            tmp.append(S[j][i])
        for j in range(N):
            if tmp.count(S[j][i])==1:
                ans[j] += S[j][i]

    for i in ans:
        print(i)

if __name__ == '__main__':
    resolve()
