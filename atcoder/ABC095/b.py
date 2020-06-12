import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N, X = map(int, input().split())
    m = [int(input()) for _ in range(N)]

    m.sort()
    X -= sum(m)
    ans = N
    i = 0
    while X>0 and i<N:
        ans += X//m[i]
        X %= m[i]
        i += 1

    print(ans)

if __name__ == '__main__':
    resolve()
