import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    a = list(map(int, input().split()))

    a.sort(reverse=True)
    ans = 0
    for i in range(len(a)):
        ans += a[i]*(-1)**i
    print(ans)

if __name__ == '__main__':
    resolve()
