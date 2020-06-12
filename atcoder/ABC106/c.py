import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    S = input()
    K = int(input())

    all1flg = True
    for i in range(min(len(S), K-1)):
        if S[i]!='1':
            ans = S[i]
            all1flg = False
            break
    if all1flg:
        print(S[K-1])
    else:
        print(ans)

if __name__ == '__main__':
    resolve()
