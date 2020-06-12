import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    if N==3 or N%3==0:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    resolve()