import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    S = input()
    if S[0] == S[1] == S[2]:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    resolve()