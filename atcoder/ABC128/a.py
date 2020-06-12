import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    A, P = map(int, input().split())
    print((3*A+P)//2)

if __name__ == '__main__':
    resolve()