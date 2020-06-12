import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    S = input()
    print(700+100*S.count('o'))

if __name__ == '__main__':
    resolve()