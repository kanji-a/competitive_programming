import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    X, Y, A, B, C = map(int, input().split())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    r = list(map(int, input().split()))
    pp = sorted(p, reverse=True)[0:X]
    qq = sorted(q, reverse=True)[0:Y]
    ppqqr = list(sorted(pp+qq+r, reverse=True))

    print(sum(ppqqr[0:X+Y]))

if __name__ == '__main__':
    resolve()
