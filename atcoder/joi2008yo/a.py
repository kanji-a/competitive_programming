import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())

    ans = 0
    back = 1000 - N
    ans += back//500
    back %= 500
    ans += back//100
    back %= 100
    ans += back//50
    back %= 50
    ans += back//10
    back %= 10
    ans += back//5
    back %= 5
    ans += back
    print(ans)

if __name__ == '__main__':
    resolve()