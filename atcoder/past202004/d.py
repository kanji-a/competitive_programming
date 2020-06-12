import sys
input = lambda: sys.stdin.readline().rstrip() 
import re
import string

def resolve():
    S = input()

    ans = set()

    if len(S)>=1:
        for i in range(len(S)):
            ans.add(S[i:i+1])
            ans.add('.')

    if len(S)>=2:
        for i in range(len(S)-1):
            for j in [S[i], '.']:
                for k in [S[i+1], '.']:
                    ans.add(j+k)

    if len(S)>=3:
        for i in range(len(S)-2):
            for j in [S[i], '.']:
                for k in [S[i+1], '.']:
                    for l in [S[i+2], '.']:
                        ans.add(j+k+l)

    print(len(ans))

if __name__ == '__main__':
    resolve()
