import re

S = input()
m = re.fullmatch(r'[0-9][0-9][0-9]', S)
if m:
    print(int(S)*2)
else:
    print('error')