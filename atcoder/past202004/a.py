import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    S, T = input().split()

    def in_to_num(s):
        if s[0]=='B':
            return -int(s[1])
        else:
            return int(s[0])-1

    print(abs(in_to_num(S)-in_to_num(T)))

if __name__ == '__main__':
    resolve()