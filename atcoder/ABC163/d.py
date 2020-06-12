import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    p = 10**9+7

    N, K = map(int, input().split())

    ans = 0
    for i in range(K, N+2):
        #0からN+iまでの和から、N+1-iからN+1までの和
        ans += ((N-i+1)+(N))*i//2 - (i-1)*i//2 + 1
        ans %= p

    print(ans)

if __name__ == '__main__':
    resolve()
