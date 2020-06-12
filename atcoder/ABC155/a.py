import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    A, B, C = input().split()
    if A==B==C or (A!=B and B!=C and C!= A):
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    resolve()