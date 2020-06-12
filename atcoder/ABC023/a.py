import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    X = input()

    print(int(X[0])+int(X[1]))

if __name__ == '__main__':
    resolve()