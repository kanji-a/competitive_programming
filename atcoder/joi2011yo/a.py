import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    t = [int(input()) for _ in range(4)]

    s = sum(t)
    print(s//60)
    print(s%60)

if __name__ == '__main__':
    resolve()