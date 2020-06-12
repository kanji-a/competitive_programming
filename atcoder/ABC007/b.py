import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    A = input()

    if A == 'a':
        print('-1')
    else:
        print('a')

if __name__ == '__main__':
    resolve()
