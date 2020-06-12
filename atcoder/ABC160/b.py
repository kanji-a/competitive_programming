import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    X = int(input())

    ans = 0
    ans += 1000 * (X // 500)
    X %= 500
    ans += 5 * (X // 5)
    print(ans)

if __name__ == '__main__':
    resolve()
