import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N, P = map(int, input().split())
    S = input()

    ans = 0

    # しゃくとり法
    r = 0
    for l in range(N):
        while r<N and int(S[l:r+1])%p==0:
            ans += 1
            r += 1

if __name__ == '__main__':
    resolve()
