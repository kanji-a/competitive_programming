import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    S = [input() for _ in range(N)]
    if S.count('black') >= (len(S)+1)//2:
        print('black')
    else:
        print('white')

if __name__ == '__main__':
    resolve()
