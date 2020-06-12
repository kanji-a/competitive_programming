import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    A, B = map(int, input().split())
    print((A-1)*(B-1))

if __name__ == '__main__':
    resolve()