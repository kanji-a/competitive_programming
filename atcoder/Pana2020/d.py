import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    
    def rec(n, maxchr, ans):
        if n==N:
            print(ans)
        else:
            for i in range(maxchr):
                rec(n+1, maxchr, ans+chr(i+97))
            rec(n+1, maxchr+1, ans+chr(maxchr+97))

    rec(0, 0, '')

if __name__ == '__main__':
    resolve()
