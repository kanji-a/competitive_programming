import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    X, Y = map(int, input().split())
    p = 10**9+7

    def combMod(n, r, p):
        numer = 1
        denom = 1
        for i in range(1, r+1):
            numer = numer * (n-r+i) % p
            denom = denom * i % p
        return numer * pow(denom, p-2, p) % p

    if (X+Y)%3==0 and Y<=X*2 and X<=Y*2:
        n = (X+Y)//3
        r = X-(X+Y)//3
        print(combMod(n, r, p))
    else:
        print('0')

if __name__ == '__main__':
    resolve()