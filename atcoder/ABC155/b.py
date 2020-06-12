import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    flag = True

    for a in A:
        if a%2==0:
            if not (a%3==0 or a%5==0):
                flag = False
   
    if flag:
        print('APPROVED')
    else:
        print('DENIED')

if __name__ == '__main__':
    resolve()
