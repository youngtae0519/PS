import sys

input = sys.stdin.readline

S = input().rstrip()
is_special = False
arr = []
for i in range(len(S)):
    if S[i] == '<':
        while len(arr) != 0:
            print(arr.pop(), end = "")
        is_special = True
        print(S[i], end = "")
    elif S[i] == '>':
        is_special = False
        print(S[i], end = "")
    elif is_special:
        print(S[i], end = "")
    elif S[i] == ' ':
        while len(arr) != 0:
            print(arr.pop(), end = "")
        print(S[i], end = "")
    else:
        arr.append(S[i])
        
while len(arr) != 0:
    print(arr.pop(), end = "")