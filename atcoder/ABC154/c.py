import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    A = list(input().split())
    if len(A) == len(set(A)):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    resolve()
