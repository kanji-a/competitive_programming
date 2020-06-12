import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    a = int(input())
    s = input()

    if a>=3200:
        print(s)
    else:
        print('red')

if __name__ == '__main__':
    resolve()