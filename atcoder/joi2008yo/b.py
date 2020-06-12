import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    S = input()

    c_joi = 0
    c_ioi = 0
    for i in range(len(S)-2):
        s = S[i:i+3]
        if s=='JOI':
            c_joi += 1
        if s=='IOI':
            c_ioi += 1
    print(c_joi)
    print(c_ioi)

if __name__ == '__main__':
    resolve()
