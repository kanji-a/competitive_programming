import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    SP = [input().split() for _ in range(N)]

    SP = enumerate(SP)
    SP = sorted(SP, key=lambda x: (x[1][0], -int(x[1][1])))
    for i in SP:
        print(i[0]+1)    

if __name__ == '__main__':
    resolve()
