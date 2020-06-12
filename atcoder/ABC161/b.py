import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    if len([a for a in A if a>=sum(A)/(4*M)])>=M:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    resolve()
