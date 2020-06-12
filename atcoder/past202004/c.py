import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    S = [input() for _ in range(N)]

    for i in range(1, N):
        ret = ''
        for j in range(i, 2*N-i-1):
            if S[N-i][j-1:j+2].count('X')>0:
                ret+='X'
            else:
                ret+=S[N-i-1][j]
        S[N-1-i] = '.'*i+ret+'.'*i

    for i in S:
        print(i)        

if __name__ == '__main__':
    resolve()
