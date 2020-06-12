import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    A, B, C, D = map(int, input().split())
    if C//B+(C%B>0) <= A//D+(A%D>0):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    resolve()
