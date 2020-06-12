import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    S = input()

    a = S.count('a')
    b = S.count('b')
    c = S.count('c')

    if a<b:
        if b<c:
            print('c')
        else:
            print('b')
    else:
        if a<c:
            print('c')
        else:
            print('a')

if __name__ == '__main__':
    resolve()
