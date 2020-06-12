import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    S = input()

    l = len(S)//2
    if S[:l] == S[l:]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    resolve()
