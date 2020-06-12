import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    H, W = map(int, input().split())
    if H==1 or W==1:
        print('1')
    else:
        print((H*W+1)//2)

if __name__ == '__main__':
    resolve()
