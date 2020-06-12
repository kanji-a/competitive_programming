import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())

    print(int(N**0.5)**2)

if __name__ == '__main__':
    resolve()
