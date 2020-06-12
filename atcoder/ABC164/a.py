import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    S, W = map(int, input().split())

    if S<=W:
        print('unsafe')
    else:
        print('safe')

if __name__ == '__main__':
    resolve()