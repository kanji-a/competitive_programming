import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    S = input()

    ans = 0
    for i in range(1000):
        s = str(i).zfill(3)
        i0 = S.find(s[0])
        if i0 != -1:
            i1 = S[i0+1:].find(s[1])
            if i1 != -1:
                i2 = S[i0+i1+2:].find(s[2])
                if i2 != -1:
                    ans += 1

    print(ans)

if __name__ == '__main__':
    resolve()
