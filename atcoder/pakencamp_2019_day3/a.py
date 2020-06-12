import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    A, B = map(int, input().split())
    print(B-A+1)

if __name__ == '__main__':
    resolve()