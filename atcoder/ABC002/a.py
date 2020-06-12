import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    X, Y = map(int, input().split())
    print(max(X, Y))

if __name__ == '__main__':
    resolve()