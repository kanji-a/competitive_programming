import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    X, Y, Z = map(int, input().split())
    print(Z, X, Y)

if __name__ == '__main__':
    resolve()