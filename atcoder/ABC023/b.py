import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    S = input()

    ok = True
    c = N//2
    if N%2==1 and S[c]=='b':
        for i in range(N-c):
            if i%3==1:
                if S[c+i]!='c' or S[c-i]!='a':
                    ok = False
            if i%3==2:
                if S[c+i]!='a' or S[c-i]!='c':
                    ok = False
            if i%3==0:
                if S[c+i]!='b' or S[c-i]!='b':
                    ok = False
    else:
        ok = False

    if ok:
        print(c)
    else:
        print(-1)
                    

if __name__ == '__main__':
    resolve()
