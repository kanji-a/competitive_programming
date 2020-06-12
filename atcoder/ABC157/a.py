import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    print((N+1)//2)

if __name__ == '__main__':
    resolve()