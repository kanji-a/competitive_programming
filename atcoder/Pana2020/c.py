import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    a, b, c = map(int, input().split())
    if c-a-b > 0:
        if 4*a*b < (c-a-b)**2:
            print('Yes')
        else:
            print('No')
    else:
        print('No')


if __name__ == '__main__':
    resolve()
