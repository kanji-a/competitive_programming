import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    b = input()
    d = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    print(d[b])

if __name__ == '__main__':
    resolve()