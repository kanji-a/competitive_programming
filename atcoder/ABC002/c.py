import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    xa, ya, xb, yb, xc, yc = map(int, input().split())
    print(abs((xb-xa)*(yc-ya)-(xc-xa)*(yb-ya))/2)

if __name__ == '__main__':
    resolve()
