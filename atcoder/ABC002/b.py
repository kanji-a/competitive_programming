import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    W = input()
    print(''.join([w for w in W if w not in ('a', 'i', 'u', 'e', 'o')]))

if __name__ == '__main__':
    resolve()
