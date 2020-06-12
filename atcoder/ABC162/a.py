import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = input()

    if '7' in N:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    resolve()