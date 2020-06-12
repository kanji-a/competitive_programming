import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    r = int(input())
    print(r**2)

if __name__ == '__main__':
    resolve()